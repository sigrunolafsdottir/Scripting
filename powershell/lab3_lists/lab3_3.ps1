$Sum = 0
do {
    [int]$Number1 = Read-Host -Prompt 'Skriv in ett tal '
    $Sum += $Number1
    $Sum 
}While ($True)