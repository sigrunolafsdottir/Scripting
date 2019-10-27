#!/bin/bash
echo  "Mata in din ålder:  " 
read age

#kollar att vi skrev in en siffra för age
if [[ ! $age =~ ^[0-9]+$ ]] ; then
    echo "Ogiltig inmatning"
    exit
fi

#vanliga paranteser för att testa matematiska uttryck
if (( $age < 18 )); then
    echo "Du är inte myndig"
else
    if (( $age < 65 )); then
        echo "Du är vuxen men ännu inte pensionär"
    else
        echo "Du är pensionär"
    fi
fi

read hej