import pymongo

#Database Connection with mongodb
client = pymongo.MongoClient('localhost',27017)
db = client.user_details_python
N=int(input("Enter the number of users : "))
username_list = []
for users in range(N):
    name = input("Enter name:")
    age = int(input("Enter age:"))
    while len(username_list) == len(set(username_list)):
        username = input("Enter a username:")
        if username not in username_list:
            username_list.append(username)
            break
        else:
            print("username already exists try new:")
    email = input("Enter your email address: ")
    while "@" not in email:
        email = input("Please write your email address again: ")
    while "." not in email:
        email = input("Please write your email address again: ")
    password = input("Enter password:")
    specialsymbol =['$', '@', '#', '%']
    VALUE = True
    if len(password) < 8:
        print('length should be at least 8')
        VALUE = False
        password = input("Enter password:")
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        VALUE = False
        password = input("Enter password:")
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        VALUE = False
        password = input("Enter password:")
    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        VALUE = False
        password = input("Enter password:")
    if not any(char in specialsymbol for char in password):
        print('Password should have at least one of the symbols $@#')
        VALUE = False
        password = input("Enter password:")
    confirm_password = input("Enter password again to confirm:")
    if confirm_password == password:
        print()
    else:
        password = input("Password doesn't match try again:")
    user = {"Name":name,"Age":age,"UserName":username,"Email":email,"Password":password,"cPassword":confirm_password}
    db.members.insert_one(user)
    print(user)
    
