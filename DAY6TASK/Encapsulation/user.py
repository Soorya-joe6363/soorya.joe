class user :

    user_name : None
    pwd       : None

    def __init__(self,user_name,pwd):
        self.__user_name = user_name
        self.__pwd  = pwd


    def set_user(self,user_name,pwd) :
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self,user_name) :
        return self.__user_name
    
    def register(self) :
        print("Registering user : ", self.__user_name)

    def login(self) :
        print("logging in : " , self.__user_name)


