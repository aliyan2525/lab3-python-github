num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))

def add(x, y):
    print("Addition of two numbers is", x + y)

def sub(x, y):
    print("Subtraction of two numbers is", x - y)

def mult(x, y):
    print("Multiplication of two numbers is", x * y)

def div(x, y):
    if y == 0:
        print("Invalid Number")
    else:
        print("Division of two numbers is", x / y)

def eo(x, y):
    if x % 2 == 0:
        print("Number 1 is even")
    else:
        print("Number 1 is odd")

    if y % 2 == 0:
        print("Number 2 is even")
    else:
        print("Number 2 is odd")

def perc(x, y):
    if y == 0:
        print("Modulus by zero is not allowed")
    else:
        print("Modulus is", (x / y)/100)

def fact(num1, num2):
    if num1 >= 0:
        factorial = 1
        for i in range(1, num1 + 1):
            factorial *= i
        print("Factorial of Number 1 is", factorial)
    else:
        print("Enter a non-negative number for Number 1")

    if num2 >= 0:
        factorial1 = 1
        for i in range(1, num2 + 1):
            factorial1 *= i
        print("Factorial of Number 2 is", factorial1)
    else:
        print("Enter a non-negative number for Number 2")

while True:
    print(
        "\nOperations:\n"
        "1. Addition\n"
        "2. Subtraction\n"
        "3. Multiplication\n"
        "4. Division\n"
        "5. Even/Odd\n"
        "6. Percentage\n"
        "7. Factorial\n"
        "8. Exit"
    )

    operation = int(input("Enter the number of operation you want to perform: "))

    if operation == 1:
        add(num1, num2)
    elif operation == 2:
        sub(num1, num2)
    elif operation == 3:
        mult(num1, num2)
    elif operation == 4:
        div(num1, num2)
    elif operation == 5:
        eo(num1, num2)
    elif operation == 6:
        perc(num1, num2)
    elif operation == 7:
        fact(num1, num2)
    elif operation == 8:
        print("Exiting program...")
        break
    else:
        print("Invalid operation!")