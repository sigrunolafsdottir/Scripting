#!/bin/bash
echo  "Vilken kategori tillhör du, vuxen, student eller pensionär? " 
read category


#-lt står för lesser than (-gt står för greater than)
if [ $category == "vuxen" ]; then
    echo "Du betalar 30 kr"
else
    if [ $category == "student" -o $category == "pensionär" ]; then
        echo "Du betalar 20 kr"
    else
        echo "Ogiltig inmatning, felaktig kategori"
    fi
fi

read hej