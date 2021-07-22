
n=int(input())
i=0
for i in range(n):
    for k in range(1,n-i):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()
for i in range(n,0,-1):
   for k in range(1,n-i+1):
      print(" ",end="")
   for j in range(1,2*i):
      print("*",end="")
   print()