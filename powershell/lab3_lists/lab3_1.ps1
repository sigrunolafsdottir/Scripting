[int]$Number1 = Read-Host -Prompt 'Skriv in ett tal '
[int]$Number2 = Read-Host -Prompt 'Skriv in ett ytterligare tal '

$Number1..$Number2 | foreach { "$_" }
" "

$computers = $Number1..$Number2 | foreach { "$_" }
$computers

