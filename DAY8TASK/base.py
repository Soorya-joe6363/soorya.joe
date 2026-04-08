from task8 import User,Expence
# create user

user1 = User("surya")
user1.add_user()
user1.show_details()

uid = user1.user_id

# add expenses

exp1 =Expence("surya", uid, 250, "Food", "Dinner","2026-04-04")
exp2 =Expence("surya", uid, 1000, "Travel", "Bike petrol","2026-04-05")
exp3 =Expence("surya", uid, 1500, "Shopping", "Shirts","2026-04-06")
exp4 =Expence("surya", uid, 400, "movie", "movie ticket","2026-04-05")
exp5 =Expence("surya", uid, 600,  "Fitness", "GYM fees","2026-04-07")

exp1.add_expense()
exp2.add_expense()
exp3.add_expense()
exp4.add_expense()
exp5.add_expense()

# view expenses

exp1.view_expense()


# filter expenses

records =exp1.get_expense()


exp1.filter_by_category(records,"Food")
exp1.filter_by_date(records, "2026-04-07")
exp1.total_expense(records)
exp1.category_wise(records)

print("------------------------------")

exp2.filter_by_category(records,"Travel")
exp2.filter_by_date(records, "2026-04-05")
exp2.total_expense(records)
exp2.category_wise(records)

print("------------------------------")

exp1.monthly_report(records)

print("-------------------------")

exp1.highest_expense(records)

print("-------------------------")

exp1.smart_insight(records)


