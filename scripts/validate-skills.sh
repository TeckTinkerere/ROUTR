#!/usr/bin/env bash
# ROUTR consistency validator — enforces docs/authoring.md checklist items that
# are mechanically checkable. Run from repo root: scripts/validate-skills.sh
#
# Checks:
#   1. Each skills/routr-*/SKILL.md frontmatter `name:` matches its folder name.
#   2. Each router description contains "Use when:".
#   3. Every `backticked` child-skill reference in a router body resolves to a
#      canonical name or alias in skill-registry.md (routr-* names excluded).
#   4. No duplicate canonical rows in skill-registry.md.
#   5. Every routr-{domain} router (excluding routr-router, routr-catalog,
#      routr-depth-*) is listed in routr-router's decision tree AND in
#      resolution.md's router precedence list.
#   6. Description length budget: FAIL > 320 chars, WARN > 280 chars.
#   7. Situational routers' description contains "Not for:" (depth/catalog exempt).
#   8. SKILL.md line cap: FAIL > 150 lines for routers, > 200 for depth fallbacks.
#   9. Every relative markdown link under skills/**.md resolves to a real file.
#   10. Every evals/*.eval.json parses, and every expected_router /
#       expected_chain / must_not_load entry names an existing skills/routr-*
#       folder.
#   11. Every situational router has >=1 eval prompt naming it as
#       expected_router somewhere in evals/ (WARN only).
#
# Checks 9-11 are implemented in scripts/_validate_helpers.py (stdlib-only
# Python) because bash JSON/link parsing gets unreadable fast.
#
# Checks 1, 2, 5, 6, 7, 8 all loop over every skills/routr-* directory; doing
# that in bash means forking grep/sed/wc/basename per skill (~0.15s per fork
# on Windows/Git Bash * ~28 skills * several forks each == most of this
# script's runtime). They're implemented as one `skills` subcommand in
# scripts/_validate_helpers.py instead, called ONCE, so bash pays a single
# python startup cost instead of forking per skill per check.
#
# Exits non-zero on any failure so it can gate CI.

set -uo pipefail
cd "$(dirname "$0")/.."

fail=0
warn=0

note_fail() { echo "FAIL: $1"; fail=$((fail + 1)); }
note_warn() { echo "WARN: $1"; warn=$((warn + 1)); }

REGISTRY="skills/routr-catalog/references/skill-registry.md"
ROUTER_TREE="skills/routr-router/SKILL.md"
RESOLUTION="skills/routr-catalog/references/resolution.md"

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

PYTHON="$(command -v python3 || command -v python || true)"
if [ -z "$PYTHON" ]; then
  echo "FAIL: no python3/python on PATH — checks 1,2,5-11 (links, eval JSON, per-skill checks) skipped"
  fail=$((fail + 1))
fi

# Run checks 1, 2, 5, 6, 7, 8 in a single python pass. Output lines look like
# "1:FAIL: msg" / "5:WARN: msg" — the leading "N:" says which section header
# the line belongs under; emit_section() below strips it and prints the rest.
"$PYTHON" scripts/_validate_helpers.py skills skills "$ROUTER_TREE" "$RESOLUTION" > "$TMP_DIR/check_skills_out.txt" 2>&1 || true

emit_section() {
  # $1 = check number to filter for
  local n="$1"
  local prefix="${n}:"
  while IFS= read -r line; do
    case "$line" in
      "${prefix}FAIL:"*) fail=$((fail + 1)); echo "${line#"$prefix"}" ;;
      "${prefix}WARN:"*) warn=$((warn + 1)); echo "${line#"$prefix"}" ;;
    esac
  done < "$TMP_DIR/check_skills_out.txt"
}

echo "== 1. Frontmatter name == folder name =="
emit_section 1

echo
echo "== 2. Router descriptions contain 'Use when:' =="
emit_section 2

