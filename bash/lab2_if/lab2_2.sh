#!/bin/bash
echo  "Hur mycket mjölk finns det? " 
read m

#-lt står för lesser than (-gt står för greater than)
if [ $m -lt 10 ]; then
    echo "Beställ 30 paket"
else
    if [ $m -lt 20 ]; then
        echo "Beställ 10 paket"
    else
        echo "Vi behöver inte beställa mjölk"
    fi
fi

read hej