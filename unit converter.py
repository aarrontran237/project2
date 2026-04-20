# Checklist:
#     -add in equations for converting
#     -add in subcategories done
#     -ability to switch between 2 units

category_options = ['length', 'time', 'temperature', 'weight']
length_options = ['meters to kilometers', 'meters to centimeters', 'meters to millimeters', 'meters to micrometers',
                  'meters to nanometers', 'meters to miles', 'meters to yards', 'meters to feet', 'meters to inches',
                  'meters to light years', 'kilometers to meters', 'kilometers to centimeters', 'kilometers to millimeters',
                  'kilometers to micrometers', 'kilometers to nanometers', 'kilometers to miles', 'kilometers to yards',
                  'kilometers to feet', 'kilometers to inches', 'kilometers to light years', 'centimeters to meters',
                  'centimeters to kilometers', 'centimeters to millimeters', 'centimeters to micrometers',
                  'centimeters to nanometers', 'centimeters to miles', 'centimeters to yards', 'centimeters to feet',
                  'centimeters to inches', 'centimeters to light years', 'millimeters to meters', 'millimeters to centimeters',
                  'millimeters to micrometers', 'millimeters to nanometers', 'millimeters to miles', 'millimeters to yards',
                  'millimeters to feet', 'millimeters to inches', 'millimeters to light years', 'micrometers to meters',
                  'micrometers to kilometers', 'micrometers to centimeters', 'micrometers to millimeters',
                  'micrometers to nanometers', 'micrometers to miles', 'micrometers to yard', 'micrometers to feet',
                  'micrometers to inches', 'micrometers to light years', 'nanometers to meters', 'nanometers to kilometers',
                  'nanometers to centimeters', 'nanometers to millimeters', 'nanometers to micrometers',
                  'nanometers to miles', 'nanometers to yards', 'nanometers to feet', 'nanometers to inches',
                  'nanometers to light years', 'miles to meters', 'miles to kilometers', 'miles to centimeters',
                  'miles to millimeters', 'miles to micrometers', 'miles to nanometers', 'miles to yards', 'miles to feet',
                  'miles to inches', 'miles to light years', 'yards to meters', 'yards to kilometers', 'yards to centimeters',
                  'yards to millimeters', 'yards to micrometers', 'yards to nanometers', 'yards to miles', 'yards to feet',
                  'yards to inches', 'yards to light years', 'inches to meters', 'inches to kilometers',
                  'inches to centimeters', 'inches to millimeters', 'inches to micrometers', 'inches to nanometers',
                  'inches to miles', 'inches to yards', 'inches to feet', 'inches to light years', 'feet to meters',
                  'feet to kilometers', 'feet to centimeters', 'feet to millimeters', 'feet to micrometers',
                  'feet to nanometers', 'feet to miles', 'feet to yards', 'feet to inches', 'feet to light years',
                  'light years to meters', 'light years to kilometers', 'light years to centimeters',
                  'light years to millimeters', 'light years to micrometers', 'light years to nanometers',
                  'light years to miles', 'light years to yards', 'light years to feet', 'light years to inches']
length_category = ['meters, kilometers, centimeters, millimeters, micrometers, nanometers, '
                   'miles, yards, feet, inches, '
                   'light years']

