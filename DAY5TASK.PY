# TASK 1

def create_user(name,age,roe) :
    return {"name" :name.title(), "age" :age, "role" :"role" }

user = [
    create_user("rohit", 25 , "designer"),
    create_user("dhoni" , 28 ,"python"),
    create_user("virat", 27 , "developer"),
    create_user("sachin" , 29 , "java")
    ]

for users in user :
    print(users)


# TASK 2

def calculate_total(*numbers) :
    total =sum(numbers)
    avg = total /len(numbers)
    return total, avg

total, avg = calculate_total(10,20,30,40,50,60,70,80)

print(f"cal_total : {total}")
print(f"ret_avg : {avg}")

# TASK 3

def system_config(**settings) :
    print("**** system configurtion ****")
    for key, value in settings.items() :
        print(f"{key} : {value}")
    print("---------------------")

system_config(
    mode = "debug",
    version = 1.0,
)

# TASK 4

def factorial(n) :
    if n<0 :
        return "error :negative number not allowed"
    elif n == 0 or n == 1:
        return 1
    else :
        return n * factorial(n-1)
    
print(factorial(5))
print(factorial(3))
print(factorial(0))
print(factorial(-3))

# TASK 5

def square_generator(n):
    for i in range(1, n+1):
        yield i * i
        

squares_list = [i*i for i in range (1,6)]
squares_gen = square_generator(5)

print(type(squares_list))
print(type(squares_gen))
print(list(squares_gen))

# TASK 6

try:
    numerator =int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print("result: ",result)

except ZeroDivisionError :
    print("Error: cannot divide by zero..!")
except ValueError :
    print("Error : invalid input")
finally :
    print("program completed")


# TASK 7

with open ("team_data.txt", "w") as file :
    file.write("name :sakthi, age : 26 ,role : developer\n")
    file.write("name : priya , age : 24, role : designer\n")

with open ("team_data.txt","r") as file :
    content = file.read()
    print(content)

print("file closed?",file.closed)