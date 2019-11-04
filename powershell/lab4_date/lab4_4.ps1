param (
    [Parameter(Mandatory=$true)][int]$rows,
    [Parameter(Mandatory=$true)][string]$filename
 )

$today = Get-Date
$todayFormatted = $today.tostring("yyyy-MM-dd hh:mm:ss")

for ($i=0; $i -lt $rows; $i++) {
    $todayFormatted >> $filename
}

