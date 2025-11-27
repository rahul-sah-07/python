print(" Simple Calculator ")

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nChoose operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print(num1 + num2)
        elif choice == "2":
            print(num1 - num2)
        elif choice == "3":
            print(num1 * num2)
        elif choice == "4":
            try:
                print(num1 / num2)
            except ZeroDivisionError:
                print("Error: Cannot divide by zero!")
        elif choice == "5":
            print("Exiting calculator.")
            break
        else:
            print("Invalid choice.")

    except ValueError:
        print("Error: Enter valid numbers.")
    except Exception as e:
        print("Unexpected error:", e)

    print("\n------------------------------\n")
