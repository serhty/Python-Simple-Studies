# When the voltage and resistance value are entered, we find the current value

# WAY 1
v = float(input("Enter Voltage Value: "))  # We get value from user.
r = float(input("Enter Resistance Value: "))  # We get value from user.
i = v/r  # We divide the variable v with the variable r.
print("Current : {}".format(i))  # We write the variable i.

# WAY 2
# If the resistance is 0, we check with the while loop and ask the user to re-enter that value.
# v = float(input("Enter Voltage Value: "))
# r = float(input("Enter Resistance Value: "))
# while True:
#     r == 0:
#         r = float(input("The resistor value cannot be 0. Re-enter: "))
#     else:
#         break
# i = v/r
# print("Current : {}".format(i))

# WAY 3
# We check with "try-except" whether the resistor value is zero.
# v = float(input("Enter Voltage Value: "))
# while True:
#     try: # We check to see if it gives an error. If there is no error, we write what to do.
#         r = float(input("Enter Resistance Value: "))
#         i = v/r
#         break
#     except: #If there is an error, we write what needs to be done.
#         print("The resistor value cannot be 0!")
# print("Current : {}".format(i))
