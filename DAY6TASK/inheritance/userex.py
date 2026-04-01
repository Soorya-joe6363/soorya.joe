class User :

    def register(self) :
        print("register....")

    def login(self) :
        print("login...")


class Student(User) :
    def student_greet(self) :
        print("Hello Student")

class Faculty(User):
    def faculty_greet(self) :
        print("Hello Faculty")

class TempFaculty(Faculty) :
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")