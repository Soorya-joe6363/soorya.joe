# loop basics
# 1 loop 1 to 50
for i in range(1,51):
    print(i)

# 2 even number 1 to 100
for i in range(2,101,2):
    print(i)

# 3 odd number 1 to 100
for i in range(1,101,2):
    print(i)

# 4 multiple table 7
for i in range(1,11):
    print(f"7*{i} ={7*i}")

for i in range(7,71,7):
    print(i)

# 5 sum number 1 to 100
total = 0 
for i in range(1,101):
    total += i
    print(total)

# 6 reverse print 50 to 1
for i in range(50,0,-1):
    print(i)

# 7 count number divisible 3(1-100)
count = 0
for i in range(1,101):
    if i % 3 == 0:
        count += 1
print(count)

# 8 squares 1 to 10
for i in range(1,11):
    print(i*i)

# 9 cube first 10 numbers
for i in range(1,6):
    print(i**3)

# 10 n = 8
n = 8 
for i in range(i,n+1):
    print(i)

# while loop
# 11 while using 1 to 20

i = 1
while i <=20 :
    i += 1
    print(i)

# 12 factorial number 
n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i+=1
print(fact)

# 13 reverse number
num = 54321
rev = 0
while num > 0:
    rev= rev*10 + num % 10
    num //= 10
print(rev)

# 14 count
num = 654321
count = 0
while num > 0 :
    count+=1
    num//=10
print(count)

# 15
list =[]
while "true":
    input1 = input("enter value:- ")
    if input1 == "stop" :
        break
    num.append(int(input1))

print(num)

# nested loop
16 
for i in range(1 , 5):
    print("*" * i)


# string basic
# 21  
name = "gaming"
print(len(name))


# 24 
name = "gaming"
print(name[ : : -1])

# 25
name = "madam"
print(name[ : :-1])


# string sliceing
# 26
name = "welcometomyworld"

x = slice(0,6)
print(name[x])

# 27
y = slice(13,16)
print(name[y])

# 28
z = slice(0,-1)
print(name[ : :-1])

# 29
print(name[ : :2])

# 30
print(name[1:-1])


# list operations
# 31
list = [1 , 2 , 3 , 4]
print(sum(list)) 

# 32
list = [1,2,3,4,5,6]
print(max(list))

# 33
list = [1,2,3,4,5,6]
print(min(list))

# 34 
list = [1,2,3,4,5,6]
print(len(list))

# 35
list = [1,2,3,4,5,6]
print(3 in list)

# 36 dd 3 element using append()

bikes = ["tvs","honda","suzuki"]
print(bikes)
print(bikes[2])

bikes.append("yamaha")
print(bikes)

# 37 insert 
bikes.insert(2,"triumph")
print(bikes)

# 38 remove()
bikes.remove("suzuki")
print(bikes)

# 39 reverse ()
bikes.reverse()
print(bikes)

# 40 sort()
bikes.sort()
print(bikes)



