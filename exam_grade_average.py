# Finding the letter grade according to student information, midterm and final grades
# We will add 40% of the midterm exam score and 60% of the final exam score and give them letter by letter according to the average exam score.

info = input("Enter the student's first and last name: ")
visaExamScore = float(input("Enter the visa exam grade: "))
finalExamScore = float(input("Enter final exam grade: "))

averageScore = visaExamScore*0.4 + finalExamScore*0.6
letterGrade = ""

if averageScore >= 90:
    letterGrade = "AA"
elif averageScore >= 85:
    letterGrade = "BA"
elif averageScore >= 80:
    letterGrade = "BB"
elif averageScore >= 75:
    letterGrade = "CB"
elif averageScore >= 70:
    letterGrade = "CC"
elif averageScore >= 65:
    letterGrade = "DC"
elif averageScore >= 60:
    letterGrade = "DD"
else:
    letterGrade = "FF"

print("Student {} average grade point average {}, letter grade {}".format(info, averageScore,letterGrade))