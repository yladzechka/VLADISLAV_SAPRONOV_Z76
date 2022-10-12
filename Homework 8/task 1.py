class Student:
    def __init__(self, firstName: str = "None", lastName: str = "None", groupNumber: str = "None", age: int = None):
        self.firstName = firstName
        self.lastName = lastName
        self.groupNumber = groupNumber
        self.age = age

    def getFullName(self):
        print(f"{self.firstName} {self.lastName}")

    def getAge(self):
        print(f"{self.firstName} {self.lastName}. Ему {self.age} года.")

    def GetGroupNumber(self):
        print(f"Это {self.firstName} {self.lastName}. Он в группе {self.groupNumber}.")

    def SetNameAge(self, firstName: str, lastName: str, groupNumber: str, age: int):
        self.firstName = firstName
        self.lastName = lastName
        self.groupNumber = groupNumber
        self.age = age

    def setGroupNumber(self, groupNumber: str):
        self.groupNumber = groupNumber

student_1 = Student("Vladislav", "Sapronov", "Z76", 22)
student_2 = Student("Vasya", "Pupkin", "Z76", 23)
student_3 = Student("Anton", "Romanovich", "Z76", 24)
student_4 = Student("Roman", "Vasilyev", "Z76", 34)
student_5 = Student("Vladimir", "Fedorov", "Z76", 32)

student_1.getFullName()
student_1.getAge()
student_1.GetGroupNumber()





