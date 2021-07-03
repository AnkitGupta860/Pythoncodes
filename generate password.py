import random
chars="abcdefghijklmnopqrstuvwxyz"
while 1:
    pass_len=int(input("length of password :"))
    pass_count=int(input("how many times you want password :"))
    for x in range(pass_count):
        password = ""
        for x in range(0,pass_len):
             k=random.choice(chars)
             password += k


    print("Here is your password :",password)









