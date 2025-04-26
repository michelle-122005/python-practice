st= input("Type a string: ")
ans=""
for i in range((len(st)-1),-1,-1):
    ans=ans+st[i]

print(ans)