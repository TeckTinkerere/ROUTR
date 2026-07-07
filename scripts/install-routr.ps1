# ROUTR bundle installer — pick groups with checkboxes, then install selected routers.
# Usage: .\scripts\install-routr.ps1
# v2: routr-* names

$ErrorActionPreference = "Stop"

$bundles = @(
    [PSCustomObject]@{
        Bundle = "Meta"
        Description = "Router + catalog + depth fallbacks"
        Skills = @("routr-router", "routr-catalog", "routr-depth-debug", "routr-depth-frontend", "routr-depth-plan", "routr-depth-ship", "routr-depth-test")
    }
    [PSCustomObject]@{
        Bundle = "Core engineering"
        Description = "Debug, ship, plan, test, review, refactor, deploy, DB, QA, security, explore"
        Skills = @(
            "routr-debug", "routr-ship", "routr-plan",
            "routr-test", "routr-review", "routr-refactor",
            "routr-deploy", "routr-database", "routr-qa",
            "routr-security", "routr-explore",
            "routr-integrate", "routr-agents"
        )
    }
    [PSCustomObject]@{
        Bundle = "Frontend"
        Description = "UI build + motion"
        Skills = @("routr-frontend", "routr-motion")
    }
    [PSCustomObject]@{
        Bundle = "Video"
        Description = "Launch, HyperFrames, Remotion (single routr-video)"
        Skills = @("routr-video")
    }
    [PSCustomObject]@{
        Bundle = "Mobile"
        Description = "Expo / React Native"
        Skills = @("routr-mobile")
    }
    [PSCustomObject]@{
        Bundle = "Marketing & SEO"
        Description = "Copy, SEO, growth"
        Skills = @("routr-marketing")
    }
    [PSCustomObject]@{
        Bundle = "AI / LLM apps"
        Description = "Vercel AI SDK, chat, RAG"
        Skills = @("routr-ai")
    }
)

Write-Host ""
Write-Host "ROUTR v2 — select bundles to install (checkbox grid)" -ForegroundColor Cyan
Write-Host ""

$selected = $bundles | Out-GridView -Title "ROUTR install bundles" -PassThru

if (-not $selected) {
    Write-Host "Cancelled — nothing installed." -ForegroundColor Yellow
    exit 0
}

$skillNames = $selected | ForEach-Object { $_.Skills } | Select-Object -Unique
$skillArgs = ($skillNames | ForEach-Object { "--skill"; $_ })

Write-Host ""
Write-Host "Installing $($skillNames.Count) skill(s):" -ForegroundColor Green
$skillNames | ForEach-Object { Write-Host "  - $_" }

$npxArgs = @("skills", "add", "TeckTinkerere/ROUTR", "-g", "--copy", "-y") + $skillArgs
& npx @npxArgs

Write-Host ""
Write-Host "Install child bundles from routr-catalog/references/skill-registry.md for full depth." -ForegroundColor Yellow
Write-Host "Done. Restart Cursor / your agent, then type / to search routr-* skills." -ForegroundColor Cyan
