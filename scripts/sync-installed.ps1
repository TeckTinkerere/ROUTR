<#
.SYNOPSIS
    Diff repo skills/routr-* against installed skill roots (PowerShell equivalent of sync-installed.sh).

.DESCRIPTION
    Default roots (whichever of these exist):
      ~/.claude/skills  ~/.agents/skills  ~/.cursor/skills  ~/.codex/skills

    For each repo routr-* skill, reports per root:
      MISSING  - not installed at all
      DRIFT    - installed but file contents differ (lists differing files)
      OK       - installed and identical

    Also reports, per root:
      ORPHAN   - an installed routr-* skill with no matching folder in the repo
      LEGACY   - an installed *-playbook / playbook-* skill whose name appears
                 in docs/naming.md's rename map

    -Apply copies the repo skill's contents over the installed folder for
    that skill (only routr-* folders are touched).

    -PruneLegacy MOVES (never deletes) every LEGACY and ORPHAN folder into
    <root>/.routr-legacy-backup-yyyyMMdd/.

.PARAMETER Root
    One or more installed-skill root paths. Repeatable. Overrides the default
    root discovery.

.PARAMETER Apply
    Copy repo skills over installed ones where MISSING or DRIFT.

.PARAMETER PruneLegacy
    Move LEGACY / ORPHAN folders into a dated backup folder under each root.

.EXAMPLE
    scripts/sync-installed.ps1
    scripts/sync-installed.ps1 -Root C:\Users\me\.claude\skills
    scripts/sync-installed.ps1 -Apply -PruneLegacy
#>
[CmdletBinding()]
param(
    [string[]]$Root,
    [switch]$Apply,
    [switch]$PruneLegacy
)

$ErrorActionPreference = 'Stop'

$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

if (-not $Root -or $Root.Count -eq 0) {
    $candidates = @(
        (Join-Path $HOME '.claude/skills'),
        (Join-Path $HOME '.agents/skills'),
        (Join-Path $HOME '.cursor/skills'),
        (Join-Path $HOME '.codex/skills')
    )
    $Root = @($candidates | Where-Object { Test-Path $_ -PathType Container })
}

if (-not $Root -or $Root.Count -eq 0) {
    Write-Host "No installed skill roots found (checked ~/.claude/skills, ~/.agents/skills, ~/.cursor/skills, ~/.codex/skills)."
    Write-Host "Pass -Root PATH to specify one explicitly."
    exit 0
}

# ---- legacy rename-map names, parsed from the "Rename map (v2)" table only ----
$namingMd = Join-Path $RepoRoot 'docs/naming.md'
$legacyNames = New-Object System.Collections.Generic.HashSet[string]
if (Test-Path $namingMd) {
    $lines = Get-Content $namingMd
    $inTable = $false
    foreach ($line in $lines) {
        if ($line -match '^##\s+Rename map') { $inTable = $true; continue }
        if ($inTable -and $line -match '^##\s+') { break }
        if ($inTable -and $line -match '^\|\s*`([a-z0-9._-]+)`') {
            [void]$legacyNames.Add($matches[1])
        }
    }
}

function Test-LegacyName([string]$name) {
    if ($legacyNames.Contains($name)) { return $true }
    if ($name -like '*-playbook') { return $true }
    if ($name -like 'playbook-*') { return $true }
    return $false
}

# ---- repo routr-* skill folders ----
$repoSkillsDir = Join-Path $RepoRoot 'skills'
$repoSkills = @(Get-ChildItem -Path $repoSkillsDir -Directory -Filter 'routr-*' | Select-Object -ExpandProperty Name)

