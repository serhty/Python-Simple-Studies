# We will write a program to hire and manage company personnel. For simplicity, we will only handle personnel transactions. we will use "inheritance in classes" to not define information every time

class Employee():
    def __init__(self, name, surname, age, gender, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.salary = salary

    def getInfo(self):
        print("""
              {} {} info:
              Age: {}
              Gender: {}
              Salary: {}
              """.format(self.name, self.surname, self.age, self.gender, self.salary))

    def __str__(self):
        return """
              {} {} info:
              Age: {}
              Gender: {}
              Salary: {}
              """.format(self.name, self.surname, self.age, self.gender, self.salary)

class Manager(Employee): # The Employee class became a superclass of the Manager. we got the same structure from the Employee
    
    def __init__(self, name, surname, age, gender, salary):
        super().__init__(name, surname, age, gender, salary) #We take the values ​​that the Employee have.

    def salaryIncrease(self, eObject, increaseAmount=1000):
        eObject.salary += increaseAmount

employee = Employee("Name", "Surname", "22", "M", 2500)
print(employee)

manager = Manager("ManagerName", "ManagerSurname", "36", "M", 5500)
manager.salaryIncrease(employee)
employee.getInfo()
