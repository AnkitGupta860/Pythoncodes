import string
import random
digit=string.digits
chars=string.ascii_letters
special_chars=string.punctuation
k=random.sample(chars,4)
I=random.sample(digit,4)
S=random.sample(special_chars,2)
print("".join(k+S+I))
