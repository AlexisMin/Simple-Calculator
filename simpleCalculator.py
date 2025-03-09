def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error! Division by zero."
    return round(a / b, 2)

def integer_division(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a // b

def simple_calculator():
    while True:
        print("===== Simple Calculator =====")
        print("1: Addition")
        print("2: Subtraction")
        print("3: Multiplication")
        print("4: Division")
        print("5: Integer Division")
        
        user_choice = input("Please enter one of these numbers for calculation (1/2/3/4/5): ")
        
        if user_choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if user_choice == '1':
                print("Addition Result:", addition(num1, num2))

            elif user_choice == '2':
                print("Subtraction Result:", subtraction(num1, num2))

            elif user_choice == '3':
                print("Multiplication Result:", multiplication(num1, num2))

            elif user_choice == '4':
                print("Division Result:", division(num1, num2))

            elif user_choice == '5':
                print("Integer Division Result:", integer_division(num1, num2))

        else:
            print("Your choice is invalid. Please try again!")
            continue
        
        progress = input("Do you want to continue? (yes/no): ").strip().lower()
        if progress == 'no':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    simple_calculator()
