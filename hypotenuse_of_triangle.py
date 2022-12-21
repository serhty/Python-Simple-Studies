# a and b indicate the side lengths of the triangle, and c will be the length of the triangle's hypotenuse.

a = input("Enter the length of side a: ") #With input, we get the length of side a from the user.
a = int(a) #Values ​​from the input are of string data type. Since we will do mathematical operations, we convert the incoming string value to integer data.

#We repeat the same operations we did for side a above for side b. We converted the data from the input directly to an integer on the same line.
b = int(input("Enter the length of side b: "))

# !!! CAUTION !!!
# Data entered with integer must be integer. If you want to allow the user to enter decimals as side lengths, you should change the entered value as a float instead of an integer: b = float(input("Enter the length of side b: "))

c = (a**2 + b**2)**0.5 #The formula for the length of side c, the hypotenuse

print("Hypotenuse Length: ",c) #We print the calculation of the hypotenuse with the print function

#or Another use of the print function
#print("Hypotenuse Length: {} ".format(c))