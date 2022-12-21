# The user initially has $2000 money. When we insert the card into the ATM, we will start an unlimited loop. User scenarios: 1-withdrawal, 2-deposit, 3-card information, 4-card refund(we will end the unlimited cycle)

money = 2000
choice = input("Press 'e' to insert your card, 'q' to exit")

if choice == "e":
    while True:
        process = int(input("""
                        Transactions:
                        ------------
                        1- Withdrawal
                        2- Deposit
                        3- Card Information
                        4- Card Return
                        
                        Enter the Transaction Number You Want to Perform: 
                        """))
        if process == 1:
            amount = int(input("How much money do you want to withdraw?: "))
            if money < amount:
                print("Insufficient Balance")
            else:
                money -= amount
                print("Balance: {}".format(money))
        if process == 2:
            amount = int(input("How much money do you want to deposit?: "))
            money += amount
            print("Balance: {}".format(money))
        if process == 3:
            print("Account info\n ********* \nName: Name\nAccount number:0123456789\nBalance: {}".format(money))
        if process == 4:
            print("You can take your card and leave the ATM.")
            break
else:
    print("Process Terminated.")