#! /bin/python3.10
from passwdChecker import passwd_check
from question2 import add_usr


def add_role(user_name, role, id):
    with open("role.txt", "a") as r:
        r.write(user_name + ":" + role + ":" + id + "\n")



while True:
    user_name = input("type a user name\n")
    passwd = input("type a password\n")
    if passwd_check(user_name, passwd):
        role = input("what is your role?")
        id = input("what is your ID?")
        add_usr(user_name, passwd)
        add_role(user_name, role, id)
        print("user added")
    else:
        print("unsuccessful")


    while True:
        command = input("Enter q to quit or enter n to add user\n")
        if command == "q":
            exit(0)
        elif command == "n":
            break
        else:
            print("command not recognized, try again\n")