#!/bin/bash
echo -n "Ange ett tal "
read tal

#med en lokal variabel kan jag lätt ändra om jag vill jämföra mot annat tal
((JMF = 10))

#-lt står för lesser than (-gt står för greater than)
if [ $tal -lt $JMF ]; then
    echo "Talet är mindre än ${JMF}"
else
    echo "Talet är större än eller lika med ${JMF}"
fi

read hej