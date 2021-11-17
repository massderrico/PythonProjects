from student import Student

class School:
    def __init__(self, schoolName):
        self.schoolName = schoolName
        self.studentList = []
    def addStudent(self, ID:str, grades:list):
        stuID = Student(ID)
        for i in grades:
            stuID.addGrade(i)
        self.studentList.append(stuID)
    def highestStudent(self):
       highestGrade = 0
       bestStudentID = ""
       for student in self.studentList:
            if student.averageGrade() >= highestGrade:
                highestGrade = student.averageGrade()
                bestStudentID = student.studentID
       return(bestStudentID,highestGrade)



