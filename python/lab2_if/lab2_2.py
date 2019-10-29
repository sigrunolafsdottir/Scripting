number = int(input("Hur mycket mjölk finns kvar?"))
if number < 10:
        print("Beställ 30 paket")
elif number >= 10 and number < 20:
    print("Beställ 10 paket")
else:
    print("Vi behöver inte beställa mjölk")