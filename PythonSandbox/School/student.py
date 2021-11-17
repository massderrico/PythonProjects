
class Student:
    def __init__(self, studentID):
        self.studentID = str(studentID)
        self.gradesList = []

    def addGrade(self, n):
        self.gradesList.append(n)
    def averageGrade(self):
        return sum(self.gradesList)/len(self.gradesList)




