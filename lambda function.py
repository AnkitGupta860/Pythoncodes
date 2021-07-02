from functools import reduce
nums = list(map(int,input().split()))
evens = list(filter(lambda n: n%2 == 0 , nums))
doubles = list(map(lambda n: n*2 , evens))
print(doubles)
sum = reduce(lambda a,b:a+b,doubles)
print(sum)
