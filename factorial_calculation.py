# Taking a positive integer from the user, we calculate the factorial of that number.

number = int(input("Please enter a number: "))
factorial = 1
for i in range(1,number+1): # With range, we repeat the loop for all numbers from 1 to 1 more than the entered number.
    factorial = factorial * i

print("Factorial {}! = {}".format(number,factorial))