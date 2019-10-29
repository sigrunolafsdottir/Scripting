l = []
 
cont = 1 
while(cont == 1):
    num = int(input("Mata in ett tal: "))
    print(f"Du matade in {num}")
    if num != 0:
        l.insert(0,num)
        amountOfNumbers = len(l)
        if amountOfNumbers > 3:
            amountOfNumbers = 3

        #beräkna medelvärdet av 3 senaste
        summa = 0
        index = 0
            
        for i in l : 
            if index < 3:
                summa += i
                index += 1

        print("Medelvardet av de tre senaste talen (om så många angivits) är: ", summa/amountOfNumbers)
    else:
        print("Programmet avslutas ")
        cont = 0