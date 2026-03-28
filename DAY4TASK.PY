# EMPLOYEE MANAGEMENT SYSTEM
# mini project 1

EMPLOYEES = []

user = {"name": "ragul", "age" : 25, "role" : "developer" , "salary": 50000}
user1 = {"name": "sathish", "age" : 29, "role" : "manager" , "salary": 55000}
EMPLOYEES.append(user)
print(EMPLOYEES)
EMPLOYEES.append(user1)
print(EMPLOYEES)

def add_employee (name, age, role , salary) :
    EMPLOYEES.append({"name": name, "age" : age, "role" : role , "salary": salary})
add_employee ("ragul",25,"developer",5000)
print(EMPLOYEES)

def update_employee(name,key,value) :
    for emp in EMPLOYEES :
        if emp["name"]== "ramesh" :
            emp[key]= value
update_employee("name", "",70000)
print(EMPLOYEES)

# mini project 2
def report():
    name = input("Name: ")
    sub1 = int(input("English: "))
    sub2 = int(input("Maths: "))
    sub3 = int(input("Science: "))
    
    total = sub1 + sub2 + sub3
    avg = total / 3
    
    grade = "A+" if avg >= 90 else "A" if avg >= 80 else "B+" if avg >= 70 else "B" if avg >=40 else "failed"
    
    print(f"{name} | Total: {total} | Avg: {avg:.2f} | Grade: {grade}")

report()


# mini project 3

cart = [
    {"name": "headphone", "price": 5000, "qty": 2},
    {"name": "powerbank", "price": 1500, "qty": 1}
]

cart.append({"name": "charger", "price": 1000, "qty": 1})

for product in cart:
    if product["name"] == "powerbank":
        cart.remove(product)

total = 0
print("Cart product:\n")

for product in cart:
    product_total = product["price"] * product["qty"]
    total += product_total
    print(f"{product['name']} - {product['price']} x {product['qty']} = {product_total}")

print("\nTotal Bill:", total)

# mini project 4

user ={"admin" : "89733","priya" : "priya@89733"}
username = input("username : ")
password = input("password: ")
print(user)

if username in user :
    if user[username] == password :
        print("login successfully...!,",username)
    else :
        print("incorrent password")
else :
    print("username not found")

       
# mini project 5

visitor_name = {"santhosh","karthik","rangesh"}
print(visitor_name)

visitor_name1 ={"santhosh","karthik","rangesh","santhosh","praveen"}
print(visitor_name1)

print("unique visitor_name :",len(visitor_name))
print("unique visitor_name1 :",len(visitor_name1))

# mini project 6

name = "kumar"
product = "laptop"
product1 = "mouse"
print(name + " brought " + product + " and " + product1)

text = "{ } brought { } and { }"


text = "{kumar} brought {laptop} and {mouse}"
print(text)

msg = "welcome"
print("****{}****".format(msg))
print("****{msg:<10}****".format(msg="welcome"))
print("****{msg:>10}****".format(msg="welcome"))
print("****{msg:^11}****".format(msg="welcome"))

# mini project 7

accounts = {}
name = "harish"
amount = 50000

def create_account(name, balance=0):
    accounts[name] = balance
    
def deposit(name, amount):
    accounts[name] += amount

def withdraw(name, amount):
    if accounts[name] >= amount:
        accounts[name] -= amount
    else:
        print("Insufficient balance")

def check_balance(name):
    print(f"{name}'s Balance: {accounts[name]}")


create_account(name,amount)
deposit(name,1400)
withdraw(name,1000)

print(accounts)



# mini project 8

votes =[]

votes = {"Andy" : 0, "brain" : 0, "carlien" : 0}

votes["Andy"] += 1
votes["brain"] += 1
votes["carlien"] += 1
votes["Andy"] += 1
votes["brain"] += 1

print("votes:")
for name in votes :
    print(name, ":", votes[name])

winner =max(votes, key=votes.get)
print("winner is:",winner)

# mini project 9

enrollments =[]

student = {"name": "pradeep","course": "business analyst"}
for key,val in student.items() :
    enrollments.append(student)
    print(key,val,sep= " : ")

student1 ={"name": "kesavan","course": "python"}
enrollments.append(student1)
print(enrollments)

#  update

student["name"] ="aashif"
print(student)


# mini project 10

num = 1001
print("binary value :- {:b}".format(num))
print("octal value :- {:o}".format(num))
print("hex value :- {:x}".format(num))
print("scientific value :- {:e}".format(num))

money =50000000
print("hve money {:,}".format(money))



