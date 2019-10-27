#!/bin/bash
echo  "Mata in din ålder:  " 
read age

#kollar att vi skrev in en siffra för age
if [[ ! $age =~ ^[0-9]+$ ]] ; then
    echo "Ogiltig inmatning"
    exit
fi

#-lt står för lesser than (-gt står för greater than)
if [ $age -lt 18 ]; then
    echo "Du är inte myndig"
else
    if [ $age -lt 65 ]; then
        echo "Du är vuxen men ännu inte pensionär"
    else
        echo "Du är pensionär"
    fi
fi

read hej