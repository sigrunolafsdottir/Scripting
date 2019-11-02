$Sum = 0
$data = @()
do {
    [int]$Number1 = Read-Host -Prompt 'Skriv in ett tal '
    $data += $Number1
    $data | ForEach-Object {$Sum += $_}
    $Sum
}While ($Number1 -ne 0)