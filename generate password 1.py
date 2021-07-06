import random
chars="abcdefghijklmnopqrstuvwxyz"
pass_len=int(input())
k = random.sample(chars, pass_len)
print("".join(k))