---
name: routr-mobile
description: "Build Expo or React Native apps (screens, navigation, native UI). Use when: mobile app, Expo, React Native, iOS, Android, EAS, native screen. Not for: web-only UI (→ routr-frontend)."
---

# routr-mobile

**Goal:** native-quality mobile UI with Expo/RN best practices.

## 0. Bootstrap

See `routr-catalog/references/skill-registry.md`:

| Order | Skill | Role |
|-------|-------|------|
| 1 | `building-native-ui` | Expo Router, native patterns, RN conventions |
| 2 | `vercel-react-native-skills` | RN performance |
| 3 | `native-data-fetching` | Data loading |
| 4 | `find-docs` | Expo API docs |
| 5 | `symdex-code-search` | Existing screens |

NativeWind projects: wire Expo's Tailwind setup (`tailwind.config.js` + Metro/Babel config) before building.

## 1. Discover

Expo SDK version; router vs legacy; SymDex `app/`.

## 2. Build

`building-native-ui`, with `frontend-design` tokens adapted for mobile density (larger touch targets, platform-native spacing).

**Skip:** web shadcn, web Framer patterns.

## 3. Ship

Store copy → `routr-marketing` (`aso`). EAS → `expo-deployment`, `routr-deploy`.

## Handoff

| Need | Router |
|------|--------|
| Landing page | `routr-frontend` |
| SEO / ASO | `routr-marketing` |
| Backend API | `routr-integrate` |
| Mobile bug | `routr-debug` |

## Anti-patterns

- Web React patterns (div, CSS grid) in RN
- Skip safe areas and accessibility
