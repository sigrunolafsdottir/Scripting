
import statistics

temp = []

index = 0
antal = int(input("Hur många mätningar? "))

while(index < antal):
    userInput = float(input("Ange ett tal: "))
    temp.append(userInput)
    index = index + 1

for i in temp:
    print(i)

print(f"Största värdet är: {max(temp)}")
print(f"Största värdet är: {statistics.mean(temp)}")