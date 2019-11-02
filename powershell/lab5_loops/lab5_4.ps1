$mail = Read-Host -Prompt 'Skriv in din mailadress '
$lastIndexDot = $mail.LastIndexOf(".")
$length = $mail.Length
$lastPartLength = $length - $lastIndexDot -1
$error = 0

#kolla kanelbulle
if (-not $mail.Contains("@")){ $error += 1 }

#kolla punkt
if (-not $mail.Contains(".")){ $error += 1 }

#kolla sista ledet har rätt längd
if ($length -gt 5 -and $lastPartLength -eq 2 -or $lastPartLength -eq 3 ){}
else { $error += 1 }


if ($error -eq 0){"Korrekt mailadress"}
else {"Felaktig mailadress"}
