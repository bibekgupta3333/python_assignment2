# 17. Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.


def basicCalculator():
    print("Select operation.\n1.Add\n2.Subtract\n3.Multiply\n4.Divide")
    choice = str(input("Enter choice(1/2/3/4)\n: "))
    while True:
        num1 = eval(input("Enter first number: "))
        num2 = eval(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", num1+num2)
            break
        elif choice == '2':
            print(num1, "-", num2, "=", num1-num2)
            break
        elif choice == '3':
            print(num1, "*", num2, "=", num1*num2)
            break
        elif choice == '4':
            print(num1, "/", num2, "=", num1/num2)
            break


if __name__ == "__main__":
    basicCalculator()
