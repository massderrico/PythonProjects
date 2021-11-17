from airplane import Airplane

planesList = []

def addPlane(ID,passengerCount,priority, time):
    planesList.append(Airplane(ID,passengerCount, priority, time))
    student = 0
    for plane in planesList:
        student = plane
        print(student.getTime)

addPlane(96, 100, 0, 1440)




