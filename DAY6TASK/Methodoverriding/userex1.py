class User :

    def register(self) :
        print("registred...")

    def login(self) :
        print("logined...")

class Student(User):
    def greet(self) :
        print("Welcome user")

class Faculty(User):
    def greet(self):
        print("Welcome Student")

class TempFaculty(Faculty):
    def greet(self) :
        print("Welcome Temp Faculty")