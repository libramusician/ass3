from hashlib import blake2b as blake


def verify(user_name, passwd: str):
    with open("passwd.txt", "r") as p:
        lines = p.readlines()
        for line in lines:
            # found the user
            words = line.split(":")
            if words[0] == user_name:
                salt = bytes.fromhex(words[1])
                # read recorded hash from file
                hash_r = words[2].strip()
                # calculate hash with salt and passwd
                hash_c = blake(salt=salt)
                hash_c.update(passwd.encode())
                hash_c = hash_c.hexdigest()
                if hash_r == hash_c:
                    return True
        return False


# print(verify("a", "123456As!"))
