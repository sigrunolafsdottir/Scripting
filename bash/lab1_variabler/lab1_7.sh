#!/usr/bin/env bash
#-n gör att vi skriver in svaret på samma rad som frågan
echo -n "Skriv in ett tal: "
read tal1
echo -n "Skriv in ett ytterligare tal: "
read tal2 

((SUM = tal1 + tal2))
#Notera att här får vi heltalsdivision
((MED = (tal1 + tal2)/2))
((DIFF = tal1 - tal2))

echo "Summan av  ${tal1} och  ${tal2} är ${SUM}."
echo "Medel av  ${tal1} och  ${tal2} är ${MED}."
echo "Differensen av  ${tal1} och  ${tal2} är ${DIFF}."

read hej