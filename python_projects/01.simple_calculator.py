"""
    Hi , this is my first project 
    a very simple python calculator
"""
print("Hello, welcome to basic calculator in python")

while True:
    
    # getting the inputs from the user
    while True:
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            op = str(input("Enter your operation (+, -, *, ^, /, //, %): "))
        except ValueError:
            print("Oops, something went wrong! Please try again.")
        else:
            break

    # now doing the operation
    if op == "+":
        print(f"{num1} + {num2} = {num1+num2}")
    elif op == "-":
        print(f"{num1} - {num2} = {num1-num2}")
    elif op == "*":
        print(f"{num1} * {num2} = {num1*num2}")
    elif op == "^":
        print(f"{num1} ^ {num2} = {num1**num2}")
    elif op == "/":
        if num2 == 0:
            print("Error: division by zero")
        else:
            print(f"{num1} / {num2} = {num1/num2}")
    elif op == "//":
        print(f"{num1} // {num2} = {num1//num2}")
    elif op == "%":
        print(f"{num1} % {num2} = {num1%num2}")
    else:
        print("You've entered the wrong operand!")

    # deciding to go over or exit the program
    print("Do you want to do another calculation? (y/n)")

    try:
        while True:
            flag = str(input())
            if flag == "y":
                first_loop_flag = False
                break
            elif flag == "n":
                first_loop_flag = True
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
    except Exception:
        print("Error, exiting the program...")
        break

    # deciding to break the loop
    if first_loop_flag:
        break
    else:
        continue
