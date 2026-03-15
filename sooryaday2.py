 # 1 
a = 10 
b = 6 
print(a & b)

# 2

X = 12 
Y = 5 
print(12 | 5) 

# 3 

num = 8 
print( ~num )

# 4

a = 15 
b = 9 
print(a ^ b)

#  5

num = 7 
print(7 << 2)

# 6 

num = 20 
print(20 >> 1) 

# 7
a = int(input("Enter the number :- "))
b = int(input("Enter the number :- "))
print(a & b)

# 8 
a = int(input("enter first number:- "))
b = int(input("enter second number:- "))
print(a ^ b)

# string task 
# 9

a = "Hi"
print(a * 4)

# 10

a = "python"
print(a * 3)

# 11

a = "super"
b = "mam"
print(a + b)

# 12

a = "hello"
b = "world"
print(a + " " + b)

# example

a = "hello"
b = "world"
c = " "
print(a + c + b)

# 13

a = input("enter the name:-")
print(a * 5 )

# 14

a = input("enter first name:- ")
b = input("enter second name:- ")
print(a + b)

# 15

name = input("enter your name:- ")
print(type(name))

# 16

age = int(input("enter your age:- "))
print(type(age))

# 17

sum1 = int(input("enter your num:- "))
sum2 = int(input("enter your num:- "))
print("total", sum1 + sum2)

# 18

num1 = int(input("enter your mark science:- "))
num2 = int(input("enter your mark social:- "))
avg =(sum1 + sum2)/2
print("average=",avg)

# 19

a=int(input("enter first number:- "))
b=int(input("enter second number:- "))

print(3*a*2+b-2)


# 20
str1 = input("enter a number:- ")
print(type(str1))

str1 = int(str1)
print(type(str1))

# 21
num = input("Enter a number:- ")
print( num[-1])

# 22
num = int(input("Enter a number:- "))
print("Unit digit =", num % 10)

# 23
num = int(input("Enter a number: "))
print("Number without last digit = ", num // 10)

# 24
Seclastdigit = 8595
print((Seclastdigit // 10 ) % 10) 

# 25

num =int(input("enter number:- "))
print((num % 10))

# 26
if (10>=5) :
    print("now i thick condition true")

# 27
if(60>50) :
    print("yes,its True")

# 29
str1 = 120
if(str1 > 120 and str1 <100) :
    print("yes,number is greater than 100")
else :
    print("no,smaller than 100")    

# 28
age>=18

if(age>=18 and age <=18) :
    print("yes,True")
else :
    print("No,false")


# 35

Age = int(input("Enter your Age:- "))
height = int(input("Enter your height:- "))
weight = int(input("Enter your Weight:- "))

if Age >= 18:
    if height >= 160:
        if weight >= 60:
            print(name,"Congratulation your Selected for this job")
        else:
            print("name,your weight is not eligible for this job")
    else:
        print(name,"your height is not eligible for this job")        
else:
    print(name,"your age is not eligible for this job")

# 36
Marks = int(input("Enter your Marks:- "))
age = int(input("Enter your Age:- "))
if Marks >= 60:
    if age >= 17:
        print("Admission Granted")
    else:
        print("Admission canceled because of age")
else:
    print("Admission canceled because of marks")

# 37
Age = int(input("Enter your Age:- "))
height = int(input("Enter your height:- "))
weight = int(input("Enter your Weight:- "))

if Age >= 16:
    if height >= 150:
        if weight >= 50:
            print(name,"Congratulation your Selected")
        else:
            print("name,your weight is not eligible")
    else:
        print(name,"your height is not eligible")        
else:
    print(name,"your age is not eligible")
# 38
days = int(input("Enter the number 1 - 7:- "))
match days:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
# 39
color = int(input("Enter number between 1 - 3:- "))
match color:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")

# 40
Fruit = int(input("Enter number between 1 - 4:- "))
match Fruit:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")
