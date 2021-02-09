for i in range(100,1000):
    arm=0
    while i>0:
        rem=i%10
        arm=arm+rem**3
        i=i//10
    print(arm)