print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")

calculator = input()

if calculator == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is:", str(int(num1) + int(num2)))
elif calculator == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is:", str(int(num1) - int(num2)))
elif calculator == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is:", str(int(num1) * int(num2)))
elif calculator == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is:", str(int(num1) / int(num2)))
else:
    print("               ERROR!!!!!!")

