
startstring = "c:\\hej\\test\\hello.txt"

firstSlashIndex = startstring.find("\\")
backwardsIndex = startstring.rfind("\\") + 1
end = len(startstring)

print(f"Första index: {firstSlashIndex} Sista index: {backwardsIndex} ")
print(f"Substring efter sista slashen: {startstring[backwardsIndex:end]}  ")

if "hello" in startstring:
    print("JA")
else:
    print("NEJ")
