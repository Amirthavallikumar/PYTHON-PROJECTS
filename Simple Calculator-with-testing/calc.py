#Program make a simple calculator and use Unitest testing


# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    if (y==0):
        raise ValueError('Denominator cannot be zero')
    return x / y



print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    #validating user input
    if (isinstance(choice,int)) and (int(choice)>=4):
        continue
    # check if choice is one of the four options
    elif choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ").lower()
        if next_calculation == "no":
             break
        elif next_calculation=="yes":
             continue
        else:
            next_calculation = input("Let's do next calculation? (yes/no): ").lower()
            if next_calculation == "no":
                break
            elif next_calculation == "yes":
                continue
            else:
                print("exiting")
                break
    else:
        print("Invalid Input")

