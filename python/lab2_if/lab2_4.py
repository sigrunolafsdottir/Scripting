try:
    number = int(input("Hur gammal är du?"))
    if number < 18:
        print("Du är inte myndig")
    elif number >= 18 and number < 65:
        print("Du är myndig men inte pensionär")
    else:
        print("Du är persionär")
except ValueError:   
    print("Inte ett giltigt nummer")