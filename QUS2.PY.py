#We are using break point
av = 5
x = int(input("Enter the number of candy you want :"))
i = 1
while i<=x:

    if i>av:
        print("out of stock")
        break

    print("Candy")
    i = i+1

print("bye")

