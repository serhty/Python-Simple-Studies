# We are making a system that registers students, shows students, organizes students, and deletes students. The recorded information will be student name, faculty, department, number, status. Students will have unique IDs.

import sqlite3

class University:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.statu = True
        
        self.connectDB()
        
    def run(self):
        self.menu()
        
        choice = self.choice()
        
        if choice == 1:
            self.addStudent()
        if choice == 2:
            self.deleteStudent()
        if choice == 3:
            self.updateStudent()
        if choice == 4:
            while True:
                try:
                    orderBy = int(input("1)All\n2)Faculty\n3)Department\n4)Status\n Select: "))
                    if orderBy < 1 or orderBy > 4:
                        continue
                    break
                except ValueError:
                    print("Must be integer")
            
            self.showAllStudents(orderBy)
        if choice == 5:
            pass
    
    def menu(self):
        print("*** {} Admin System ***".format(self.name))
        print("\n1)Add Student\n2)Delete Student\n3)Update Student\n4)Show All Student\n5)Exit\n")
        
    def choice(self):
        while True:
            try:
                process = int(input("Select: "))
                if process < 1 or process > 5:
                    print("Select must be between 1-5: ")
                    continue
                
                break
            except ValueError:
                print("Select must be integer!")
                
        return process
    
    def addStudent(self):
        print("*** Student Infos: ***")
        stid = input("StudentID: ")
        name = input("Name: ").lower().capitalize()
        faculty = input("Faculty: ").lower().capitalize()
        department = input("Department: ").lower().capitalize()
        status = "Active"
        
        self.cursor.execute("INSERT INTO students VALUES('{}','{}','{}','{}','{}')".format(stid, name, faculty, department, status))
        
        self.connect.commit()
        print("Student {} added".format(name))
    
    def deleteStudent(self):
        self.cursor.execute("SELECT * FROM students")
        allStudents = self.cursor.fetchall()
        convertAllString = lambda x: [str(y) for y in x]
        
        for i,j in enumerate(allStudents,1):
            print("{}) {} ".format(i," ".join(convertAllString(j))))
            
        while True:
            try:
                select = int(input("Select the student to be deleted: "))
                break
            except ValueError:
                print("Please enter type integer")
        
        self.cursor.execute("DELETE FROM students WHERE rowid={}".format(select))
        self.connect.commit()
        print("\nStudent deleted.")
    
    def updateStudent(self):
        self.cursor.execute("SELECT * FROM students")
        allStudents = self.cursor.fetchall()
        convertAllString = lambda x: [str(y) for y in x]
        
        for i,j in enumerate(allStudents,1):
            print("{}) {} ".format(i," ".join(convertAllString(j))))
            
        while True:
            try:
                select = int(input("Select the student to be update: "))
                break
            except ValueError:
                print("Please enter type integer")
                
        while True:
            try:
                updateSelect = int(input("1)StudentID\n2)name\n3)faculty\n4)department\n5)status"))
                if updateSelect < 1 or updateSelect > 7:
                    continue
                break
            except ValueError:
                print("Please enter integer")
        
        operations = ["studentid","name","faculty","department","status"]
                
        newValue = input("Enter new value: ")
        self.cursor.execute("UPDATE students SET {}='{}' WHERE rowid={}".format(operations[updateSelect-1], newValue, select))
        self.connect.commit()
        print("Student Updated")
    
    def showAllStudents(self, by):
        if by == 1:
            self.cursor.execute("SELECT * FROM students")
            allStudents = self.cursor.fetchall()
            convertAllString = lambda x: [str(y) for y in x]
            for i,j in enumerate(allStudents,1):
                print("{}) {} ".format(i," ".join(convertAllString(j))))
                
        if by == 2:
            self.cursor.execute("SELECT faculty FROM students")
            faculties = list(enumerate(list(set(self.cursor.fetchall())),1))
            
            for i,j in faculties:
                print("{}) {} ".format(i,j[0]))
                
            while True:
                try:
                    select = int(input("\nSelect: "))
                    break
                except ValueError:
                    print("Enter integer")
                
        self.cursor.execute("SELECT * FROM students WHERE faculty='{}'".format(faculties[select-1][1][0]))
        allStudents = self.cursor.fetchall()
        convertAllString = lambda x: [str(y) for y in x]
        for i,j in enumerate(allStudents,1):
            print("{}) {} ".format(i," ".join(convertAllString(j))))
            
        if by == 3:
            self.cursor.execute("SELECT department FROM students")
            departments = list(enumerate(list(set(self.cursor.fetchall())),1))
            
            for i,j in departments:
                print("{}) {} ".format(i,j[0]))
                
            while True:
                try:
                    select = int(input("\nSelect: "))
                    break
                except ValueError:
                    print("Enter integer")
                
        self.cursor.execute("SELECT * FROM students WHERE department='{}'".format(departments[select-1][1][0]))
        allStudents = self.cursor.fetchall()
        convertAllString = lambda x: [str(y) for y in x]
        for i,j in enumerate(allStudents,1):
            print("{}) {} ".format(i," ".join(convertAllString(j))))
            
        if by == 4:
            self.cursor.execute("SELECT status FROM students")
            statuses = list(enumerate(list(set(self.cursor.fetchall())),1))
            
            for i,j in statuses:
                print("{}) {} ".format(i,j[0]))
                
            while True:
                try:
                    select = int(input("\nSelect: "))
                    break
                except ValueError:
                    print("Enter integer")
                
        self.cursor.execute("SELECT * FROM students WHERE status='{}'".format(statuses[select-1][1][0]))
        allStudents = self.cursor.fetchall()
        convertAllString = lambda x: [str(y) for y in x]
        for i,j in enumerate(allStudents,1):
            print("{}) {} ".format(i," ".join(convertAllString(j))))
    
    def systemExit(self):
        self.statu = False
    
    def connectDB(self):
        self.connect = sqlite3.connect("university1.db")
        self.cursor = self.connect.cursor()
        
        self.cursor.execute("CREATE TABLE IF NOT EXISTS students(stid TEXT, name TEXT, faculty TEXT, department TEXT, status TEXT)")
        
        self.connect.commit()
        
university1 = University("University Name 1", "Country 1")
while university1.statu:
    university1.run()