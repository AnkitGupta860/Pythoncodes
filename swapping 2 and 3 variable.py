n=int(input())
for i in range(n+1):
    d=0
    arm=0
    t1=i
    t2=i
    while t1>0:
        p=t1%10
        d+=1
        t1//=10
    while t2>0:
        rem=t2%10
        arm+=rem**d
        t2//=10
if arm==i:
    print("armstrong")
else:
    print("not armstrong")

