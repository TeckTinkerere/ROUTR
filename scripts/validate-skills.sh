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
  echo "FAIL: no python3/python on PATH — checks 9-11 (links, eval JSON) skipped"
  fail=$((fail + 1))
fi

echo "== 1. Frontmatter name == folder name =="
for dir in skills/*/; do
  name=$(basename "$dir")
  skill_md="${dir}SKILL.md"
  [ -f "$skill_md" ] || continue
  fm_name=$(grep -m1 '^name:' "$skill_md" | sed 's/^name:[[:space:]]*//' | tr -d '"' | tr -d '\r')
  if [ "$fm_name" != "$name" ]; then
    note_fail "$skill_md: frontmatter name '$fm_name' != folder name '$name'"
  fi
done

echo
echo "== 2. Router descriptions contain 'Use when:' =="
for dir in skills/routr-*/; do
  name=$(basename "$dir")
  skill_md="${dir}SKILL.md"
  [ -f "$skill_md" ] || continue
  case "$name" in
    routr-catalog) continue ;; # reference skill, not a situational router
  esac
  if ! grep -q 'Use when:' "$skill_md"; then
    note_fail "$skill_md: description missing 'Use when:' trigger phrase"
  fi
done

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
for dir in skills/routr-*/; do
  name=$(basename "$dir")
  case "$name" in
    routr-router|routr-catalog|routr-depth-*) continue ;;
  esac
  if ! grep -q -- "$name\$\|$name \|$name)" "$ROUTER_TREE" 2>/dev/null && ! grep -q "$name" "$ROUTER_TREE"; then
    note_fail "$name: not referenced anywhere in $ROUTER_TREE decision tree"
  fi
  if ! grep -q "\`$name\`" "$RESOLUTION"; then
    note_warn "$name: not listed in $RESOLUTION router precedence list"
  fi
done

echo
echo "== 6. Description length budget (FAIL > 320 chars, WARN > 280 chars) =="
for dir in skills/routr-*/; do
  name=$(basename "$dir")
  skill_md="${dir}SKILL.md"
  [ -f "$skill_md" ] || continue
  desc=$(grep -m1 '^description:' "$skill_md" | sed 's/^description:[[:space:]]*//' | tr -d '\r')
  # strip one layer of surrounding quotes, if present
  desc="${desc%\"}"
  desc="${desc#\"}"
  len=${#desc}
  if [ "$len" -gt 320 ]; then
    note_fail "$skill_md: description is $len chars (> 320 limit)"
  elif [ "$len" -gt 280 ]; then
    note_warn "$skill_md: description is $len chars (> 280 soft budget)"
  fi
done

echo
echo "== 7. Situational router descriptions contain 'Not for:' =="
for dir in skills/routr-*/; do
  name=$(basename "$dir")
  skill_md="${dir}SKILL.md"
  [ -f "$skill_md" ] || continue
  case "$name" in
    routr-router|routr-catalog|routr-depth-*) continue ;;
  esac
  if ! grep -q 'Not for:' "$skill_md"; then
    note_fail "$skill_md: description missing 'Not for:' boundary phrase"
  fi
done

echo
echo "== 8. SKILL.md line cap (routers <= 150, depth fallbacks <= 200) =="
for dir in skills/routr-*/; do
  name=$(basename "$dir")
  skill_md="${dir}SKILL.md"
  [ -f "$skill_md" ] || continue
  case "$name" in
    routr-catalog) continue ;; # catalog has its own (unchecked here) budget
  esac
  lines=$(wc -l < "$skill_md" | tr -d ' ')
  case "$name" in
    routr-depth-*)
      if [ "$lines" -gt 200 ]; then
        note_fail "$skill_md: $lines lines (> 200 line cap for depth fallbacks)"
      fi
      ;;
    *)
      if [ "$lines" -gt 150 ]; then
        note_fail "$skill_md: $lines lines (> 150 line cap for routers)"
      fi
      ;;
  esac
done

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
