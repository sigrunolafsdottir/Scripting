[double]$Number = Read-Host -Prompt 'What is your temperature? '
If ($Number -le 37.8) {"You do not have a temperature"}
If ($Number -gt 37.8 -and $Number -le 39.5) {"You are sick"}
If ($Number -gt 39.5) {"Go see a doctor"}
