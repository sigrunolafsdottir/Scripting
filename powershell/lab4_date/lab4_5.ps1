param (
    [Parameter(Mandatory=$true)][string]$srcFilePath,
    [Parameter(Mandatory=$true)][string]$destPath
 )

$today = Get-Date
$todayFormatted = $today.tostring("yyyyMMddhhmmss")

$srcFile = Split-Path $srcFilePath -Leaf
$srcFile
$destPathFile = Join-Path $destPath $srcFile
$destPathFile

if([System.IO.File]::Exists($destPathFile)){
    "File does exist, append the timestamp"
}
elseif ([System.IO.File]::Exists($destPath)){
    "Dir does exist, just do a copy"
}
else{
    "Create dir, copy path"
}

