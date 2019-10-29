number = float(input("Vad är tempen?"))
if number < 37.8:
        print("Du har inte feber")
elif number >= 37.8 and number < 39.5:
    print("Du har feber")
else:
    print("Uppsök läkare")