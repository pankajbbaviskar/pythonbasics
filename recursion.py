def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# a=factorial(7)
# print(a)

# 0,1,1,2,3,5,8,13,21,34

def fibonacchi(n):
    if n<=1:
        return n
    return fibonacchi(n-1) + fibonacchi(n-2)

# a=fibonacchi(20)
# print(a)

# 729 = 7 + 2 + 9

def sum_pf_digits(n):
    if n<10:
        return n
    return n%10 + sum_pf_digits( n // 10)

# a=sum_pf_digits(729)
# print(a)

number = int(input("Enter a number: "))
original_number = number
n = 0
suum = 0
digit = 0

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

if  is_armstrong_number(number):
    print(f"{original_number} is an Armstrong number.")
else:
    print(f"{original_number} is not an Armstrong number.")