[int]$Number = Read-Host -Prompt 'Hur mycket mjolk finns kvar'
If ($Number -le 10) {"Koep 30 paket"}
If ($Number -gt 10 -and $Number -le 20) {"Vi behover kopa 10 paket mjolk"}
If ($Number -gt 20) {"Vi behover inte kopa mjolk"}

