from userexe3 import User,Student,Faculty

s1 = Student()
s1.set_user("alice","alice123").login().greet().register()

print("=====================")

f1 = Faculty()
f1.set_user("krish","krish563").login().greet().register()
f1.set_user("naveen","nv986").login().greet().register()

print("======================")

print("Total users created: ", User.users)






