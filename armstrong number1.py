n=int(input())
for i in range(100,n+1):
    d=0
    while i>0:
           p=i%10
           d=d+1
           i=i//10
           for j in range(100,n+1):
                arm=0
                t=j
                while j>0:
                   rem=j%10
                   arm=arm+rem**d
                   j=j//10
                   if t==arm:
                        print(arm)
                   else:
                        print("not armstrong")
