#!/bin/bash
echo  "Vilket land är du ifrån? " 
read country

#-o står för or
#både = och == verkar funka
if [ $country = "Sverige" -o $country = "Norge" -o $country = "Danmank" ]; then
    echo "Du är ifrån Skandinavien"
else
    echo "Du är inte från Skandinavien."
fi

read hej