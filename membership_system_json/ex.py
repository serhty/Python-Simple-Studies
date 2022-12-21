# login, register (with the activation code, not by sending an e-mail for now, but by printing it to a file), I forgot my password (by changing the old password with the new password), we will log out
import json
from random import randint

class System:
    def __init__(self):
        self.statu = True
        self.datas = self.getDatas()
        
    def run(self):
        self.showMenu()
        choice = self.menuChoice()
        if choice == 1:
            self.login()
        if choice == 2:
            self.signup()
        if choice == 3:
            self.forgotPassword()
        if choice == 4:
            self.logout()
    
    def showMenu(self):
        print("""
              1- Login
              2- Signin
              3- Forgot Password
              4- Logout
              """)
    
    def menuChoice(self):
        while True:
            try:
                choice = int(input("Enter your choice: "))
                while choice < 1 or choice > 4:
                    choice = int(input("Enter Your Choice Between 1-4: "))
                break
            except ValueError:
                print("Please Enter Number!\n")
        
        return choice
    
    def getDatas(self):
        try:
            with open("users.json","r") as file:
                datas = json.load(file)
        except FileNotFoundError:
            with open("users.json","w") as file:
                file.write("{}")
                
            with open("users.json","r") as file:
                datas = json.load(file)
        
        return datas
    
    def login(self):
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        statu = self.check(username,password)
        if statu:
            self.loginSuccessful()
        else:
            self.loginFailed("Information Incorrect")
        
    def signup(self):
        username = input("Enter Your Username: ")
        while True:
            password = input("Enter Your Password: ")
            againPassword = input("Reenter password:  ")
            if password == againPassword:
                break
            else:
                print("Passwords Do Not Match. Enter Again:")
        email = input("Enter Email: ")
        
        statu = self.signinCheck(username, email)
        if statu:
            print("Username or email registered in the system")
        else:
            activationCode = self.activationCodeSend()
            activationStatu = self.activationCheck(activationCode)
            
            if activationStatu:
                self.save(username, password, email, )
            else:
                print("Activation Invalid")
        
    
    def forgotPassword(self):
        mail = input("Enter your e-mail address: ")
        if self.mailCheck(mail):
            with open("activation.txt","w") as file:
                activation = str(randint(1000,9999))
                file.write(activation)
                
            activationEnter = input("Enter Activation Code: ")
        
            if activationEnter == activation:
                while True:
                    newPassword = input("Enter New Password: ")
                    againNewPassword = input("Enter New Password: ")
                
                    if newPassword == againNewPassword:
                        break
                    else:
                        print("Passwords Do Not Match")
            self.datas = self.getDatas()
            for user in self.datas["users"]:
                if user["mail"] == mail:
                    user["password"] = str(newPassword)
                    
            with open("users.json","w") as file:
                json.dump(self.datas,file)
                print("The password was changed")
            
            
        else:
            print("Mail Kayıtlı Değil")
        
    def mailCheck(self, mail):
        self.datas = self. getDatas()
        for user in self.datas["users"]:
            if user["mail"] == mail:
                return True
            
        return False
    
    def logout(self):
        self.statu = False
    
    def check(self, username, password):
        self.datas = self.getDatas()
        for user in self.datas["users"]:
            if user["username"] == username and user["password"] == password and user["timeout"] == "0" and user["activation"] == "Y":
                return True
        
        return False

    def loginFailed(self,reason):
        print(reason)
    
    def loginSuccessful(self):
        print("Hoş Geldiniz")
        self.statu = False
    
    def signinCheck(self, username, email):
        self.datas = self.getDatas()
        try:
            for user in self.datas["users"]:
                if user["username"] == username and user["mail"] == email:
                    return True
        except KeyError:
            return False
            
        return False
    
    def activationCodeSend(self):
        with open("activationcode.txt","w") as file:
            activation = str(randint(1000,9999))
            file.write(activation)
        
        return activation
    
    def activationCheck(self, activation):
        getActivationCode = input("Enter Activation Code: ")
        if activation == getActivationCode:
            return True
        else:
            return False
    
    def save(self, username, password, mail):
        self.datas = self.getDatas()
        try:
            self.datas["users"].append({"username" : username, "password" : password, "mail" : mail, "activation" : "Y", "timeout" : "0"})
        except KeyError:
            self.datas["users"] = []
            self.datas["users"].append({"username" : username, "password" : password, "mail" : mail, "activation" : "Y", "timeout" : "0"})
            
        with open("users.json","w") as file:
            json.dump(self.datas,file)
            print("Registration successfully created")

system = System()
while system.statu:
    system.run()







