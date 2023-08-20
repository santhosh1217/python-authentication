table = {}

class User:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.status = False
    def checkPassword(self,password,confirmPassword):
        if password == confirmPassword:
            return True
        return False
    def login(self,username,password):
        self.username = username
        self.password = password
        self.status =True
        print("logining in",username)

    def signup(self):
        name = input("Username :")
        password = input("password :")
        confirmPassword = input("confirm password :")

        if (self.checkPassword(password,confirmPassword)):
            table[name] = self
            self.login(name , password)

        else:
            print("password not matched")
            print("try again")
            self.signup()

def get():
    for x,y in table.items():
        print("username :{} password :{} status :{}".format(x,y.password,y.status))

def signup():
    u = User()
    u.signup()
def logout():
    name = input("username : ")
    try:
        table[name].status = False
        print("loging out",name)

    except:
        print("username not found")
        
def login():
    username = input("username : ")
    password = input("password : ")

    try:
        if table[username].password == password:
            print("login sucessfully")
        else:
            print("password not matched")
    except:
        print("username not found")

while True:
    print("1, signup ")
    print("2, login ")
    print("3, select * from users ")
    print("4, exit ")
    print("5, logout ")

    choice = int(input("Enter your choice : "))
    try:
        if choice ==1:
            signup()
        elif choice ==2:
            login()
        elif choice ==3:
            get()
        elif choice ==4:
            break
        elif choice == 5:
            logout()
        else:
            print("invalid choice") 
    except:
        print("something went wrong")


    
    