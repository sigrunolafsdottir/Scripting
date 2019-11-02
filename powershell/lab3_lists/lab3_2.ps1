$goOn = "Y"
While ($goOn -ne "N") {
    [int]$Number1 = Read-Host -Prompt 'Skriv in ett tal '
    [int]$Number2 = Read-Host -Prompt 'Skriv in ett ytterligare tal '
    $Number1+$Number2
    $goOn = Read-Host -Prompt 'Vill du fortsätta Y/N '
}


