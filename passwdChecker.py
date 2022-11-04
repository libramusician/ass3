weak_passwds = ["Password1", "Qwerty123", "20210203"]


def passwd_check(user_name, password):

    lowercase = False
    uppercase = False
    num = False
    special = False

    if not (8<= len(password) <=12):
        print("your password need to be 8-12 characters")
        return False

    if password == user_name:
        print("can not have password same as user name")
        return False

    if password in weak_passwds:
        print("your pass word is common weak or matching the format of calendar dates, license plate numbers, telephone numbers")
        return False

    for character in password:
        if character in "abcdefghijklmnopqrstuvwxyz":
            lowercase = True
        if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uppercase = True
        if character in "0123456789":
            num = True
        if character in "!@#$%?*":
            special = True

    if not lowercase:
        print("Your password should contains lowercase characters.")
        return False

    if not uppercase:
        print("Your password should contains uppercase characters.")
        return False

    if not num:
        print("Your password should contains digits.")
        return False

    if not special:
        print("Your password should contains special character.")
        return False
    return True


# passwd_check("abc", "123456")