time_category = ['seconds, milliseconds, microseconds, nanoseconds, picoseconds, minutes, hours, days, weeks, months, years']
time_options = ['seconds to milliseconds', 'seconds to microsecond', 'seconds to nanoseconds', 'seconds to picoseconds',
                'seconds to minutes', 'seconds to hours', 'seconds to days', 'seconds to weeks', 'seconds to months',
                'seconds to years', 'milliseconds to seconds', 'milliseconds to microseconds', 'milliseconds to nanoseconds',
                'milliseconds to picoseconds', 'milliseconds to minutes', 'milliseconds to hours', 'milliseconds to days',
                'milliseconds to weeks', 'milliseconds to months', 'milliseconds to years', 'microseconds to seconds',
                'microseconds to milliseconds', 'microseconds to nanoseconds', 'microseconds to picoseconds',
                'microseconds to minutes', 'microseconds to hours', 'microseconds to days', 'microseconds to weeks',
                'microseconds to months', 'microseconds to years', 'nanoseconds to seconds', 'nanoseconds to milliseconds',
                'nanoseconds to microseconds', 'nanoseconds to picoseconds', 'nanoseconds to minutes', 'nanoseconds to hours',
                'nanoseconds to days', 'nanoseconds to weeks', 'nanoseconds to months', 'nanoseconds to years',
                'picoseconds to seconds', 'picoseconds to milliseconds', 'picoseconds to microseconds',
                'picoseconds to nanoseconds', 'picoseconds to minutes', 'picoseconds to hours', 'picoseconds to days',
                'picoseconds to weeks', 'picoseconds to months', 'picoseconds to years', 'minutes to seconds',
                'minutes to milliseconds', 'minutes to microseconds', 'minutes to nanoseconds', 'minutes to picoseconds',
                'minutes to hours', 'minutes to days', 'minutes to weeks', 'minutes to months', 'minutes to years',
                'hours to seconds', 'hours to milliseconds', 'hours to microseconds', 'hours to nanoseconds',
                'hours to picoseconds', 'hours to minutes', 'hours to days', 'hours to weeks', 'hours to months',
                'hours to years', 'days to seconds', 'days to milliseconds', 'days to microseconds', 'days to nanoseconds',
                'days to picoseconds', 'days to minutes', 'days to hours', 'days to weeks', 'days to months',
                'days to years', 'weeks to seconds', 'weeks to milliseconds', 'weeks to microseconds', 'weeks to nanoseconds',
                'weeks to picoseconds', 'weeks to minutes', 'weeks to hours', 'weeks to days', 'weeks to months',
                'weeks to years', 'months to seconds', 'months to milliseconds', 'months to microseconds',
                'months to nanoseconds', 'months to picoseconds', 'months to minutes', 'months to hours', 'months to days',
                'months to weeks', 'months to years', 'years to seconds', 'years to seconds', 'years to milliseconds',
                'years to microseconds', 'years to nanoseconds', 'years to picoseconds', 'years to minutes',
                'years to hours', 'years to days', 'years to weeks', 'years to months']

temperature_category = ['celsius, fahrenheit, kelvin']
temperature_options = ['celsius to fahrenheit', 'celsius to kelvin', 'fahrenheit to celsius', 'fahrenheit to kelvin',
                       'kelvin to celsius', 'kelvin to fahrenheit']

weight_category = ['milligrams, grams, kilograms, carats, ounces, pounds, tons, long tons, tonnes']
weight_options = ['milligrams to grams', 'milligrams to kilograms', 'milligrams to carats', 'milligrams to ounces',
                   'milligrams to pounds', 'milligrams to tons', 'milligrams to long tons', 'milligrams to tonnes',
                   'grams to milligrams', 'grams to kilograms', 'grams to carats', 'grams to ounces', 'grams to pounds',
                   'grams to tons', 'grams to long tons', 'grams to tonnes', 'kilograms to milligrams', 'kilograms to grams',
                   'kilograms to carats', 'kilograms to ounces', 'kilograms to pounds', 'kilograms to tons',
                   'kilograms to long tons', 'kilograms to tonnes', 'carats to milligrams', 'carats to grams',
                   'carats to kilograms', 'carats to ounces', 'carats to pounds', 'carats to tons', 'carats to long tons',
                   'carats to tonnes', 'ounces to milligrams', 'ounces to grams', 'ounces to kilograms', 'ounces to carats',
                   'ounces to pounds', 'ounces to tons', 'ounces to long tons', 'ounces to tonnes', 'pounds to milligrams',
                   'pounds to grams', 'pounds to kilograms', 'pounds to carats', 'pounds to ounces', 'pounds to tons',
                   'pounds to long tons', 'pounds to tonnes', 'tons to milligrams', 'tons to grams', 'tons to kilograms',
                   'tons to carats', 'tons to ounces', 'tons to pounds', 'tons to long tons', 'tons to tonnes',
                   'long tons to milligrams', 'long tons to grams', 'long tons to kilograms', 'long tons to carats',
                   'long tons to ounces', 'long tons to pounds', 'long tons to tons', 'long tons to tonnes',
                   'tonnes to milligrams', 'tonnes to grams', 'tonnes to kilograms', 'tonnes to carats', 'tonnes to ounces',
                   'tonnes to pounds', 'tonnes to tons', 'tonnes to long tons']

