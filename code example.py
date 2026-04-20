

while True: # Loop indefinitely until a valid choice breaks it
    print("\nChoose your primary backend language:")
    user_input = input("1) Python | 2) Go | 3) Java [Enter 1, 2, or 3]: ")

    if user_input == '1':
        selected_language = "Python"
        print("Excellent choice!")
        user_input = input()
        if user_input == 'meters to km':
            print('a')
        elif user_input == 'meters to cm':
            print('b')
            
        break # Exit the loop
    elif user_input == '2':
        selected_language = "Go"
        print("Speedy!")
        break # Exit the loop
    elif user_input == '3':
        selected_language = "Java"
        print("Very enterprise.")
        break # Exit the loop
    else:
        # Invalid input, loop continues
        print("Invalid choice. Please enter 1, 2, or 3.")
        # 'continue' is implicit here, loop restarts

print(f"\nSelected Language: {selected_language}")