echo
echo "== 3. Child-skill references resolve to the registry =="
# Canonical names + aliases from every `name` / `alias` markdown-table cell.
: > $TMP_DIR/routr_registry_names.txt
grep -oP '^\|\s*`\K[a-z0-9._-]+' "$REGISTRY" | sort -u >> $TMP_DIR/routr_registry_names.txt
# alias column (2nd cell) may hold bare words, not backticked — collect those too.
awk -F'|' '/^\|[[:space:]]*`/{gsub(/^[[:space:]]+|[[:space:]]+$/,"",$3); if ($3!="" && $3!="—" && $3!="aliases") print $3}' "$REGISTRY" >> $TMP_DIR/routr_registry_names.txt
sort -u -o $TMP_DIR/routr_registry_names.txt $TMP_DIR/routr_registry_names.txt

grep -rhoP '`\K[a-z][a-z0-9-]{2,}(?=`)' skills --include='*.md' \
  | grep -v '^routr-' \
  | sort -u > $TMP_DIR/routr_referenced_names.txt

# Words that are markdown/table furniture or prose, not skill names.
# map/lines/signatures: lean-ctx read modes, not skill names.
# grilling: deliberately-cited non-canonical alias (routr-plan gotchas warns against it).
# remotion: npm package name / registry namespace label, not a skill itself.
# ffmpeg/ffprobe/npm/node: system binaries/runtimes referenced as prerequisites, not skills.
cat > $TMP_DIR/routr_stopwords.txt <<'EOF'
canonical
aliases
namespace
tier
routers
source
required
recommended
optional
description
docs
test
feat
fix
chore
refactor
signatures
prefers-reduced-motion
data-testid
map
lines
grilling
remotion
ffmpeg
ffprobe
npm
node
EOF

comm -23 $TMP_DIR/routr_referenced_names.txt <(sort -u $TMP_DIR/routr_registry_names.txt) \
  | grep -vxFf $TMP_DIR/routr_stopwords.txt > $TMP_DIR/routr_unresolved.txt || true

if [ -s $TMP_DIR/routr_unresolved.txt ]; then
  while IFS= read -r n; do
    note_fail "child skill '$n' is referenced in skills/ but has no row in $REGISTRY"
  done < $TMP_DIR/routr_unresolved.txt
fi

echo
echo "== 4. No duplicate canonical rows in the registry =="
dupes=$(grep -oP '^\|\s*`\K[a-z0-9._-]+' "$REGISTRY" | sort | uniq -d)
if [ -n "$dupes" ]; then
  while IFS= read -r d; do
    note_fail "canonical skill '$d' has duplicate rows in $REGISTRY"
  done <<< "$dupes"
fi

echo
echo "== 5. Every router is in routr-router's tree and resolution.md precedence =="
emit_section 5

echo
echo "== 6. Description length budget (FAIL > 320 chars, WARN > 280 chars) =="
emit_section 6

echo
echo "== 7. Situational router descriptions contain 'Not for:' =="
emit_section 7

echo
echo "== 8. SKILL.md line cap (routers <= 150, depth fallbacks <= 200) =="
emit_section 8

echo
echo "== 9. Relative markdown links in skills/**.md resolve =="
"$PYTHON" scripts/_validate_helpers.py links skills > "$TMP_DIR/check9_out.txt" 2>&1 || true
if [ -s "$TMP_DIR/check9_out.txt" ]; then
  while IFS= read -r line; do
    case "$line" in
      FAIL:*) fail=$((fail + 1)); echo "$line" ;;
      WARN:*) warn=$((warn + 1)); echo "$line" ;;
      *) echo "$line" ;;
    esac
  done < "$TMP_DIR/check9_out.txt"
fi

echo
echo "== 10/11. evals/*.eval.json validity, router-name references, and coverage =="
"$PYTHON" scripts/_validate_helpers.py evals evals skills > "$TMP_DIR/check10_out.txt" 2>&1 || true
if [ -s "$TMP_DIR/check10_out.txt" ]; then
  while IFS= read -r line; do
    case "$line" in
      FAIL:*) fail=$((fail + 1)); echo "$line" ;;
      WARN:*) warn=$((warn + 1)); echo "$line" ;;
      *) echo "$line" ;;
    esac
  done < "$TMP_DIR/check10_out.txt"
fi

echo
echo "================================"
if [ "$fail" -gt 0 ]; then
  echo "$fail failure(s), $warn warning(s)."
  exit 1
else
  echo "All checks passed ($warn warning(s))."
  exit 0
fi
