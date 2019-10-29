userInput = input("Är du studerande, vuxen eller pensionär?")
if userInput in ['studerande', 'vuxen', 'pensionär']:
    if userInput ==  'studerande' or userInput ==  'pensionär':
        print("Det kostar 20 kr")
    elif userInput ==  'vuxen':
        print("Det kostar 30 kr")

if userInput not in ['studerande', 'vuxen', 'pensionär']: 
    print("Inte en giltig inmatning")