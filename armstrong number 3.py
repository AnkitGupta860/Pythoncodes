n=int(input())
for i in range(100,n+1):
    d=0
    arm=0
    t1=i
    t2=i
    while t1>0:
           p=t1%10
           d=d+1
           t1=t1//10
    while t2>0:
        rem=t2%10
        arm=arm+rem**d
        t2=t2//10
    if arm==i:
      print(arm)



