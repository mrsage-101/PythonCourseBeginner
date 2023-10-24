
operator_choice = input("Enter operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator_choice == "+":
    add = num1 + num2
    print(f"Addtion result of {num1} + {num2}: {add}")
elif operator_choice == "-":
    sub = num1 - num2
    print(f"Subtraction result of {num1} + {num2}: {sub}")
elif operator_choice == "*":
    mul = num1 * num2
    print(f"Multiplication result of {num1} * {num2}: {mul}")
elif operator_choice == "/":
    div = num1 / num2
    print(f"Division result of {num1} / {num2}: {div}")
else:
    print("You choose not the mentioned operator")