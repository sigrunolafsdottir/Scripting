cont = True

while(cont is True):
    num1 = int(input("Mata in ett tal: "))
    num2 = int(input("Mata in ytterligare ett tal: "))
    print(num1 + num2)
    userCont = input("Vill du fortsätta, J/N: ")
    if userCont == 'N' or userCont == 'n':
        cont = False