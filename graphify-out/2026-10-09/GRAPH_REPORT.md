# Graph Report - ROUTR  (2026-09-02)

## Corpus Check
- Corpus is ~15,740 words - fits in a single context window. You may not need a graph.

## Summary
- 240 nodes · 557 edges · 11 communities (10 shown, 1 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 1% AMBIGUOUS · INFERRED: 9 edges (avg confidence: 0.77)
- Token cost: 388,908 input · 0 output

## Community Hubs (Navigation)
- Debug & Agent Core Skills
- Code Review & Ship Skills
- Frontend & Motion Design
- Deploy, Marketing & Mobile
- Video Production Skills
- Testing & QA Skills
- ROUTR Architecture & Docs
- Planning & PRD Skills
- Deprecated Playbook Names
- Install Script (Bash)

## God Nodes (most connected - your core abstractions)
1. `routr-frontend` - 49 edges
2. `routr-debug` - 38 edges
3. `routr-ship` - 38 edges
4. `ROUTR README` - 32 edges
5. `routr-plan` - 31 edges
6. `ROUTR Install Guide` - 30 edges
7. `routr-agents` - 29 edges
8. `routr-video` - 29 edges
9. `routr-motion` - 28 edges
10. `routr-router` - 27 edges

## Surprising Connections (you probably didn't know these)
- `routr-depth-frontend` --semantically_similar_to--> `routr-frontend Fallback Rules`  [INFERRED] [semantically similar]
  README.md → skills/routr-frontend/references/fallback.md
- `routr-depth-plan` --semantically_similar_to--> `routr-plan Fallback Rules`  [INFERRED] [semantically similar]
  README.md → skills/routr-plan/references/fallback.md
- `lean-ctx` --references--> `routr-ship`  [AMBIGUOUS]
  skills/routr-catalog/references/skill-registry.md → README.md
- `lean-ctx` --references--> `routr-refactor`  [AMBIGUOUS]
  skills/routr-catalog/references/skill-registry.md → README.md
- `lean-ctx` --references--> `routr-explore`  [AMBIGUOUS]
  skills/routr-catalog/references/skill-registry.md → README.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **ROUTR situational routers (top layer)** — skills_routr_debug_skill_routr_debug, skills_routr_ship_skill_routr_ship, skills_routr_frontend_skill_routr_frontend, skills_routr_plan_skill_routr_plan, skills_routr_test_skill_routr_test, skills_routr_review_skill_routr_review, skills_routr_refactor_skill_routr_refactor, skills_routr_deploy_skill_routr_deploy, skills_routr_database_skill_routr_database, skills_routr_qa_skill_routr_qa, skills_routr_security_skill_routr_security, skills_routr_explore_skill_routr_explore, skills_routr_integrate_skill_routr_integrate, skills_routr_agents_skill_routr_agents, skills_routr_motion_skill_routr_motion, skills_routr_mobile_skill_routr_mobile, skills_routr_marketing_skill_routr_marketing, skills_routr_ai_skill_routr_ai, skills_routr_video_skill_routr_video [EXTRACTED 0.95]
- **routr-depth-* fallback skills** — skills_routr_depth_debug_skill_routr_depth_debug, skills_routr_depth_frontend_skill_routr_depth_frontend, skills_routr_depth_plan_skill_routr_depth_plan, skills_routr_depth_ship_skill_routr_depth_ship, skills_routr_depth_test_skill_routr_depth_test [EXTRACTED 0.90]
- **routr-debug reference documentation set** — skills_routr_debug_skill_routr_debug, skills_routr_debug_references_workflow_workflow, skills_routr_debug_references_fallback_fallback, skills_routr_debug_references_gotchas_gotchas, skills_routr_debug_references_examples_examples, skills_routr_debug_references_boundaries_boundaries [EXTRACTED 0.95]
- **ROUTR Depth Fallback Skills** — skills_routr_depth_debug_skill_routr_depth_debug, skills_routr_depth_frontend_skill_routr_depth_frontend, skills_routr_depth_plan_skill_routr_depth_plan, skills_routr_depth_ship_skill_routr_depth_ship, skills_routr_depth_test_skill_routr_depth_test [EXTRACTED 1.00]
- **routr-frontend Skill + Reference Docs** — skills_routr_frontend_skill_routr_frontend, skills_routr_frontend_references_boundaries_boundaries, skills_routr_frontend_references_examples_examples, skills_routr_frontend_references_fallback_fallback, skills_routr_frontend_references_gotchas_gotchas, skills_routr_frontend_references_workflow_workflow [EXTRACTED 1.00]
- **routr-plan Skill + Reference Docs** — skills_routr_plan_skill_routr_plan, skills_routr_plan_references_boundaries_boundaries, skills_routr_plan_references_examples_examples, skills_routr_plan_references_fallback_fallback, skills_routr_plan_references_gotchas_gotchas, skills_routr_plan_references_workflow_workflow [EXTRACTED 1.00]
- **ROUTR Router Skill System** — skills_routr_router_skill_routr_router, skills_routr_qa_skill_routr_qa, skills_routr_refactor_skill_routr_refactor, skills_routr_review_skill_routr_review, skills_routr_security_skill_routr_security, skills_routr_ship_skill_routr_ship, skills_routr_test_skill_routr_test, skills_routr_video_skill_routr_video [INFERRED 0.85]
- **routr-ship Reference Documentation Bundle** — skills_routr_ship_skill_routr_ship, skills_routr_ship_references_workflow_workflow, skills_routr_ship_references_fallback_fallback, skills_routr_ship_references_gotchas_gotchas, skills_routr_ship_references_examples_examples, skills_routr_ship_references_boundaries_boundaries [EXTRACTED 1.00]
- **routr-video Reference Documentation Bundle** — skills_routr_video_skill_routr_video, skills_routr_video_references_launch_launch, skills_routr_video_references_remotion_remotion, skills_routr_video_references_gotchas_gotchas, skills_routr_video_references_examples_examples, skills_routr_video_references_boundaries_boundaries [EXTRACTED 1.00]

## Communities (11 total, 1 thin omitted)

### Community 0 - "Debug & Agent Core Skills"
Cohesion: 0.07
Nodes (41): ai-llm-app-playbook, database-playbook, docs/naming.md (deprecated skill names), routr-agents, routr-ai, Skill Resolution (routr-catalog), advanced-evaluation, ai-sdk (+33 more)

### Community 1 - "Code Review & Ship Skills"
Cohesion: 0.07
Nodes (38): code-review-playbook, refactor-playbook, security-review-playbook, caveman-commit, caveman-review, finishing-a-development-branch, firebase-security-rules-auditor, improve-codebase-architecture (+30 more)

### Community 2 - "Frontend & Motion Design"
Cohesion: 0.08
Nodes (36): explore-codebase-playbook, frontend-motion-playbook, library-integration-playbook, context-fundamentals, find-docs, framer-motion-animator, frontend-design (Anthropic Skill), lean-ctx (+28 more)

### Community 3 - "Deploy, Marketing & Mobile"
Cohesion: 0.09
Nodes (27): deploy-playbook, marketing-seo-playbook, mobile-expo-playbook, ai-seo, aso, building-native-ui, copywriting, expo-deployment (+19 more)

### Community 4 - "Video Production Skills"
Cohesion: 0.16
Nodes (25): brag, embedded-captions, faceless-explainer, find-docs, hyperframes, motion-graphics, pr-to-video, product-launch-video (+17 more)

### Community 5 - "Testing & QA Skills"
Cohesion: 0.13
Nodes (21): e2e-qa-playbook, testing-playbook, test-driven-development (Obra), webapp-testing (Anthropic Skill), agent-browser, playwright-best-practices, playwright-cli, agent-browser (+13 more)

### Community 6 - "ROUTR Architecture & Docs"
Cohesion: 0.23
Nodes (19): ROUTR Architecture, Discovery noise problem, Progressive disclosure principle, ROUTR two-layer model, Authoring ROUTR Skills, ROUTR Naming Taxonomy, caveman-commit, requesting-code-review (Obra) (+11 more)

### Community 7 - "Planning & PRD Skills"
Cohesion: 0.15
Nodes (19): brainstorming (Obra), executing-plans (Obra), find-skills, grill-me, grill-with-docs, improve-codebase-architecture, to-prd, brainstorming (+11 more)

### Community 8 - "Deprecated Playbook Names"
Cohesion: 0.18
Nodes (11): agent-design-playbook, debugging-playbook, fix-and-ship-playbook, frontend-feature-playbook, planning-playbook, playbook-common, playbook-router, ROUTR v2 rename map (*-playbook to routr-*) (+3 more)

## Ambiguous Edges - Review These
- `routr-ship` → `lean-ctx`  [AMBIGUOUS]
  skills/routr-catalog/references/skill-registry.md · relation: references
- `routr-refactor` → `lean-ctx`  [AMBIGUOUS]
  skills/routr-catalog/references/skill-registry.md · relation: references
- `routr-explore` → `lean-ctx`  [AMBIGUOUS]
  skills/routr-catalog/references/skill-registry.md · relation: references
- `routr-frontend` → `lean-ctx`  [AMBIGUOUS]
  skills/routr-catalog/references/skill-registry.md · relation: references

## Knowledge Gaps
- **100 isolated node(s):** `install-routr.sh script`, `Skill Catalog (deprecated)`, `routr-debug Examples`, `find-skills`, `caveman` (+95 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `routr-ship` and `lean-ctx`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `routr-refactor` and `lean-ctx`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `routr-explore` and `lean-ctx`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `routr-frontend` and `lean-ctx`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **Why does `routr-frontend` connect `Frontend & Motion Design` to `Debug & Agent Core Skills`, `Code Review & Ship Skills`, `Deploy, Marketing & Mobile`, `Video Production Skills`, `Testing & QA Skills`, `ROUTR Architecture & Docs`, `Planning & PRD Skills`, `Deprecated Playbook Names`?**
  _High betweenness centrality (0.214) - this node is a cross-community bridge._
- **Why does `routr-plan` connect `Planning & PRD Skills` to `Debug & Agent Core Skills`, `Code Review & Ship Skills`, `Frontend & Motion Design`, `ROUTR Architecture & Docs`, `Deprecated Playbook Names`?**
  _High betweenness centrality (0.132) - this node is a cross-community bridge._
- **Why does `routr-ship` connect `Code Review & Ship Skills` to `Debug & Agent Core Skills`, `Frontend & Motion Design`, `Deploy, Marketing & Mobile`, `Video Production Skills`, `Testing & QA Skills`, `ROUTR Architecture & Docs`, `Planning & PRD Skills`, `Deprecated Playbook Names`?**
  _High betweenness centrality (0.127) - this node is a cross-community bridge._