#!/usr/bin/env bash 
echo  "Hej, vad heter du?" 
read name 
echo "Kul att träffas ${name}" 

#notera skillnaden med enkelfnuttar
#variabeln byts inte ut, strängen skrivs bokstavligt
echo 'Kul att träffas ${name}'

#för att fönstret inte ska stängas
#gör ingenting
read hej