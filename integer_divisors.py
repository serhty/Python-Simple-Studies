# It asks the user to enter a number. We print the integer divisors of the entered number using a function
def integerDivisors(number):
    list = [] #We first define the list that we will print the integer divisors as empty.
    for i in range(1,number): #We try the numbers from 1 to the entered number one by one with the range in the for loop
        if number % i == 0:
            list.append(i) #If the remainder of the division of the entered number by the number tested in the loop is zero, we add i to the list.
    
    return list

inputNumber = int(input("Please enter an integer: "))
print(integerDivisors(inputNumber))