try {
    [int]$Age = Read-Host -Prompt 'What is your age? '
    If ($Age -le 18 -or $Age -ge 65) {"Det kostar 20 kr"}
    If ($Age -gt 18 -and $Age -lt 65) {"Det kostar 30 kr "}
}
catch {"Felaktig inmatning"}