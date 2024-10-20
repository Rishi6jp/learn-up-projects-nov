def calculator():
    print("Welcome to simple calculator")

    while True: 
        num1 = float(input("Enter First digit: "))
        num2 = float(input("Enter Second number: "))

        print("Select an operation: +, -, *, /")
        operation = input("Enter the operation: ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1/num2
            else: 
                print("Error: Cannot divide by zero!")
                continue
        else: 
            print("Invalid operation. Please Try again")

        print(f" The resule of {num1} {operation} {num2} is: {result}")

        another_calc = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calc != "yes":
            break

calculator()