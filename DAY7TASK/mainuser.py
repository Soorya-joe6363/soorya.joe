# task 1
# super() usage

class User :
    
    name = None
    id = None

    def __init__(self,name,id):
        self.name = name
        self.id = id

class Student(User) :

    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self) :
        return f"Student : {self.name}, ID : {self.id}, Dept : {self.dept}, Fees : {self.fees}"

class Faculty(User) :
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self) :
        return f"Faculty : {self.name}, ID : {self.id}, salary : {self.salary}"
    
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self) :
        return f"TempFaculty : {self.name}, ID : {self.id}, duration : {self.duration}"
    
# task 2
# abstraction

from abc import ABC, abstractmethod

class AbstractUser(ABC) :
    @abstractmethod
    def get_details(self) :
        pass

class User(AbstractUser) :
    def __init__(self, name ,id):
        self.name = name
        self.id = id


    def get_details(self):
        return f"UserName: {self.name}, ID: {self.id}"
    

class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees
        
    def get_details(self):
        return f"{super().get_details()}, Department: {self.dept}, Fees: {self.fees}"
    
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
        
    def get_details(self):
        return f"{super().get_details()}, Salary: {self.salary}"
    
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration
        
    def get_details(self):
        return f"{super().get_details()}, duration : {self.duration}"
    


# task 3
# sorting


# students.sort(key=lambda x: x.fees)
# facultys.sort(key=lambda x: x.salary)

# task 4
# map

# names = list(map(lambda s:s.name,Student))


# task 5
# use filter



# high_fee_students = list(filter(lambda s: int(s.fees) > 50000, Student))
# high_salary_faculty = list(filter(lambda f: int(f.salary) > 30000, Faculty))


# task 6
# reduce()

# total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
# total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

# Task 7

# higher oder function

def process_students(students, func):
    return list(map(func, students))