function Get-FileHashMap([string]$dir) {
    $map = @{}
    if (-not (Test-Path $dir)) { return $map }
    Get-ChildItem -Path $dir -Recurse -File | ForEach-Object {
        $rel = $_.FullName.Substring($dir.Length).TrimStart('\', '/')
        $map[$rel] = (Get-FileHash -Path $_.FullName -Algorithm SHA256).Hash
    }
    return $map
}

$missingOrDrift = $false
$dateStamp = Get-Date -Format 'yyyyMMdd'

foreach ($root in $Root) {
    Write-Host ('=' * 64)
    Write-Host "Root: $root"
    Write-Host ('=' * 64)

    if (-not (Test-Path $root -PathType Container)) {
        Write-Host "  (root does not exist, skipping)"
        continue
    }

    foreach ($skill in $repoSkills) {
        $src = Join-Path $repoSkillsDir $skill
        $dst = Join-Path $root $skill

        if (-not (Test-Path $dst -PathType Container)) {
            Write-Host "MISSING  $skill"
            $missingOrDrift = $true
            if ($Apply) {
                Copy-Item -Path $src -Destination $dst -Recurse -Force
                Write-Host "         -> copied (apply)"
            }
            continue
        }

        $srcMap = Get-FileHashMap $src
        $dstMap = Get-FileHashMap $dst
        $allKeys = New-Object System.Collections.Generic.HashSet[string]
        $srcMap.Keys | ForEach-Object { [void]$allKeys.Add($_) }
        $dstMap.Keys | ForEach-Object { [void]$allKeys.Add($_) }

        $diffFiles = @()
        foreach ($key in $allKeys) {
            $inSrc = $srcMap.ContainsKey($key)
            $inDst = $dstMap.ContainsKey($key)
            if ($inSrc -and $inDst) {
                if ($srcMap[$key] -ne $dstMap[$key]) { $diffFiles += "differ: $key" }
            } elseif ($inSrc -and -not $inDst) {
                $diffFiles += "(repo-only) $key"
            } else {
                $diffFiles += "(installed-only) $key"
            }
        }

        if ($diffFiles.Count -gt 0) {
            Write-Host "DRIFT    $skill"
            $diffFiles | ForEach-Object { Write-Host "         $_" }
            $missingOrDrift = $true
            if ($Apply) {
                Remove-Item -Path $dst -Recurse -Force
                Copy-Item -Path $src -Destination $dst -Recurse -Force
                Write-Host "         -> replaced with repo version (apply)"
            }
        } else {
            Write-Host "OK       $skill"
        }
    }

    # ORPHAN: installed routr-* not in repo
    $orphans = @()
    if (Test-Path $root) {
        Get-ChildItem -Path $root -Directory -Filter 'routr-*' -ErrorAction SilentlyContinue | ForEach-Object {
            if ($repoSkills -notcontains $_.Name) {
                Write-Host "ORPHAN   $($_.Name) (installed, no matching repo skill)"
                $orphans += $_.Name
            }
        }
    }

    # LEGACY: *-playbook / playbook-* stubs named in the rename map
    $legacies = @()
    Get-ChildItem -Path $root -Directory -ErrorAction SilentlyContinue | ForEach-Object {
        if ($_.Name -notlike 'routr-*' -and (Test-LegacyName $_.Name)) {
            Write-Host "LEGACY   $($_.Name) (deprecated per docs/naming.md rename map)"
            $legacies += $_.Name
        }
    }

    if ($PruneLegacy -and (($orphans.Count -gt 0) -or ($legacies.Count -gt 0))) {
        $backupDir = Join-Path $root ".routr-legacy-backup-$dateStamp"
        New-Item -ItemType Directory -Force -Path $backupDir | Out-Null
        foreach ($name in ($orphans + $legacies)) {
            $p = Join-Path $root $name
            if (Test-Path $p) {
                Move-Item -Path $p -Destination $backupDir -Force
                Write-Host "         -> moved $name to $backupDir/ (prune-legacy)"
            }
        }
    }

    Write-Host ""
}

Write-Host ('=' * 64)
if ($Apply) {
    Write-Host "Applied. Re-run without -Apply to confirm clean diff."
} elseif ($missingOrDrift) {
    Write-Host "Drift detected (MISSING/DRIFT above). Re-run with -Apply to sync."
} else {
    Write-Host "All installed routr-* skills match the repo."
}

exit 0
