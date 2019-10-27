#!/bin/bash
#variant där teperaturerna ges på kommandoraden och läses in till en array

max=0
medel=0
counter=0
sum=0

args=()
for i in "$@"; do
    args+=("$i")
done

echo "De temperaturer som har angivits: ${args[@]}"
echo " "

for i in "${args[@]}";
do    
    if (( i > $max )) ; then
        (( max=i )) 
    fi
    (( counter = counter+1))
    (( sum = sum+i))
done

echo "Högsta temperaturen är $max" 

(( medel = sum/counter ))

#kom ihåg att bash bara hanterar integers!
echo "Antal värden är $counter" 

echo "Medelvärdet är $medel" 





#for i in "${args[@]}";
#do    
#   echo $i
#done



read hej