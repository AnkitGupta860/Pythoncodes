import sys
sys.setrecursionlimit(2000)
print(sys.setrecursionlimit(2000))
i=0
def greet():
    global i
    print("hello",i)
    i+=1
    greet()

greet()