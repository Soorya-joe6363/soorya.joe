class User :

    users = 0

    def __init__(self):
        self.__user_name = None
        self.__pwd  = None
        User.users += 1


    def set_user(self,user_name,pwd) :
        self.__user_name = user_name
        self.__pwd = pwd
        return self

    def get_user(self,user_name) :
        return self.__user_name
    
    def register(self) :
        print("registering user : ",self.__user_name)
        return self
    
    def login(self):
        print("logging in : " , self.__user_name)
        return self

    def greet(self) :
        print("Welcome user")
        return self

class Student(User) :
    def greet(self):
        print("Welcome Student")
        return self

class Faculty(User) :
    def greet(self) :
        print("Welcome Faculty")
        return self
    

        

        
