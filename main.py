#! /bin/python3.10
from question1 import *
from passwdVerify import verify

# default value for testing purpose only. assumption
TIME = 10
APPROVED = True

while True:
    print("Finvest Holdings")
    print("Client Holdings and Information System")
    print("----------------------------------------------------")
    user_name = input("Enter username:")
    passwd = input("Enter password:")
    if not verify(user_name, passwd):
        print("authentication failed, exit")
        exit(1)
    print("ACCESS GRANTED")
    print("your role is " + role(user_name) + "your ID is " + id(user_name))
    files_viewable = []
    files_modifiable = []
    files_accessible = []
    for file in VFS:
        if can_view(user_name, file, TIME):
            files_viewable.append(file)
        if can_modify(user_name, file):
            files_modifiable.append(file)
        if can_access(user_name, file, APPROVED):
            files_accessible.append(file)
    if len(files_viewable) > 0:
        print("you can view:")
        for item in files_viewable:
            print(item)
    if len(files_modifiable) > 0:
        print("\nyou can modify:")
        for item in files_modifiable:
            print(item)
    if len(files_accessible) > 0:
        print("\nyou can access:")
        for item in files_accessible:
            print(item)

    while True:
        command = input("Enter q to quit or enter s to switch user\n")
        if command == "q":
            exit(0)
        elif command == "s":
            break
        else:
            print("command not recognized, try again\n")
