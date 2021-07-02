str=input()
lst=[]
for x in str.split(','):
    print(x)
    y=x.split('=')
    print(y)
    lst.append(y)
print(lst)
d=dict(lst)
d1={}
for k,v in d.items():
    d1[k]=int(v)
print(d1)

