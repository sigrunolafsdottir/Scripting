[int]$Age = Read-Host -Prompt 'What is your age? '
If ($Age -le 18) {"Du är inte myndig"}
If ($Age -gt 18 -and $Number -lt 65) {"Du är myndig"}
If ($Age -ge 65) {"Du är en pensionaer"}
