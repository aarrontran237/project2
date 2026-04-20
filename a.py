for a in category_options:
    if a == "length" in category_options[0]:
        print("What 2 units would you like to convert from? (eg. millimeters to meters)")
        print(length_category)
        b = input().lower
        for b in length_options:
            if b == "millimeters to meters":
                print("Input for millimeters")
                ab = input()
                millimeters_to_meters = int(ab)/1000
                print(f'{ab} millimeters is equal to {millimeters_to_meters} meters.')
                break
            elif b == "meters to centimeters":
                print("Input for meters")
                ba = input()
                meters_to_centimeters = int(ba) * 100
                print('{} meters is equal to {} centimeters.' .format(ba, meters_to_centimeters))
                break
            elif b == "meters to kilometers":
                print("Input for meters")
                aba = input()
                meters_to_kilometers = int(aba)/1000
                print(f'{aba} meters is equal to {meters_to_kilometers} kilometers.')
                break
    elif a := "time":
        print("What 2 units would you like to convert from? (eg. hours to days)")
        print(time_category)
        b = input().lower
    elif a == "temperature":
        print("What 2 units would you like to convert from? (eg. celsius to fahrenheit)")
        print(temperature_category)
        b = input().lower
    elif a == "weight":
        print("What 2 units would you like to convert from? (eg. grams to ounces)")
        print(weight_category)
        b = input().lower
    else:
        print('Please choose a category')