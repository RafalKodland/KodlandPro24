import random 

def gen_pass(length):
    sings = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i  in range(length):
        password += sings[random.randint(0,len(sings))]

    return password
