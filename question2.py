import os
from hashlib import blake2b as blake


def add_usr(user_name, passwd):
    b_passwd = passwd.encode()
    r_salt = os.urandom(blake.SALT_SIZE)
    hash_user = blake(salt=r_salt)
    hash_user.update(b_passwd)
    with open("passwd.txt", "a") as file:
        file.write(user_name + ":" + r_salt.hex() + ":" + hash_user.hexdigest() + "\n")


def passwd_f_test():
    add_usr("abc", "123")
    add_usr("bcd", "123")