def pick_category():
    print("What category would you like to convert from? Choose a number. (1. length/2. time/3. temperature/4. weight)")


while True:
    pick_category()
    user_input = input()
    
    if user_input == '1':
        print('What 2 units would you like to covert from?')
        print(length_category)
        user_input = input()
        if user_input == 'meters to kilometers':
            print('Input for meters')
            user_input = input()
            m_to_km = int(user_input)/1000
            print(f'{user_input} meters is equal to {m_to_km} kilometers.')
            break
        elif user_input == 'meters to centimeters':
            print('Input for meters')
            user_input = input()
            m_to_cm = int(user_input)*100
            print(f'{user_input} meters is equal to {m_to_cm} centimeters.')
            break
        elif user_input == 'meters to millimeters':
            print('Input for meters')
            user_input = input()
            m_to_mm = int(user_input)*1000
            print(f'{user_input} meters is equal to {m_to_mm} millimeters.')
            break
        elif user_input == 'meters to micrometers':
            print('Input for meters')
            user_input = input()
            m_to_µm = int(user_input)*1000000
            print(f'{user_input} meters is equal to {m_to_µm} micrometers.')
            break
        elif user_input == 'meters to nanometers':
            print('Input for meters')
            user_input = input()
            m_to_nm = int(user_input)*1000000000
            print(f'{user_input} meters is equal to {m_to_nm} nanometers.')
            break
        elif user_input == 'meters to miles':
            print('Input for meters')
            user_input = input()
            m_to_mi = int(user_input)/1609.344
            print(f'{user_input} meters is equal to {m_to_mi} miles.')
            break
        elif user_input == 'meters to yards':
            print('Input for meters')
            user_input = input()
            m_to_yd = int(user_input)*1.0936133
            print(f'{user_input} meters is equal to {m_to_yd} yards.')
            break
        elif user_input == 'meters to feet':
            print('Input for meters')
            user_input = input()
            m_to_ft = int(user_input)*3.2808399
            print(f'{user_input} meters is equal to {m_to_ft} feet.')
            break
        elif user_input == 'meters to inches':
            print('Input for meters')
            user_input = input()
            m_to_in = int(user_input)*39.3700787
            print(f'{user_input} meters is equal to {m_to_in} inches.')
            break
        elif user_input == 'meters to light years':
            print('Input for meters')
            user_input = input()
            m_to_ly = int(user_input)/9460700000000000.0
            print(f'{user_input} meters is equal to {m_to_ly} light years.')
            break
        elif user_input == 'kilometers to meters':
            print('Input for kilometers')
            user_input = input()
            km_to_m = int(user_input)*1000
            print(f'{user_input} kilometers is equal to {km_to_m} meters.')
            break
        elif user_input == 'kilometers to centimeters':
            print('Input for kilometers')
            user_input = input()
            km_to_cm = int(user_input)*100000
            print(f'{user_input} kilometers is equal to {km_to_cm} centimeters.')
            break
        elif user_input == 'kilometers to millimeters':
            print('Input for kilometers')
            user_input = input()
            km_to_mm = int(user_input)*1000000
            print(f'{user_input} kilometers is equal to {km_to_mm} millimeters.')
            break
        elif user_input == 'kilometers to micrometers':
            print('Input for kilometers')
            user_input = input()
            km_to_µm = int(user_input)*1000000000
            print(f'{user_input} kilometers is equal to {km_to_µm} micrometers.')
            break
        elif user_input == 'kilometers to nanometers':
            print('Input for kilometers')
            user_input = input()
            km_to_nm = int(user_input)*1000000000000
            print(f'{user_input} kilometers is equal to {km_to_nm} nanometers.')
            break
        else:
            print('Please choose 2 units')
        
    elif user_input == '2':
        print()
        print(time_category)
        break
    elif user_input == '3':
        print(temperature_category)
        break
    elif user_input == '4':
        print(weight_category)
        break
    else:
        print('Please choose a category')