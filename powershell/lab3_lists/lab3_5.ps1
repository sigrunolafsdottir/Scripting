$Sum = 0
$data = @()
do {
    [int]$Number1 = Read-Host -Prompt 'Skriv in ett tal '
    $data += $Number1
    $Sum = 0
    If ($data.count -le 3) {
        $data | ForEach-Object {$Sum += $_}
        $Sum
    }
    Else {
        $ThreeFromLastIndex = $data.count-3
        $lastIndex = $data.count

        #alternativ for-loop
        #for ($i=$ThreeFromLastIndex; $i -lt $lastIndex; $i++) {
        #    $Sum += $data[$i]
        #}
        
        $data[$ThreeFromLastIndex..$lastIndex] | ForEach-Object {$Sum += $_}
        
        $Sum
    }
    
    
}While ($Number1 -ne 0)