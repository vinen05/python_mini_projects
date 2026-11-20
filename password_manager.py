from cryptography.fernet import Fernet
import os

def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key","rb") as key_file:
        key = key_file.read()
        return key

def view():
    key = load_key()
    fer = Fernet(key)
    with open("passwords.txt","r") as pwd_file:
        for line in pwd_file.readlines():
            data = line.rstrip()
            user,pwd = data.split("|")
            print("Account Name:",user,"\nPassword:",fer.decrypt(pwd.encode()).decode())

def add():
    key = load_key()
    fer = Fernet(key)
    name = input("Please enter your account name: ")
    pwd = input("Please enter your account password: ")

    with open("passwords.txt","a") as add_file:
        add_file.write(name+"|"+ fer.encrypt(pwd.encode()).decode() +"\n")

if not os.path.exists("key.key"):
    write_key()

if not os.path.exists("passwords.txt"):
    with open("passwords.txt","a") as file:
        file.write("")

while True:
    mode = input("Would you like to add a new password or view existing one's (view, add), press q to quit?")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Please enter either 'view' or 'add'")
        continue
