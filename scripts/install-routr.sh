#!/usr/bin/env bash
# ROUTR bundle installer — pick groups, then install selected routers.
# v2: routr-* names

set -euo pipefail

declare -A BUNDLE_SKILLS
BUNDLE_SKILLS[meta]="routr-router routr-catalog routr-depth-debug routr-depth-frontend routr-depth-plan routr-depth-ship routr-depth-test"
BUNDLE_SKILLS[core]="routr-debug routr-ship routr-plan routr-test routr-review routr-refactor routr-deploy routr-database routr-qa routr-security routr-explore routr-integrate routr-agents"
BUNDLE_SKILLS[frontend]="routr-frontend routr-motion"
BUNDLE_SKILLS[video]="routr-video"
BUNDLE_SKILLS[mobile]="routr-mobile"
BUNDLE_SKILLS[marketing]="routr-marketing"
BUNDLE_SKILLS[ai]="routr-ai"

echo ""
echo "ROUTR v2 — select bundles (comma-separated numbers, or 'a' for all, Enter for skills CLI picker)"
echo ""
echo "  1) Meta (router + catalog + depth fallbacks)"
echo "  2) Core engineering"
echo "  3) Frontend"
echo "  4) Video"
echo "  5) Mobile"
echo "  6) Marketing & SEO"
echo "  7) AI / LLM apps"
echo "  8) Use skills CLI checkbox picker (recommended if unsure)"
echo ""
read -r -p "Choice [8]: " choice
choice="${choice:-8}"

if [[ "$choice" == "8" ]]; then
  echo ""
  echo "Launching interactive skills CLI (Space = toggle, Enter = confirm)..."
  npx skills add TeckTinkerere/ROUTR -g --copy
  exit 0
fi

keys=(meta core frontend video mobile marketing ai)
selected_skills=()

if [[ "$choice" == "a" || "$choice" == "A" ]]; then
  for k in "${keys[@]}"; do
    selected_skills+=(${BUNDLE_SKILLS[$k]})
  done
else
  IFS=',' read -ra nums <<< "$choice"
  for n in "${nums[@]}"; do
    n=$(echo "$n" | tr -d ' ')
    idx=$((n - 1))
    if [[ $idx -ge 0 && $idx -lt ${#keys[@]} ]]; then
      selected_skills+=(${BUNDLE_SKILLS[${keys[$idx]}]})
    fi
  done
fi

mapfile -t unique_skills < <(printf '%s\n' "${selected_skills[@]}" | sort -u)

if [[ ${#unique_skills[@]} -eq 0 ]]; then
  echo "No bundles selected — cancelled."
  exit 0
fi

skill_args=()
for s in "${unique_skills[@]}"; do
  skill_args+=(--skill "$s")
done

echo ""
echo "Installing ${#unique_skills[@]} skill(s):"
printf '  - %s\n' "${unique_skills[@]}"
echo ""

npx skills add TeckTinkerere/ROUTR -g --copy -y "${skill_args[@]}"

echo ""
echo "Install child bundles from routr-catalog/references/skill-registry.md for full depth."
echo "Done. Restart your agent, then type / to search routr-* skills."
