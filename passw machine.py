import random

passw = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

q = int(input("password length?:"))

g_password = "" 

for i in range(q):
    a = random.randint(0,len(passw)-1)
    c = passw[a]
    g_password += c  

print("Passw:", g_password)
