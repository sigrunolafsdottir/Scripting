[int]$Number = Read-Host -Prompt 'Ange ett nummer'
$Comparator = 10
If ($Number -gt $Comparator) {"Bigger than $Comparator"}
If ($Number -le $Comparator) {"Less than or equal to $Comparator"}
