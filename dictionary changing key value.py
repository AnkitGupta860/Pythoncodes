n = eval(input())
dict = {"vijay":5}
for k,v in n.items():
    if v in dict:
        dict[v].append(k)
    else:
        dict[v]= k

print(dict)