$Max = 0
$data = @()
$Sum = 0

[int]$Amount = Read-Host -Prompt 'Hur många måtningar ska registreras '

for ($i=0; $i -lt $Amount; $i++) {
    [double]$Number1 = Read-Host -Prompt 'Skriv in ett tal '
    $data += $Number1
    $Sum += $Number1
    if ($Number1 -gt $Max){ $Max = $Number1 }
}

$Mean = $Sum / $data.count

"Vår array $data"
"Summan är $Sum"
"Maxvärdet är $Max"
"Medelvärdet är $Mean"
