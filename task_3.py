def fact(n):
    cur = 1
    for i in range(1, n+1):
        cur = cur * i
    return cur

num = int(input("Enter a number: "))
ans = fact(num)
print(f"{num}! is {ans}")