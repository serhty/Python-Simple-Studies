# we will do employee registration, employee addition, employee deletion, company budget for the company. Since it is a simple example, we will use a text document, not a database.

# We create budget.txt, employees.txt

class Company():
    def __init__(self, name):
        self.name = name
        self.work = True

    def program(self):
        selection = self.menuSelection()
        
        if selection == 1:
            self.addEmployee()
        elif selection == 2:
            self.quitEmployee()
        elif selection == 3:
            choice = input("Would you like to see salaries on an annual basis? (y/n)")
            if choice == "y":
                self.showSalary(calculation="y")
            else:
                self.showSalary()
        elif selection == 4:
            self.giveSalaries()

    def menuSelection(self):
        selection = int(input(
            "*** welcome to {} automation ****\n\n1-Add Employee\n2-Employee Interest\n3-Show Payable Salary\n4-Give Salaries\n\nEnter Your Choice:".format(self.name)))
        while selection < 1 or selection > 6:
            selection = int(input("Please enter one of the options 1-4."))
        return selection

    def addEmployee(self):
        eId = 1
        name = input("Enter Employee Name: ")
        surname = input("Enter Employee Surname: ")
        age = input("Enter Employee Age: ")
        gender = input("Enter Employee Gender: ")
        salary = input("Enter Employee Salary: ")

        with open("employees.txt","r") as employeesFile:
            employeesList = employeesFile.readlines()

        if len(employeesList) == 0:
            eId = 1
        else:
            with open("employees.txt","r") as employeesFile:
                eId = int(employeesFile.readlines()[-1].split(")")[0]) + 1

        with open("employees.txt","a+") as employeesFile:
            employeesFile.write("{}){}-{}-{}-{}-{}\n".format(eId,name,surname,age,gender,salary))


    def quitEmployee(self):
        with open("employees.txt","r") as employeesFile:
            employees = employeesFile.readlines()
            
        showEmployees = []
        
        for employee in employees:
            showEmployees.append(" ".join(employee[:-1].split("-")))
            
        for employee in showEmployees:
            print(employee)
            
        choice = int(input("Please enter the number of the employee you want to dismiss: 1-{}: ".format(len(showEmployees))))
        while choice < 1 or choice > len(showEmployees):
            choice = int(input("Please enter the number (1-{}): ".format(len(showEmployees))))
            
        employees.pop(choice - 1)
        
        counter = 1
        
        changingEmployees = []
        
        for employee in employees:
            changingEmployees.append(str(counter) + ")" + employee.split(")")[1])
            counter += 1
        
        with open("employees.txt","w") as employeesFile:
            employeesFile.writelines(changingEmployees)

    def showSalary(self, calculation="m"):
        """ calculation monthly if m, annual calculation if y """
        with open("employees.txt","r") as employeesFile:
            employees = employeesFile.readlines()
        
        salaries = []
        
        for employee in employees:
            salaries.append(int(employee.split("-")[-1]))
            
        if calculation == "m":
            print("Total salary to be paid this month: {} ".format(sum(salaries)))
        else:
            print("Total salary to be paid this month: {} ".format(sum(salaries)*12))

    def giveSalaries(self):
        with open("employees.txt","r") as employeesFile:
            employees = employeesFile.readlines()
        
        salaries = []
        
        for employee in employees:
            salaries.append(int(employee.split("-")[-1]))
            
        totalSalary = sum(salaries)
        
        with open("budget.txt","r") as employeesFile:
            totalBudget = int(employeesFile.readlines()[0])
            
        totalBudget = totalBudget - totalSalary
        
        with open("budget.txt","w") as employeesFile:
            employeesFile.write(str(totalBudget))

company = Company("My Company")
while company.work:
    company.program()
