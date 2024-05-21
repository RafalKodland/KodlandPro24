import random 
sings = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lengh = int(input("długość hasła:"))
password = ""
for i  in range(lengh):
    password += sings[random.randint(0,len(sings))]  
print(password)
