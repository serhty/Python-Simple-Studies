#We ask the user to enter two numbers. We print the least common multiple of the two numbers entered with the function

def leastCommonMultiple(a,b):
    leastCommonMultiple = a*b #at first we equated the least common multiple to the product of two numbers
    for number in range(leastCommonMultiple,max(a,b),-1): #We reduce the number by 1 with the "-1" expression at the end and get the number into the for loop.
        if number % a == 0 and number % b == 0: # We are checking to see if there is a number that is smaller than the product of a multiple of two. If there is, we equate the least common multiple to that number.
            leastCommonMultiple = number
    
    return leastCommonMultiple

firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))
print(leastCommonMultiple(firstNumber,secondNumber))