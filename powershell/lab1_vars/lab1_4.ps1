$User = Read-Host -Prompt 'Vad heter du?'
[int]$Age = Read-Host -Prompt 'Hur gammal aer du?'
$Age5 = $Age+5
Write-Host "Kul att ses $User, om 5 aar aer du $Age5 aar." 