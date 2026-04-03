from mainuser import User,Student,Faculty,TempFaculty

# task 1

students = [
    Student("sathish", 101, "CSE",60000),
    Student("santhosh", 102, "EEE", 55000),
    Student("pradeep", 103, "AE", 65000)
    ]

for s in students :
    print(s.get_details())

facultys = [
    Faculty("kesavan", 110, 50000),
    Faculty("aashif", 111, 45000),
    Faculty("dilip", 112, 55000)
]

for f in facultys :
    print(f.get_details())

tempfacultys = [
    TempFaculty("karthik", 120, 45000, "6 months" ),
    TempFaculty("ramesh", 121, 45000, "6 months" ),
    TempFaculty("suresh", 122, 45000, "6 months" )
]

for t in tempfacultys :
    print(t.get_details())

# task 2
from mainuser import AbstractUser,User,Student,Faculty,TempFaculty

students1 = Student("krish", 201, "MECH",60000)
facultys1 = Faculty("jack", 211,30000)
tempfacultys1 = TempFaculty("rakesh", 221, 45000, "3 months")


print(students1.get_details())
print(facultys1.get_details())
print(tempfacultys1.get_details())


# task 3

# sorting by fees
students.sort(key=lambda x: x.fees)
facultys.sort(key=lambda x: x.salary)
print("\n-------sorted students fees--------")
for s in students :
    
    print(s.get_details())

print("\n----------sorted Faculty salary------")

for f in facultys:
    print(f.get_details())

# task 4
names =list(map(lambda s:s.name,students))

print("Student Name : ",names)

depts =list(map(lambda s:s.dept,students))

print("Department Name: ",depts)

# task 5

high_fee_students = list(filter(lambda s: s.fees > 55000,students))

print("-------high student fees > 55000------")
for s in high_fee_students:
    print(s.get_details())


high_salary_faculty = list(filter(lambda f: f.salary > 45000, facultys))

print ("-------high faculty salary fees > 45000------")
for f in high_salary_faculty :
    print(f.get_details())

# task 6

from functools import reduce

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary =reduce(lambda acc, f: acc + f.salary, facultys, 0)

print("Total fees of students: ",total_fees)
print("total salary of facultys: ",total_salary)

# task 7

from mainuser import process_students

print("--------------------------------------")
names = process_students(students,lambda s:s.name.upper())
print("student name: ",names)

print("-----------------------------------")