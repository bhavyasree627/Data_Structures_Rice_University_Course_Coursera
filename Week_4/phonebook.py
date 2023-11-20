n=int(input())
ans=[]
hash={}
for i in range(n):
    li=list(map(str,input().split()))
    if li[0]=="add":
        hash[li[1]]=li[2]
    elif li[0]=="find":
        if li[1] in hash:
            ans.append(hash[li[1]])
        else:
            ans.append("not found")
    else:
        if li[1] in hash:
            del hash[li[1]]
for i in ans:
    print(i)
        