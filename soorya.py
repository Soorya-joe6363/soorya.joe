# Task 1 
# print formatting

print("Hello world",end=" ")
print("welcome python")
print("Hello","world","welcome","python")
print("Laptop","Mouse","keyboard",sep=" | ")

# Task 2 
# variable 

name = "Ravi"
age = 22
city = "chennai"

print(name,age,city,sep="-")

# Task 3 
# multiple assignment 

name = "Meena"
age = 20 
student = True

name,age,student = "Meena",20,True

print("Multii assignment:-",name,age,student)

# Task 4
#  Indexing 

Word = "python"

print(Word[0])
print(Word[3])
print(Word[5])

# Task 5
#  Arithmetic operators

25 + 10
50 - 20
8 * 5
100 / 10
10 % 3 
2 ** 4
20 // 3 

print(25 + 10)
print(50 - 20)
print(8 * 5)
print(100 / 10)
print(10 % 3)
print(2 ** 4)
print(20 // 3)

# Task 6 
#  Bodmas Expression

3+2*5**2
3+2*25
3+50

print(3+50)

# Task 7 
#  Assignment Operator

num = 50 
num += 25

num += num
print(num)

num = 100
num /= 10 

print(num)

#  Task 8
#  Comparison operator 

10 > 5 
20 < 15 
5 == 5 
10 != 8
7 >= 7
6 <= 2 

print(10 > 5)
print(20 < 15)
print(5 == 5)
print(10 != 8)
print(7 >= 7)
print(6 <= 2)

# Task 9 
# string comparison 

a = "apple"
b = "Apple"

print("a:-",ord("a"))
print("A:-",ord("b")) 

print(a == b)

# Task 10 
# Logial operator

10<5 and 5==5
5>10 or 10==10
not 5>2

print(10>5 and 5==5)
print(5>10 or 10==10)
print(not(5>2))

# Task 11
#  Membership Operator

numbers = [10,20,30,40,50]

print(numbers)
print(20 in numbers)
print(60 in numbers)
print(30 not in numbers)

# Task 12
# Swap variable 

a = 10
b = 20 

a,b = b,a 

print(a,b)
print("a=",a)
print("b=",b)

# Task 13
# bitwise XOR

a = 6 
b = 3

print(a^b)