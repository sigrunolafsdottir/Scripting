$Country = Read-Host -Prompt 'Var kommer du ifrån? '

If ($Country -eq "Sverige" -or $Country -eq "Norge" -or $Country -eq "Danmark") 
    {"Du kommer ifrån Skandinavien"}
If ($Country -ne "Sverige" -and $Country -ne "Norge" -and $Country -ne "Danmark") 
    {"Du kommer inte från Skandinavien"}
