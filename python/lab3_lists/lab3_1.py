import statistics

tal1 = int(input("Mata in tal 1. "))
tal2 = int(input("Mata in tal 2. "))
tal3 = int(input("Mata in tal 3. "))
tal4 = int(input("Mata in tal 4. "))

arr = [tal1, tal2, tal3, tal4]

storst = -1000
# # ett sätt att lösa detta är for-loop
for i in arr:
    if i > storst:
        storst = i

# max(arr) är ett annat sätt att lösa detta
print(f"Största talet är: {storst} {max(arr)}")
