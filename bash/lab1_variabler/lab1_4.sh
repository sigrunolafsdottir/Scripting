#!/usr/bin/env bash 
echo -n "ENTER name: "
read name
echo -n "ENTER age: "
read age

#kollar att vi skrev in en siffra för age
if [[ ! $age =~ ^[0-9]+$ ]] ; then
    echo "No good"
    exit
fi
(( age = age + 5 ))
echo "Hej ${name}, om 5 år är du ${age} år gammal."

read hej