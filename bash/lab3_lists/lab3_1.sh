#!/bin/bash

max=0

echo  "Mata in första talet:  " 
read tal1
echo  "Mata in andra talet:  " 
read tal2
echo  "Mata in tredje talet:  " 
read tal3
echo  "Mata in fjärde talet:  " 
read tal4

arr=($tal1 $tal2 $tal3 $tal4) 

for i in "${arr[@]}";
do    
    if (( i > $max )) ; then
        (( max=i )) 
    fi
done

echo "Största talet är $max" 

read hej