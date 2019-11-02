$input =  "c:\hej\test\hello.txt"

#a
$input.LastIndexOf('\') + 1

#b
$lastIndexSlash = $input.LastIndexOf('\') + 1
$input.Substring($lastIndexSlash)

#c
if ($input.Contains("hej")){ "JA" }