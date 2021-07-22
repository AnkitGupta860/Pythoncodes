import string
digit=string.digits
special_chars=string.punctuation
vowel_count=0
Digit_count=0
a=input()
a=a.lower()
i=0
while i<=len(str):
    if str[i] in special_chars:
        break
    elif str[i] in ('a','e','i','o','u'):
        vowel_count+=1
    elif str[i] in digit:
        Digit_count+=1
print(vowel_count)
print(Digit_count)






