import mysql.connector
from functools import reduce   

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ssoorya@15",
    port=3306,
    database="expense_db"
)

print("connection sucessfully...!")
cursor=conn.cursor()

from abc import ABC, abstractmethod

class AbstractUser(ABC) :
    @abstractmethod
    def show_details(self) :
        pass

class User:
    def __init__(self,name):
        self.__name = name
        self.user_id = None

    def get_names(self) :
        return self.__name
    
    def add_user(self):
        cursor.execute("INSERT INTO users (name) VALUES (%s)",(self.__name,))
        conn.commit()
        self.user_id =cursor.lastrowid
        print("User added successfully...!")

    def show_details(self) :
        print("User name: ",self.__name)
        print("User id: ",self.user_id)

class Expence(User):
    def __init__(self,name, user_id,amount,category,descripition,date):
        super().__init__(name)
        self.user_id = user_id
        self.amount =amount
        self.category =category
        self.descripition =descripition
        self.date = date


    def add_expense(self):
        cursor.execute("""INSERT INTO expenses (user_id,amount,category,descripition,date) VALUES(%s, %s, %s, %s, %s)""",(self.user_id, self.amount, self.category, self.descripition, self.date))
        conn.commit()
        print("Expense added successfully...!")

    def show_details(self):
        print("===========details==========")
        print("Expense Details: ")
        print("Name: ",self.get_names())
        print("User id: ",self.user_id)
        print("Amount: ",self.amount)
        print("Category: ",self.category) 
        print("Descripition: ",self.descripition)
        print("Date: ",self.date)
        print("============================")

    def get_expense(self):
        cursor.execute("""SELECT u.user_id, u.name, e.amount, e.category, e.descripition, e.date
        FROM users u JOIN expenses e ON u.user_id =e.user_id WHERE u.user_id =%s """,(self.user_id,))
        return cursor.fetchall()
        
    
    
    def view_expense(self):
        record_data =self.get_expense()

        print("\n========ALL EXPENSES========")
        if record_data:
            print("row in data records....")
        else:
            print("not found details....")
            return record_data
        
    def filter_by_category(self, record_data, category_name) :
        result = list(filter(lambda x : x[3] == category_name,record_data))

        print("\n------filter by category--------")
        if result :
            for row in result:
                print(row)
        else:
            print("category not found")
        return result
    
    

    
    def filter_by_date(self, record_data, exp_date) :
        result = [rec for rec in record_data if str(rec[5])== exp_date]

        print("\n-------filter by date----------")
        if result:
            for row in result:
                print(row)
        else:
            print("date not found")    
        return result

    

    def total_expense(self, record_data) :
        amounts = list(map(lambda x: x[2],record_data))
        total = reduce(lambda a,b :a+b, amounts, 0)
       
        print("total expense: ",total)
        return total


    def category_wise(self, record_data) :
        category1 ={x[3] for x in record_data}
        result = {cat : sum([x[2] for x in record_data if x[3] ==cat]) for cat in category1}
        print("\n===category wise spend========")
        for key,val in result.items():
            print(key, ":", val)
        return result


    def delete_expense(self, exp_id) :
        cursor.execute("DELETE FROM expenses WHERE exp_id=%s", (exp_id,))
        conn.commit()

        print("expense deleted")

    def update_expense(self, exp_id, amount):
        cursor.execute("UPDATE expenses SET amount=%s WHERE exp_id=%s",(amount, exp_id))
        conn.commit()

        print("expense updated")

    
# MONTHLY REPORT
    def monthly_report(self, record_data):
        report = {}
        for x in record_data:
            month = x[5].strftime("%Y-%m")
            report[month] = report.get(month, 0) + x[2]

        print("\nMonthly Report:")
        for key, val in report.items():
            print(key, ":", val)
            return report

    def highest_expense(self, record_data):
        high_exp = reduce(lambda x, y: x if x[1] > y[1] else y, record_data)
        print("Highest Expense:", high_exp)


    def smart_insight(self, record_data):
        category1 = {x[3] for x in record_data}
        result = {cat: sum([x[2] for x in record_data if x[3] == cat]) for cat in category1}
        max_cat = max(result, key=result.get)

        print(f" You are spending too much on {max_cat}....!")
        return result
