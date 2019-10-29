mail = input("Mata in en mailadress: ")

if "@" in mail and "." in mail:
    lastDotIndex = mail.rfind(".")+1
    lastPart = mail[lastDotIndex:len(mail)]
    if len(lastPart) == 2 or len(lastPart) == 3:
        print("JA")
    else:
        print("NEJ")
else:
    print("NEJ")