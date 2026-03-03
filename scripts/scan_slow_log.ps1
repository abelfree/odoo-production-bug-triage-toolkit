param(
    [Parameter(Mandatory = $true)]
    [string]$LogPath,
    [int]$MinDurationMs = 500
)

Get-Content $LogPath |
    Where-Object { $_ -match "duration: ([0-9.]+) ms" } |
    ForEach-Object {
        if ($_ -match "duration: ([0-9.]+) ms") {
            if ([double]$matches[1] -ge $MinDurationMs) {
                $_
            }
        }
    }
