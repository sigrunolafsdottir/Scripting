#!/bin/bash

echo "Mata in en mail-adress"
read email

if [[ $email != *"@"* ]]; then
  echo "Kanelbullen saknas"
fi

lastpart=$email | cut -d "@" -f 1
echo "lastpart $lastpart"


regex="^*.[a-z][a-z]([a-z])*)/$"
if [[ $email =~ $regex ]] ; then
    echo "OK"
else
    echo "not OK"
fi


# proffsigare lösning, snodd från nätet

regexInternet="^[a-z0-9!#\$%&'*+/=?^_\`{|}~-]+(\.[a-z0-9!#$%&'*+/=?^_\`{|}~-]+)*@([a-z0-9]([a-z0-9-]*[a-z0-9])?\.)+[a-z0-9]([a-z0-9-]*[a-z0-9])?\$"

if [[ $email =~ $regexInternet ]] ; then
    echo "OK"
else
    echo "not OK"
fi

read hej