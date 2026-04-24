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
            print('Input for meters (whole numbers only)')
            user_input = input()
            m_to_km = int(user_input)/1000
            print(f'{user_input} meters is equal to {m_to_km} kilometers.')
            break
        elif user_input == 'meters to centimeters':
            print('Input for meters (whole numbers only)')
            user_input = input()
            m_to_cm = int(user_input)*100
            print(f'{user_input} meters is equal to {m_to_cm} centimeters.')
            break
        elif user_input == 'meters to millimeters':
            print('Input for meters (whole numbers only)')
            user_input = input()
            m_to_mm = int(user_input)*1000
            print(f'{user_input} meters is equal to {m_to_mm} millimeters.')
            break
        elif user_input == 'meters to micrometers':
            print('Input for meters (whole numbers only)')
            user_input = input()
            m_to_µm = int(user_input)*1000000
            print(f'{user_input} meters is equal to {m_to_µm} micrometers.')
            break
        elif user_input == 'meters to nanometers':
            print('Input for meters (whole numbers only)')
            user_input = input()
            m_to_nm = int(user_input)*1000000000
            print(f'{user_input} meters is equal to {m_to_nm} nanometers.')
            break
        elif user_input == 'meters to miles':
            print('Input for meters (whole numbers only)')
            user_input = input()
            m_to_mi = int(user_input)/1609.344
            print(f'{user_input} meters is equal to {m_to_mi} miles.')
            break
        elif user_input == 'meters to yards':
            print('Input for meters (whole numbers only)')
            user_input = input()
            m_to_yd = int(user_input)*1.0936133
            print(f'{user_input} meters is equal to {m_to_yd} yards.')
            break
        elif user_input == 'meters to feet':
            print('Input for meters (whole numbers only)')
            user_input = input()
            m_to_ft = int(user_input)*3.2808399
            print(f'{user_input} meters is equal to {m_to_ft} feet.')
            break
        elif user_input == 'meters to inches':
            print('Input for meters (whole numbers only)')
            user_input = input()
            m_to_in = int(user_input)*39.3700787
            print(f'{user_input} meters is equal to {m_to_in} inches.')
            break
        elif user_input == 'meters to light years':
            print('Input for meters (whole numbers only)')
            user_input = input()
            m_to_ly = int(user_input)/9460700000000000.0
            print(f'{user_input} meters is equal to {m_to_ly} light years.')
            break
        elif user_input == 'kilometers to meters':
            print('Input for kilometers (whole numbers only)')
            user_input = input()
            km_to_m = int(user_input)*1000
            print(f'{user_input} kilometers is equal to {km_to_m} meters.')
            break
        elif user_input == 'kilometers to centimeters':
            print('Input for kilometers (whole numbers only)')
            user_input = input()
            km_to_cm = int(user_input)*100000
            print(f'{user_input} kilometers is equal to {km_to_cm} centimeters.')
            break
        elif user_input == 'kilometers to millimeters':
            print('Input for kilometers (whole numbers only)')
            user_input = input()
            km_to_mm = int(user_input)*1000000
            print(f'{user_input} kilometers is equal to {km_to_mm} millimeters.')
            break
        elif user_input == 'kilometers to micrometers':
            print('Input for kilometers (whole numbers only)')
            user_input = input()
            km_to_µm = int(user_input)*1000000000
            print(f'{user_input} kilometers is equal to {km_to_µm} micrometers.')
            break
        elif user_input == 'kilometers to nanometers':
            print('Input for kilometers (whole numbers only)')
            user_input = input()
            km_to_nm = int(user_input)*1000000000000
            print(f'{user_input} kilometers is equal to {km_to_nm} nanometers.')
            break
        elif user_input == 'kilometers to miles':
            print('Input for kilometers (whole numbers only)')
            user_input = input()
            km_to_mi = int(user_input)*0.621371
            print(f'{user_input} kilometers is equal to {km_to_mi} miles.')
            break
        elif user_input == 'kilometers to yards':
            print('Input for kilometers (whole numbers only)')
            user_input = input()
            km_to_yd = int(user_input)*1093.6132983377
            print(f'{user_input} kilometers is equal to {km_to_yd} yards.')
            break
        elif user_input == 'kilometers to inches':
            print('Input for kilometers (whole numbers only)')
            user_input = input()
            km_to_in = int(user_input)*39370.1
            print(f'{user_input} kilometers is equal to {km_to_in} inches.')
            break
        elif user_input == 'kilometers to feet':
            print('Input for kilometers (whole numbers only)')
            user_input = input()
            km_to_ft = int(user_input)*3280.8398950131
            print(f'{user_input} kilometers is equal to {km_to_ft} feet.')
            break
        elif user_input == 'kilometers to light years':
            print('Input for kilometers (whole numbers only)')
            user_input = input()
            km_to_ly = int(user_input)*3280.8398950131
            print(f'{user_input} kilometers is equal to {km_to_ly} light years.')
            break
        elif user_input == 'centimeters to meters':
            print('Input for centimeters (whole numbers only)')
            user_input = input()
            cm_to_m = int(user_input)/100
            print(f'{user_input} centimeters is equal to {cm_to_m} meters.')
            break
        elif user_input == 'centimeters to kilometers':
            print('Input for centimeters (whole numbers only)')
            user_input = input()
            cm_to_km = int(user_input)/100000
            print(f'{user_input} centimeters is equal to {cm_to_km} kilometers.')
            break
        elif user_input == 'centimeters to millimeters':
            print('Input for centimeters (whole numbers only)')
            user_input = input()
            cm_to_mm = int(user_input)*10
            print(f'{user_input} centimeters is equal to {cm_to_mm} millimeters.')
            break
        elif user_input == 'centimeters to micrometers':
            print('Input for centimeters (whole numbers only)')
            user_input = input()
            cm_to_mim = int(user_input)/10000000
            print(f'{user_input} centimeters is equal to {cm_to_mim} micrometers.')
            break
        elif user_input == 'centimeters to miles':
            print('Input for centimeters (whole numbers only)')
            user_input = input()
            cm_to_mi = int(user_input)*0.00000621
            print(f'{user_input} centimeters is equal to {cm_to_mi} miles.')
            break
        elif user_input == 'centimeters to yards':
            print('Input for centimeters (whole numbers only)')
            user_input = input()
            cm_to_yd = int(user_input)*91.44
            print(f'{user_input} centimeters is equal to {cm_to_yd} yards.')
            break
        elif user_input == 'centimeters to feet':
            print('Input for centimeters (whole numbers only)')
            user_input = input()
            cm_to_ft = int(user_input)*0.00000621
            print(f'{user_input} centimeters is equal to {cm_to_ft} ft.')
            break
        elif user_input == 'centimeters to inches':
            print('Input for centimeters (whole numbers only)')
            user_input = input()
            cm_to_in = int(user_input)/2.54
            print(f'{user_input} centimeters is equal to {cm_to_in} inches.')
            break
        elif user_input == 'centimeters to light years':
            print('Input for centimeters (whole numbers only)')
            user_input = input()
            cm_to_ly = int(user_input)/0.000000000000000001057000
            print(f'{user_input} centimeters is equal to {cm_to_ly} light years.')
            break
        elif user_input == 'millimeters to meters':
            print('Input for millimeters (whole numbers only)')
            user_input = input()
            mm_to_m = int(user_input)/1000
            print(f'{user_input} millimeters is equal to {mm_to_m} meters.')
            break
        elif user_input == 'millimeters to kilometers':
            print('Input for millimeters (whole numbers only)')
            user_input = input()
            mm_to_km = int(user_input)/1000000
            print(f'{user_input} millimeters is equal to {mm_to_km} kilometers.')
            break
        elif user_input == 'millimeters to centimeters':
            print('Input for millimeters (whole numbers only)')
            user_input = input()
            mm_to_cm = int(user_input)/10
            print(f'{user_input} millimeters is equal to {mm_to_cm} centimeters.')
            break
        elif user_input == 'millimeters to micrometers':
            print('Input for millimeters (whole numbers only)')
            user_input = input()
            mm_to_mim = int(user_input)*1000
            print(f'{user_input} millimeters is equal to {mm_to_mim} micrometers.')
            break
        elif user_input == 'millimeters to nanometers':
            print('Input for millimeters (whole numbers only)')
            user_input = input()
            mm_to_nm = int(user_input)*1000000
            print(f'{user_input} millimeters is equal to {mm_to_nm} nanometers.')
            break
        elif user_input == 'millimeters to miles':
            print('Input for millimeters (whole numbers only)')
            user_input = input()
            mm_to_mi = int(user_input)/1609.344
            print(f'{user_input} millimeters is equal to {mm_to_mi} miles.')
            break
        elif user_input == 'millimeters to yards':
            print('Input for millimeters (whole numbers only)')
            user_input = input()
            mm_to_yd = int(user_input)*0.0010936133
            print(f'{user_input} millimeters is equal to {mm_to_yd} yards.')
            break
        elif user_input == 'millimeters to feet':
            print('Input for millimeters (whole numbers only)')
            user_input = input()
            mm_to_ft = int(user_input)*0.00328084
            print(f'{user_input} millimeters is equal to {mm_to_ft} feet.')
            break
        elif user_input == 'millimeters to inches':
            print('Input for millimeters (whole numbers only)')
            user_input = input()
            mm_to_in = int(user_input)/25.4
            print(f'{user_input} millimeters is equal to {mm_to_in} inches.')
            break
        elif user_input == 'millimeters to light years':
            print('Input for millimeters (whole numbers only)')
            user_input = input()
            mm_to_ly = int(user_input)/9460700000000000000.0
            print(f'{user_input} millimeters is equal to {mm_to_ly} light years.')
            break
        elif user_input == 'micrometers to meters':
            print('Input for micrometers (whole numbers only)')
            user_input = input()
            mim_to_m = int(user_input)*1000000
            print(f'{user_input} micrometers is equal to {mim_to_m} meters.')
            break
        elif user_input == 'micrometers to kilometers':
            print('Input for micrometers (whole numbers only)')
            user_input = input()
            mim_to_km = int(user_input)*1000000000
            print(f'{user_input} micrometers is equal to {mim_to_km} kilometers.')
            break
        elif user_input == 'micrometers to centimeters':
            print('Input for micrometers (whole numbers only)')
            user_input = input()
            mim_to_cm = int(user_input)/10000
            print(f'{user_input} micrometers is equal to {mim_to_cm} centimeters.')
            break
        elif user_input == 'micrometers to millimeters':
            print('Input for micrometers (whole numbers only)')
            user_input = input()
            mim_to_mm = int(user_input)/1000
            print(f'{user_input} micrometers is equal to {mim_to_mm} millimeters.')
            break
        elif user_input == 'micrometers to nanometers':
            print('Input for micrometers (whole numbers only)')
            user_input = input()
            mim_to_nm = int(user_input)*1000
            print(f'{user_input} micrometers is equal to {mim_to_nm} nanometers.')
            break
        elif user_input == 'micrometers to miles':
            print('Input for micrometers (whole numbers only)')
            user_input = input()
            mim_to_mi = int(user_input)/1609300000.0
            print(f'{user_input} micrometers is equal to {mim_to_mi} miles.')
            break
        elif user_input == 'micrometers to yards':
            print('Input for micrometers (whole numbers only)')
            user_input = input()
            mim_to_yd = int(user_input)/914400
            print(f'{user_input} micrometers is equal to {mim_to_yd} yards.')
            break
        elif user_input == 'micrometers to feet':
            print('Input for micrometers (whole numbers only)')
            user_input = input()
            mim_to_ft = int(user_input)/304800
            print(f'{user_input} micrometers is equal to {mim_to_ft} feet.')
            break
        elif user_input == 'micrometers to inches':
            print('Input for micrometers (whole numbers only)')
            user_input = input()
            mim_to_in = int(user_input)/25400
            print(f'{user_input} micrometers is equal to {mim_to_in} inches.')
            break
        elif user_input == 'micrometers to light years':
            print('Input for micrometers (whole numbers only)')
            user_input = input()
            mim_to_ly = int(user_input)/9460700000000000000000.0
            print(f'{user_input} micrometers is equal to {mim_to_ly} light years.')
            break
        elif user_input == 'nanometers to meters':
            print('Input for nanometers (whole numbers only)')
            user_input = input()
            nm_to_m = int(user_input)/1000000000
            print(f'{user_input} nanometers is equal to {nm_to_m} meters.')
            break
        elif user_input == 'nanometers to kilometers':
            print('Input for nanometers (whole numbers only)')
            user_input = input()
            nm_to_km = int(user_input)/1000000000000
            print(f'{user_input} nanometers is equal to {nm_to_km} kilometers.')
            break
        elif user_input == 'nanometers to centimeters':
            print('Input for nanometers (whole numbers only)')
            user_input = input()
            nm_to_cm = int(user_input)/10000000
            print(f'{user_input} nanometers is equal to {nm_to_cm} centimeters.')
            break
        elif user_input == 'nanometers to micrometers':
            print('Input for nanometers (whole numbers only)')
            user_input = input()
            nm_to_mim = int(user_input)/1000
            print(f'{user_input} nanometers is equal to {nm_to_mim} micrometers.')
            break
        elif user_input == 'nanometers to miles':
            print('Input for nanometers (whole numbers only)')
            user_input = input()
            nm_to_mi = int(user_input)/1609300000000
            print(f'{user_input} nanometers is equal to {nm_to_mi} miles.')
            break
        elif user_input == 'nanometers to yards':
            print('Input for nanometers (whole numbers only)')
            user_input = input()
            nm_to_yd = int(user_input)/914400000
            print(f'{user_input} nanometers is equal to {nm_to_yd} yards.')
            break
        elif user_input == 'nanometers to feet':
            print('Input for nanometers (whole numbers only)')
            user_input = input()
            nm_to_ft = int(user_input)/304800000
            print(f'{user_input} nanometers is equal to {nm_to_ft} feet.')
            break
        elif user_input == 'nanometers to inches':
            print('Input for nanometers (whole numbers only)')
            user_input = input()
            nm_to_in = int(user_input)/25400000
            print(f'{user_input} nanometers is equal to {nm_to_in} inches.')
            break
        elif user_input == 'nanometers to light years':
            print('Input for nanometers (whole numbers only)')
            user_input = input()
            nm_to_ly = int(user_input)/9460700000000000000000000.0
            print(f'{user_input} nanometers is equal to {nm_to_ly} light years.')
            break
        elif user_input == 'miles to meters':
            print('Input for miles (whole numbers only)')
            user_input = input()
            mi_to_m = int(user_input)*1609.344
            print(f'{user_input} miles is equal to {mi_to_m} meters.')
            break
        elif user_input == 'miles to kilometers':
            print('Input for miles (whole numbers only)')
            user_input = input()
            mi_to_km = int(user_input)*1.609344
            print(f'{user_input} miles is equal to {mi_to_km} kilometers.')
            break
        elif user_input == 'miles to centimeters':
            print('Input for miles (whole numbers only)')
            user_input = input()
            mi_to_cm = int(user_input)*160934.4
            print(f'{user_input} miles is equal to {mi_to_cm} centimeters.')
            break
        elif user_input == 'miles to millimeters':
            print('Input for miles (whole numbers only)')
            user_input = input()
            mi_to_mm = int(user_input)*1609300
            print(f'{user_input} miles is equal to {mi_to_mm} millimeters.')
            break
        elif user_input == 'miles to micrometers':
            print('Input for miles (whole numbers only)')
            user_input = input()
            mi_to_mim = int(user_input)*1609300000
            print(f'{user_input} miles is equal to {mi_to_mim} micrometers.')
            break
        elif user_input == 'miles to nanometers':
            print('Input for miles (whole numbers only)')
            user_input = input()
            mi_to_nm = int(user_input)*160934400000000
            print(f'{user_input} miles is equal to {mi_to_nm} nanometers.')
            break
        elif user_input == 'miles to yards':
            print('Input for miles (whole numbers only)')
            user_input = input()
            mi_to_yd = int(user_input)*1760
            print(f'{user_input} miles is equal to {mi_to_yd} yards.')
            break
        elif user_input == 'miles to feet':
            print('Input for miles (whole numbers only)')
            user_input = input()
            mi_to_ft = int(user_input)*5280
            print(f'{user_input} miles is equal to {mi_to_ft} feet.')
            break
        elif user_input == 'miles to inches':
            print('Input for miles (whole numbers only)')
            user_input = input()
            mi_to_in = int(user_input)*63360
            print(f'{user_input} miles is equal to {mi_to_in} inches.')
            break
        elif user_input == 'miles to light years':
            print('Input for miles (whole numbers only)')
            user_input = input()
            mi_to_ly = int(user_input)/5878600000000.0
            print(f'{user_input} miles is equal to {mi_to_ly} light years.')
            break
        elif user_input == 'yards to meters':
            print('Input for yards (whole numbers only)')
            user_input = input()
            yd_to_m = int(user_input)/1.0936133
            print(f'{user_input} yards is equal to {yd_to_m} meters.')
            break
        elif user_input == 'yards to kilometers':
            print('Input for yards (whole numbers only)')
            user_input = input()
            yd_to_km = int(user_input)/1093.6133
            print(f'{user_input} yards is equal to {yd_to_km} kilometers.')
            break
        elif user_input == 'yards to centimeters':
            print('Input for yards (whole numbers only)')
            user_input = input()
            yd_to_cm = int(user_input)*91.44
            print(f'{user_input} yards is equal to {yd_to_cm} centimeters.')
            break
        elif user_input == 'yards to millimeters':
            print('Input for yards (whole numbers only)')
            user_input = input()
            yd_to_mm = int(user_input)*914.4
            print(f'{user_input} yards is equal to {yd_to_mm} millimeters.')
            break
        elif user_input == 'yards to micrometers':
            print('Input for yards (whole numbers only)')
            user_input = input()
            yd_to_mim = int(user_input)*914400
            print(f'{user_input} yards is equal to {yd_to_mim} micrometers.')
            break
        elif user_input == 'yards to nanometers':
            print('Input for yards (whole numbers only)')
            user_input = input()
            yd_to_nm = int(user_input)*914400000
            print(f'{user_input} yards is equal to {yd_to_nm} nanometers.')
            break
        elif user_input == 'yards to miles':
            print('Input for yards (whole numbers only)')
            user_input = input()
            yd_to_mi = int(user_input)/1760
            print(f'{user_input} yards is equal to {yd_to_mi} miles.')
            break
        elif user_input == 'yards to feet':
            print('Input for yards (whole numbers only)')
            user_input = input()
            yd_to_ft = int(user_input)*3
            print(f'{user_input} yards is equal to {yd_to_ft} feet.')
            break
        elif user_input == 'yards to inches':
            print('Input for yards (whole numbers only)')
            user_input = input()
            yd_to_in = int(user_input)*36
            print(f'{user_input} yards is equal to {yd_to_in} inches.')
            break
        elif user_input == 'yards to light years':
            print('Input for yards (whole numbers only)')
            user_input = input()
            yd_to_ly = int(user_input)/10346000000000000
            print(f'{user_input} yards is equal to {yd_to_ly} light years.')
            break
        elif user_input == 'feet to meters':
            print('Input for feet (whole numbers only)')
            user_input = input()
            ft_to_m = int(user_input)/3.2808399
            print(f'{user_input} feet is equal to {ft_to_m} meters.')
            break
        elif user_input == 'feet to kilometers':
            print('Input for feet (whole numbers only)')
            user_input = input()
            ft_to_km = int(user_input)/3280.8399
            print(f'{user_input} feet is equal to {ft_to_km} kilometers.')
            break
        elif user_input == 'feet to centimeters':
            print('Input for feet (whole numbers only)')
            user_input = input()
            ft_to_cm = int(user_input)*30.48
            print(f'{user_input} feet is equal to {ft_to_cm} centimeters.')
            break
        elif user_input == 'feet to millimeters':
            print('Input for feet (whole numbers only)')
            user_input = input()
            ft_to_mm = int(user_input)*304.8
            print(f'{user_input} feet is equal to {ft_to_mm} millimeters.')
            break
        elif user_input == 'feet to micrometers':
            print('Input for feet (whole numbers only)')
            user_input = input()
            ft_to_mim = int(user_input)*304800
            print(f'{user_input} feet is equal to {ft_to_mim} micrometers.')
            break
        elif user_input == 'feet to nanometers':
            print('Input for feet (whole numbers only)')
            user_input = input()
            ft_to_nm = int(user_input)*304800000
            print(f'{user_input} feet is equal to {ft_to_nm} nanometers.')
            break
        elif user_input == 'feet to miles':
            print('Input for feet (whole numbers only)')
            user_input = input()
            ft_to_mi = int(user_input)/5280
            print(f'{user_input} feet is equal to {ft_to_mi} miles.')
            break
        elif user_input == 'feet to yards':
            print('Input for feet (whole numbers only)')
            user_input = input()
            ft_to_yd = int(user_input)/3
            print(f'{user_input} feet is equal to {ft_to_yd} yards.')
            break
        elif user_input == 'feet to inches':
            print('Input for feet (whole numbers only)')
            user_input = input()
            ft_to_in = int(user_input)*12
            print(f'{user_input} feet is equal to {ft_to_in} inches.')
            break
        elif user_input == 'feet to light years':
            print('Input for feet (whole numbers only)')
            user_input = input()
            ft_to_ly = int(user_input)/31039000000000000.0
            print(f'{user_input} feet is equal to {ft_to_ly} light years.')
            break
        elif user_input == 'inches to meters':
            print('Input for inches (whole numbers only)')
            user_input = input()
            in_to_m = int(user_input)/39.3700787
            print(f'{user_input} inches is equal to {in_to_m} meters.')
            break
        elif user_input == 'inches to kilometers':
            print('Input for inches (whole numbers only)')
            user_input = input()
            in_to_km = int(user_input)/39370.0787
            print(f'{user_input} inches is equal to {in_to_km} kilometers.')
            break
        elif user_input == 'inches to centimeters':
            print('Input for inches (whole numbers only)')
            user_input = input()
            in_to_cm = int(user_input)*2.54
            print(f'{user_input} inches is equal to {in_to_cm} centimeters.')
            break
        elif user_input == 'inches to millimeters':
            print('Input for inches (whole numbers only)')
            user_input = input()
            in_to_mm = int(user_input)*25.4
            print(f'{user_input} inches is equal to {in_to_mm} millimeters.')
            break
        elif user_input == 'inches to micrometers':
            print('Input for inches (whole numbers only)')
            user_input = input()
            in_to_mim = int(user_input)*25400
            print(f'{user_input} inches is equal to {in_to_mim} micrometers.')
            break
        elif user_input == 'inches to nanometers':
            print('Input for inches (whole numbers only)')
            user_input = input()
            in_to_nm = int(user_input)*25400000
            print(f'{user_input} inches is equal to {in_to_nm} nanometers.')
            break
        elif user_input == 'inches to miles':
            print('Input for inches (whole numbers only)')
            user_input = input()
            in_to_mi = int(user_input)/63360
            print(f'{user_input} inches is equal to {in_to_mi} miles.')
            break
        elif user_input == 'inches to yards':
            print('Input for inches (whole numbers only)')
            user_input = input()
            in_to_yd = int(user_input)/36
            print(f'{user_input} inches is equal to {in_to_yd} yards.')
            break
        elif user_input == 'inches to feet':
            print('Input for inches (whole numbers only)')
            user_input = input()
            in_to_ft = int(user_input)/12
            print(f'{user_input} inches is equal to {in_to_ft} feet.')
            break
        elif user_input == 'inches to light years':
            print('Input for inches (whole numbers only)')
            user_input = input()
            in_to_ly = int(user_input)/372470000000000000.0
            print(f'{user_input} inches is equal to {in_to_ly} light years.')
            break
        elif user_input == 'light years to meters':
            print('Input for light years (whole numbers only)')
            user_input = input()
            ly_to_m = int(user_input)*9460700000000000.0
            print(f'{user_input} light years is equal to {ly_to_m} meters.')
            break
        elif user_input == 'light years to kilometers':
            print('Input for light years (whole numbers only)')
            user_input = input()
            ly_to_km = int(user_input)*9460700000000.0
            print(f'{user_input} light years is equal to {ly_to_km} kilometers.')
            break
        elif user_input == 'light years to centimeters':
            print('Input for light years (whole numbers only)')
            user_input = input()
            ly_to_cm = int(user_input)*946070000000000000.0
            print(f'{user_input} light years is equal to {ly_to_cm} centimeters.')
            break
        elif user_input == 'light years to millimeters':
            print('Input for light years (whole numbers only)')
            user_input = input()
            ly_to_mm = int(user_input)*9460700000000000000.0
            print(f'{user_input} light years is equal to {ly_to_mm} millimeters.')
            break
        elif user_input == 'light years to micrometers':
            print('Input for light years (whole numbers only)')
            user_input = input()
            ly_to_mim = int(user_input)*9460700000000000000000.0
            print(f'{user_input} light years is equal to {ly_to_mim} micrometers.')
            break
        elif user_input == 'light years to nanometers':
            print('Input for light years (whole numbers only)')
            user_input = input()
            ly_to_nm = int(user_input)*9460700000000000000000000.0
            print(f'{user_input} light years is equal to {ly_to_nm} nanometers.')
            break
        elif user_input == 'light years to miles':
            print('Input for light years (whole numbers only)')
            user_input = input()
            ly_to_mi = int(user_input)*5878600000000.0
            print(f'{user_input} light years is equal to {ly_to_mi} miles.')
            break
        elif user_input == 'light years to yards':
            print('Input for light years (whole numbers only)')
            user_input = input()
            ly_to_yd = int(user_input)*10346000000000000.0
            print(f'{user_input} light years is equal to {ly_to_yd} yards.')
            break
        elif user_input == 'light years to feet':
            print('Input for light years (whole numbers only)')
            user_input = input()
            ly_to_ft = int(user_input)*31039000000000000.0
            print(f'{user_input} light years is equal to {ly_to_ft} feet.')
            break
        elif user_input == 'light years to inches':
            print('Input for light years (whole numbers only)')
            user_input = input()
            ly_to_in = int(user_input)*372470000000000000.0
            print(f'{user_input} light years is equal to {ly_to_in} inches.')
            break
        else:
            print('Please choose 2 units')
        
    elif user_input == '2':
        print('What 2 units would you like to covert from?')
        print(time_category)
        user_input = input()
        if user_input == 'seconds to milliseconds':
            print('Input for seconds (whole numbers only)')
            user_input = input()
            s_to_ms = int(user_input)*1000
            print(f'{user_input} seconds is equal to {s_to_ms} milliseconds.')
            break
        elif user_input == 'seconds to microseconds':
            print('Input for seconds (whole numbers only)')
            user_input = input()
            s_to_mis = int(user_input)*1000000
            print(f'{user_input} seconds is equal to {s_to_mis} microseconds.')
            break
        elif user_input == 'seconds to nanoseconds':
            print('Input for seconds (whole numbers only)')
            user_input = input()
            s_to_ns = int(user_input)*1000000000
            print(f'{user_input} seconds is equal to {s_to_ns} nanoseconds.')
            break
        elif user_input == 'seconds to picoseconds':
            print('Input for seconds (whole numbers only)')
            user_input = input()
            s_to_ps = int(user_input)*1000000000000
            print(f'{user_input} seconds is equal to {s_to_ps} picoseconds.')
            break
        elif user_input == 'seconds to minutes':
            print('Input for seconds (whole numbers only)')
            user_input = input()
            s_to_min = int(user_input)/60
            print(f'{user_input} seconds is equal to {s_to_min} minute.')
            break
        elif user_input == 'seconds to hours':
            print('Input for seconds (whole numbers only)')
            user_input = input()
            s_to_h = int(user_input)/3600
            print(f'{user_input} seconds is equal to {s_to_h} hours.')
            break
        elif user_input == 'seconds to days':
            print('Input for seconds (whole numbers only)')
            user_input = input()
            s_to_d = int(user_input)/86400
            print(f'{user_input} seconds is equal to {s_to_d} days.')
            break
        elif user_input == 'seconds to weeks':
            print('Input for seconds (whole numbers only)')
            user_input = input()
            s_to_w = int(user_input)/604800
            print(f'{user_input} seconds is equal to {s_to_w} weeks.')
            break
        elif user_input == 'seconds to months':
            print('Input for seconds (whole numbers only)')
            user_input = input()
            s_to_mon = int(user_input)/2628000
            print(f'{user_input} seconds is equal to {s_to_mon} months.')
            break
        elif user_input == 'seconds to years':
            print('Input for seconds (whole numbers only)')
            user_input = input()
            s_to_y = int(user_input)/31536000
            print(f'{user_input} seconds is equal to {s_to_y} years.')
            break
        elif user_input == 'milliseconds to seconds':
            print('Input for milliseconds (whole numbers only)')
            user_input = input()
            ms_to_s = int(user_input)/1000
            print(f'{user_input} milliseconds is equal to {ms_to_s} milliseconds.')
            break
        elif user_input == 'milliseconds to microseconds':
            print('Input for milliseconds (whole numbers only)')
            user_input = input()
            ms_to_mis = int(user_input)*1000
            print(f'{user_input} milliseconds is equal to {ms_to_mis} microseconds.')
            break
        elif user_input == 'milliseconds to nanoseconds':
            print('Input for milliseconds (whole numbers only)')
            user_input = input()
            ms_to_ns = int(user_input)*1000000
            print(f'{user_input} milliseconds is equal to {ms_to_ns} nanoseconds.')
            break
        elif user_input == 'milliseconds to picoseconds':
            print('Input for milliseconds (whole numbers only)')
            user_input = input()
            ms_to_ps = int(user_input)*1000000000
            print(f'{user_input} milliseconds is equal to {ms_to_ps} microseconds.')
            break
        elif user_input == 'milliseconds to minutes':
            print('Input for milliseconds (whole numbers only)')
            user_input = input()
            ms_to_min = int(user_input)/60000
            print(f'{user_input} milliseconds is equal to {ms_to_min} minutes.')
            break
        elif user_input == 'milliseconds to hours':
            print('Input for milliseconds (whole numbers only)')
            user_input = input()
            ms_to_h = int(user_input)/3600000
            print(f'{user_input} milliseconds is equal to {ms_to_h} hours.')
            break
        elif user_input == 'milliseconds to days':
            print('Input for milliseconds (whole numbers only)')
            user_input = input()
            ms_to_d = int(user_input)/86400000
            print(f'{user_input} milliseconds is equal to {ms_to_d} days.')
            break
        elif user_input == 'milliseconds to weeks':
            print('Input for milliseconds (whole numbers only)')
            user_input = input()
            ms_to_w = int(user_input)/604800000
            print(f'{user_input} milliseconds is equal to {ms_to_w} weeks.')
            break
        elif user_input == 'milliseconds to months':
            print('Input for milliseconds (whole numbers only)')
            user_input = input()
            ms_to_mon = int(user_input)/2628000000
            print(f'{user_input} milliseconds is equal to {ms_to_mon} months.')
            break
        elif user_input == 'milliseconds to years':
            print('Input for milliseconds (whole numbers only)')
            user_input = input()
            ms_to_y = int(user_input)/31536000000
            print(f'{user_input} milliseconds is equal to {ms_to_y} years.')
            break
        elif user_input == 'microseconds to seconds':
            print('Input for microseconds (whole numbers only)')
            user_input = input()
            mis_to_s = int(user_input)/1000000
            print(f'{user_input} microseconds is equal to {mis_to_s} microseconds.')
            break
        elif user_input == 'microseconds to milliseconds':
            print('Input for microseconds (whole numbers only)')
            user_input = input()
            mis_to_ms = int(user_input)/1000
            print(f'{user_input} microseconds is equal to {mis_to_ms} milliseconds.')
            break
        elif user_input == 'microseconds to nanoseconds':
            print('Input for microseconds (whole numbers only)')
            user_input = input()
            mis_to_ns = int(user_input)*1000
            print(f'{user_input} microseconds is equal to {mis_to_ns} nanoseconds.')
            break
        elif user_input == 'microseconds to picoseconds':
            print('Input for microseconds (whole numbers only)')
            user_input = input()
            mis_to_ps = int(user_input)*1000000
            print(f'{user_input} microseconds is equal to {mis_to_ps} picoseconds.')
            break
        elif user_input == 'microseconds to minutes':
            print('Input for microseconds (whole numbers only)')
            user_input = input()
            mis_to_min = int(user_input)/60000000
            print(f'{user_input} microseconds is equal to {mis_to_min} minutes.')
            break
        elif user_input == 'microseconds to hours':
            print('Input for microseconds (whole numbers only)')
            user_input = input()
            mis_to_h = int(user_input)/3600000000
            print(f'{user_input} microseconds is equal to {mis_to_h} hours.')
            break
        elif user_input == 'microseconds to days':
            print('Input for microseconds (whole numbers only)')
            user_input = input()
            mis_to_d = int(user_input)/86400000000
            print(f'{user_input} microseconds is equal to {mis_to_d} days.')
            break
        elif user_input == 'microseconds to weeks':
            print('Input for microseconds (whole numbers only)')
            user_input = input()
            mis_to_w = int(user_input)/604800000000
            print(f'{user_input} microseconds is equal to {mis_to_w} weeks.')
            break
        elif user_input == 'microseconds to months':
            print('Input for microseconds (whole numbers only)')
            user_input = input()
            mis_to_mon = int(user_input)/2628000000000
            print(f'{user_input} microseconds is equal to {mis_to_mon} months.')
            break
        elif user_input == 'microseconds to years':
            print('Input for microseconds (whole numbers only)')
            user_input = input()
            mis_to_y = int(user_input)/31536000000000
            print(f'{user_input} microseconds is equal to {mis_to_y} years.')
            break
        elif user_input == 'nanoseconds to seconds':
            print('Input for nanoseconds (whole numbers only)')
            user_input = input()
            ns_to_s = int(user_input)/1000000000
            print(f'{user_input} nanoseconds is equal to {ns_to_s} seconds.')
            break
        elif user_input == 'nanoseconds to milliseconds':
            print('Input for nanoseconds (whole numbers only)')
            user_input = input()
            ns_to_ms = int(user_input)/1000000
            print(f'{user_input} nanoseconds is equal to {ns_to_ms} milliseconds.')
            break
        elif user_input == 'nanoseconds to microseconds':
            print('Input for nanoseconds (whole numbers only)')
            user_input = input()
            ns_to_mis = int(user_input)/1000
            print(f'{user_input} nanoseconds is equal to {ns_to_mis} microseconds.')
            break
        elif user_input == 'nanoseconds to picoseconds':
            print('Input for nanoseconds (whole numbers only)')
            user_input = input()
            ns_to_ps = int(user_input)*1000
            print(f'{user_input} nanoseconds is equal to {ns_to_ps} picoseconds.')
            break
        elif user_input == 'nanoseconds to minutes':
            print('Input for nanoseconds (whole numbers only)')
            user_input = input()
            ns_to_min = int(user_input)/60000000000.0
            print(f'{user_input} nanoseconds is equal to {ns_to_min} minutes.')
            break
        elif user_input == 'nanoseconds to hours':
            print('Input for nanoseconds (whole numbers only)')
            user_input = input()
            ns_to_h = int(user_input)/3600000000000.0
            print(f'{user_input} nanoseconds is equal to {ns_to_h} hours.')
            break
        elif user_input == 'nanoseconds to days':
            print('Input for nanoseconds (whole numbers only)')
            user_input = input()
            ns_to_d = int(user_input)/86400000000000.0
            print(f'{user_input} nanoseconds is equal to {ns_to_d} days.')
            break
        elif user_input == 'nanoseconds to weeks':
            print('Input for nanoseconds (whole numbers only)')
            user_input = input()
            ns_to_w = int(user_input)/604800000000000.0
            print(f'{user_input} nanoseconds is equal to {ns_to_w} weeks.')
            break
        elif user_input == 'nanoseconds to months':
            print('Input for nanoseconds (whole numbers only)')
            user_input = input()
            ns_to_mon = int(user_input)/2628000000000000.0
            print(f'{user_input} nanoseconds is equal to {ns_to_mon} months.')
            break
        elif user_input == 'nanoseconds to years':
            print('Input for nanoseconds (whole numbers only)')
            user_input = input()
            ns_to_y = int(user_input)/31536000000000000.0
            print(f'{user_input} nanoseconds is equal to {ns_to_y} years.')
            break
        elif user_input == 'picoseconds to seconds':
            print('Input for picoseconds (whole numbers only)')
            user_input = input()
            ps_to_s = int(user_input)/1000000000000.0
            print(f'{user_input} picoseconds is equal to {ps_to_s} seconds.')
            break
        elif user_input == 'picoseconds to milliseconds':
            print('Input for picoseconds (whole numbers only)')
            user_input = input()
            ps_to_ms = int(user_input)/1000000000.0
            print(f'{user_input} picoseconds is equal to {ps_to_ms} milliseconds.')
            break
        elif user_input == 'picoseconds to microseconds':
            print('Input for picoseconds (whole numbers only)')
            user_input = input()
            ps_to_ms = int(user_input)/1000000.0
            print(f'{user_input} picoseconds is equal to {ps_to_ms} microseconds.')
            break
        elif user_input == 'picoseconds to nanoseconds':
            print('Input for picoseconds (whole numbers only)')
            user_input = input()
            ps_to_ns = int(user_input)/1000.0
            print(f'{user_input} picoseconds is equal to {ps_to_ns} nanoseconds.')
            break
        elif user_input == 'picoseconds to minutes':
            print('Input for picoseconds (whole numbers only)')
            user_input = input()
            ps_to_min = int(user_input)/60000000000000.0
            print(f'{user_input} picoseconds is equal to {ps_to_min} minutes.')
            break
        elif user_input == 'picoseconds to hours':
            print('Input for picoseconds (whole numbers only)')
            user_input = input()
            ps_to_h = int(user_input)/3600000000000000.0
            print(f'{user_input} picoseconds is equal to {ps_to_h} hours.')
            break
        elif user_input == 'picoseconds to days':
            print('Input for picoseconds (whole numbers only)')
            user_input = input()
            ps_to_d = int(user_input)/86400000000000000.0
            print(f'{user_input} picoseconds is equal to {ps_to_d} days.')
            break
        elif user_input == 'picoseconds to weeks':
            print('Input for picoseconds (whole numbers only)')
            user_input = input()
            ps_to_w = int(user_input)/604800000000000000.0
            print(f'{user_input} picoseconds is equal to {ps_to_w} weeks.')
            break
        elif user_input == 'picoseconds to months':
            print('Input for picoseconds (whole numbers only)')
            user_input = input()
            ps_to_m = int(user_input)/2628000000000000000.0
            print(f'{user_input} picoseconds is equal to {ps_to_m} months.')
            break
        elif user_input == 'picoseconds to years':
            print('Input for picoseconds (whole numbers only)')
            user_input = input()
            ps_to_y = int(user_input)/31536000000000000000.0
            print(f'{user_input} picoseconds is equal to {ps_to_y} years.')
            break
        elif user_input == 'minutes to seconds':
            print('Input for minutes (whole numbers only)')
            user_input = input()
            min_to_s = int(user_input)*60
            print(f'{user_input} minutes is equal to {min_to_s} seconds.')
            break
        elif user_input == 'minutes to milliseconds':
            print('Input for minutes (whole numbers only)')
            user_input = input()
            min_to_ms = int(user_input)*60000
            print(f'{user_input} minutes is equal to {min_to_ms} milliseconds.')
            break
        elif user_input == 'minutes to microseconds':
            print('Input for minutes (whole numbers only)')
            user_input = input()
            min_to_mis = int(user_input)*60000000
            print(f'{user_input} minutes is equal to {min_to_mis} microseconds.')
            break
        elif user_input == 'minutes to nanoseconds':
            print('Input for minutes (whole numbers only)')
            user_input = input()
            min_to_ns = int(user_input)*60000000000
            print(f'{user_input} minutes is equal to {min_to_ns} nanoseconds.')
            break
        elif user_input == 'minutes to picoseconds':
            print('Input for minutes (whole numbers only)')
            user_input = input()
            min_to_ps = int(user_input)*60000000000000
            print(f'{user_input} minutes is equal to {min_to_ps} picoseconds.')
            break
        elif user_input == 'minutes to hours':
            print('Input for minutes (whole numbers only)')
            user_input = input()
            min_to_h = int(user_input)/60
            print(f'{user_input} minutes is equal to {min_to_h} hours.')
            break
        elif user_input == 'minutes to days':
            print('Input for minutes (whole numbers only)')
            user_input = input()
            min_to_d = int(user_input)/1440
            print(f'{user_input} minutes is equal to {min_to_d} days.')
            break
        elif user_input == 'minutes to weeks':
            print('Input for minutes (whole numbers only)')
            user_input = input()
            min_to_w = int(user_input)/10080
            print(f'{user_input} minutes is equal to {min_to_w} weeks.')
            break
        elif user_input == 'minutes to months':
            print('Input for minutes (whole numbers only)')
            user_input = input()
            min_to_mon = int(user_input)/43800
            print(f'{user_input} minutes is equal to {min_to_mon} months.')
            break
        elif user_input == 'minutes to years':
            print('Input for minutes (whole numbers only)')
            user_input = input()
            min_to_y = int(user_input)/525600
            print(f'{user_input} minutes is equal to {min_to_y} years.')
            break
        
        break
    elif user_input == '3':
        print(temperature_category)
        break
    elif user_input == '4':
        print(weight_category)
        break
    else:
        print('Please choose a category')