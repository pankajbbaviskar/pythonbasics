def factorial(n):
    if n == 0 or n==1:
        return 1
    return n * factorial(n-1)

def fibonacchi(n):
    if n<=1:
        return n
    return fibonacchi(n-1) + fibonacchi(n-2)

def sum_pf_digits(n):
    if n<10:
        return n
    return n%10 + sum_pf_digits( n // 10)

def is_armstrong_number(number):
    # Convert the number to a string to access each digit
    num_str = str(number)
    # Calculate the length of the number
    length = len(num_str)
    # Initialize sum to zero
    sum = 0
    # Iterate through each digit
    for digit in num_str:
        # Convert digit back to integer and raise to the power of length
        sum += int(digit) ** length
    # Check if the sum equals the original number
    return sum == number

def main():
    while True:
        print("Welcome to the recursion program")
        print("1. Factorial of a number")
        print("2. Fibonacchi of a number")
        print("3. Sum of digits of a number")
        print("4. Check Armstrong number")
        print("5. Exit")

        choice = int(input("Please Enter your choice (1 to 4) : "))

        if choice == 5:
            print("Thank you for using the program")
            break

        elif choice == 1:
            try:
                num = int(input("please Enter a number to find factorial you want : "))
                if num < 0:
                    print("Please give a valid number, Please provide a positive number..")
                result = factorial(num)
                print(f"Factorial of {num} is {result} .")
            except ValueError:
                print("Please give a valid number, Please provide a positive number..")

        elif choice == 2:
            try:
                num = int(input("please Enter a number to find fibonacchi you want : "))
                if num < 0:
                    print("Please give a valid number, Please provide a positive number..")
                result = fibonacchi(num)
                print(f"Fibonacchi of {num} is {result} .")
            except ValueError:
                print("Please give a valid number, Please provide a positive number..")

        elif choice == 3:
            try:
                num = int(input("please Enter a number whose sum series you want : "))
                if num < 0:
                    print("Please enter a valid number..")
                result = sum_pf_digits(num)
                print(f"Sum of digits of {num} is {result} .")
            except ValueError:
                print("Please enter a valid number")
                
        elif choice == 4:
            try:
                num = int(input("please Enter a number to check Armstrong number : "))
                if num < 0:
                    print("Please enter a valid number..")
                if is_armstrong_number(num):
                    print(f"{num} is an Armstrong number.")
                else:
                    print(f"{num} is not an Armstrong number.")
            except ValueError:
                print("Please enter a valid number")
        
        else:
            print("Invalid Choise, Please select 1-5")

if __name__ == "__main__":
    main() 