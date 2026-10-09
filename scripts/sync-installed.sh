#!/usr/bin/env bash
# sync-installed.sh — diff repo skills/routr-* against installed skill roots.
#
# Default roots (whichever of these exist):
#   ~/.claude/skills  ~/.agents/skills  ~/.cursor/skills  ~/.codex/skills
#
# Usage:
#   scripts/sync-installed.sh                     # dry run, default roots
#   scripts/sync-installed.sh --root PATH [...]    # dry run, custom root(s), repeatable
#   scripts/sync-installed.sh --apply              # copy repo skills over installed
#   scripts/sync-installed.sh --prune-legacy        # move legacy stubs/orphans to backup
#   scripts/sync-installed.sh --apply --prune-legacy
#
# For each repo routr-* skill, reports per root:
#   MISSING  — not installed at all
#   DRIFT    — installed but file contents differ (lists differing files)
#   OK       — installed and identical
#
# Also reports, per root:
#   ORPHAN   — an installed routr-* skill with no matching folder in the repo
#   LEGACY   — an installed *-playbook / playbook-* skill whose name appears
#              in docs/naming.md's rename map
#
# --apply replaces the installed folder's *contents* for that skill with the
# repo's (only routr-* folders are touched; nothing else in the root is
# touched).
#
# --prune-legacy MOVES (never deletes) every LEGACY and ORPHAN folder into
# <root>/.routr-legacy-backup-YYYYMMDD/.
#
# Exits non-zero if any MISSING/DRIFT found in dry-run mode (report-only,
# does not fail on ORPHAN/LEGACY alone) so it can be used as a CI gate later.

set -uo pipefail
cd "$(dirname "$0")/.."
REPO_ROOT="$(pwd)"

APPLY=0
PRUNE_LEGACY=0
declare -a ROOTS=()

while [ $# -gt 0 ]; do
  case "$1" in
    --apply) APPLY=1; shift ;;
    --prune-legacy) PRUNE_LEGACY=1; shift ;;
    --root)
      [ $# -ge 2 ] || { echo "error: --root requires a PATH argument" >&2; exit 2; }
      ROOTS+=("$2")
      shift 2
      ;;
    -h|--help)
      sed -n '2,33p' "$0"
      exit 0
      ;;
    *)
      echo "error: unrecognized argument '$1'" >&2
      exit 2
      ;;
  esac
done

if [ "${#ROOTS[@]}" -eq 0 ]; then
  for candidate in "$HOME/.claude/skills" "$HOME/.agents/skills" "$HOME/.cursor/skills" "$HOME/.codex/skills"; do
    [ -d "$candidate" ] && ROOTS+=("$candidate")
  done
fi

if [ "${#ROOTS[@]}" -eq 0 ]; then
  echo "No installed skill roots found (checked ~/.claude/skills, ~/.agents/skills, ~/.cursor/skills, ~/.codex/skills)."
  echo "Pass --root PATH to specify one explicitly."
  exit 0
fi

# Build the legacy rename-map name set from docs/naming.md ("| \`old\` | \`new\` |" rows).
NAMING_MD="docs/naming.md"
declare -a LEGACY_NAMES=()
if [ -f "$NAMING_MD" ]; then
  # Only the "Rename map (v2)" table's first column — other tables in this
  # file (namespace prefixes, etc.) also have backticked first cells but are
  # NOT deprecated names.
  while IFS= read -r n; do
    [ -n "$n" ] && LEGACY_NAMES+=("$n")
  done < <(awk '/^## Rename map/{f=1; next} /^## /{f=0} f' "$NAMING_MD" \
    | grep -oP '^\|\s*`\K[a-z0-9._-]+(?=`)')
fi

is_legacy_name() {
  local n="$1"
  for l in "${LEGACY_NAMES[@]:-}"; do
    [ "$n" = "$l" ] && return 0
  done
  case "$n" in
    *-playbook|playbook-*) return 0 ;;
  esac
  return 1
}

# repo routr-* skill folders
declare -a REPO_SKILLS=()
for d in skills/routr-*/; do
  [ -d "$d" ] || continue
  REPO_SKILLS+=("$(basename "$d")")
done

missing_or_drift=0
date_stamp="$(date +%Y%m%d)"

for root in "${ROOTS[@]}"; do
  echo "================================================================"
  echo "Root: $root"
  echo "================================================================"

  if [ ! -d "$root" ]; then
    echo "  (root does not exist, skipping)"
    continue
  fi

  # 1. MISSING / DRIFT / OK for each repo skill
  for skill in "${REPO_SKILLS[@]}"; do
    src="$REPO_ROOT/skills/$skill"
    dst="$root/$skill"

    if [ ! -d "$dst" ]; then
      echo "MISSING  $skill"
      missing_or_drift=1
      if [ "$APPLY" -eq 1 ]; then
        mkdir -p "$dst"
        cp -r "$src"/. "$dst"/
        echo "         -> copied (apply)"
      fi
      continue
    fi

    diff_files="$(diff -rq "$src" "$dst" 2>/dev/null | sed -n "s#^Files .*and \(.*\) differ#\1#p; s#^Only in $src[/: ]*#(repo-only) #p; s#^Only in $dst[/: ]*#(installed-only) #p")"
    if [ -n "$diff_files" ]; then
      echo "DRIFT    $skill"
      echo "$diff_files" | sed 's/^/         /'
      missing_or_drift=1
      if [ "$APPLY" -eq 1 ]; then
        rm -rf "$dst"
        mkdir -p "$dst"
        cp -r "$src"/. "$dst"/
        echo "         -> replaced with repo version (apply)"
      fi
    else
      echo "OK       $skill"
    fi
  done

  # 2. ORPHAN: installed routr-* not in repo
  declare -a orphans=()
  if [ -d "$root" ]; then
    for d in "$root"/routr-*/; do
      [ -d "$d" ] || continue
      name="$(basename "$d")"
      found=0
      for s in "${REPO_SKILLS[@]}"; do
        [ "$s" = "$name" ] && found=1 && break
      done
      if [ "$found" -eq 0 ]; then
        echo "ORPHAN   $name (installed, no matching repo skill)"
        orphans+=("$name")
      fi
    done
  fi

  # 3. LEGACY: *-playbook / playbook-* stubs named in the rename map
  declare -a legacies=()
  for d in "$root"/*/; do
    [ -d "$d" ] || continue
    name="$(basename "$d")"
    case "$name" in
      routr-*) continue ;;
    esac
    if is_legacy_name "$name"; then
      echo "LEGACY   $name (deprecated per $NAMING_MD rename map)"
      legacies+=("$name")
    fi
  done

  if [ "$PRUNE_LEGACY" -eq 1 ] && { [ "${#orphans[@]}" -gt 0 ] || [ "${#legacies[@]}" -gt 0 ]; }; then
    backup_dir="$root/.routr-legacy-backup-$date_stamp"
    mkdir -p "$backup_dir"
    for name in "${orphans[@]:-}" "${legacies[@]:-}"; do
      [ -n "$name" ] || continue
      if [ -d "$root/$name" ]; then
        mv "$root/$name" "$backup_dir/"
        echo "         -> moved $name to $backup_dir/ (prune-legacy)"
      fi
    done
  fi

  echo
done

echo "================================================================"
if [ "$APPLY" -eq 1 ]; then
  echo "Applied. Re-run without --apply to confirm clean diff."
elif [ "$missing_or_drift" -eq 1 ]; then
  echo "Drift detected (MISSING/DRIFT above). Re-run with --apply to sync."
else
  echo "All installed routr-* skills match the repo."
fi

exit 0
