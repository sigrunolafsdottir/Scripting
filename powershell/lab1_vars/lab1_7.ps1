[int]$Number1 = Read-Host -Prompt 'Type a number '
[int]$Number2 = Read-Host -Prompt 'Type another number '
$Sum = $Number1 + $Number2
$Mean = $Sum / 2
$Diff = $Number1 - $Number2
Write-Host "The sum of $Number1 and $Number2 is $Sum" 
Write-Host "The mean of $Number1 and $Number2 is $Mean" 
Write-Host "The sum of $Number1 and $Number2 is $Diff" 