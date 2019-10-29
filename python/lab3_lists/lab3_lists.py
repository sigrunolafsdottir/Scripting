import statistics

# tal1 = int(input("Mata in tal 1. "))
# tal2 = int(input("Mata in tal 2. "))
# tal3 = int(input("Mata in tal 3. "))
# tal4 = int(input("Mata in tal 4. "))

# arr = [tal1, tal2, tal3, tal4]

# storst = -1000
# # ett sätt att lösa detta är for-loop
# for i in arr:
#     if i > storst:
#         storst = i

# # max(arr) är ett annat sätt att lösa detta
# print(f"Största talet är: {storst} {max(arr)}")


# temp = []

# index = 0
# antal = int(input("Hur många mätningar? "))

# while(index < antal):
#     userInput = float(input("Ange ett tal: "))
#     temp.append(userInput)
#     index = index + 1

# for i in temp:
#     print(i)

# print(f"Största värdet är: {max(temp)}")
# print(f"Största värdet är: {statistics.mean(temp)}")


# startstring = "c:\hej\test\hello.txt"

# firstSlashIndex = startstring.find("\\")
# backwardsIndex = startstring.rfind("\\") + 1
# end = len(startstring)

# print(f"Första index: {firstSlashIndex} Sista index: {backwardsIndex} ")
# print(f"Substring efter sista slashen: {startstring[backwardsIndex:end]}  ")

# if "hello" in startstring:
#     print("JA")
# else:
#     print("NEJ")


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





