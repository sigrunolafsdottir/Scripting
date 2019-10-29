countryInput = input("ViLket land bor du i? ")
if countryInput == 'Sverige' or countryInput == 'Norge' or countryInput == 'Danmark':
    print("Du bor i Skandinavien")
else:
    print("Du bor inte i Skandinavien")

countryInput = input("ViLket land bor du i? ")
if countryInput in ['Sverige', 'Norge', 'Danmark']:
    print("Du bor i Skandinavien")
else:
    print("Du bor inte i Skandinavien")