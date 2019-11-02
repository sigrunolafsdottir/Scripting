$Max = 0
$data = @()

for ($i=0; $i -lt 4; $i++) {
    [int]$Number1 = Read-Host -Prompt 'Skriv in ett tal '
    $data += $Number
    if ($Number1 -gt $Max){ $Max = $Number1 }
}

"Maxvärdet är $Max"

$max2 = ($data | measure-object -maximum).maximum
"Maxvärdet (alternativt sätt att få fram) är $max2"




