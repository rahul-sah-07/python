# Time Unit Converter with Choice Selection & Restart

while True:
    print("\n----- Time Unit Converter -----")
    print("1. Seconds to Minutes")
    print("2. Minutes to Seconds")
    print("3. Minutes to Hours")
    print("4. Hours to Minutes")
    print("5. Hours to Days")
    print("6. Days to Hours")

    choice = int(input("Enter your choice (1–6): "))

    if choice >=1 and choice <=6:
        value = float(input("Enter the time value: "))
    else:
        print("Invalid Choice! Please choose 1–6 only.")
        continue

    
    if choice == 1:
        print("Result:", value / 60, "minutes")
    elif choice == 2:
        print("Result:", value * 60, "seconds")
    elif choice == 3:
        print("Result:", value / 60, "hours")
    elif choice == 4:
        print("Result:", value * 60, "minutes")
    elif choice == 5:
        print("Result:", value / 24, "days")
    elif choice == 6:
        print("Result:", value * 24, "hours")

 
    print("\nOptions:")
    print("1. New Conversion")
    print("2. Change Choice")
    print("3. Exit Program")

    opt = input("Enter your option (1/2/3): ")

    if opt == "1":     # value फिर से होगा
        continue
    elif opt == "2":   # same loop (menu फिर से दिखेगा)
        continue
    elif opt == "3":   # program exit
        print("Program End. Thank you!")
        break
    else:
        print("Invalid option! Program closed.")
        break
