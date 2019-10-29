l = []

cont = 1 
while(cont == 1):
    num = int(input("Mata in ett tal: "))
    print(f"Du matade in {num}")
    if num != 0:
        l.append(num)
        print("Summan av alla tal är", sum(l))
    else:
        print("Programmet avslutas ")
        cont = 0
