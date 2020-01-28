n=int(input())
lst=list(map(int,input().split()))
ls=[]
for i in range(n):
    a=lst.count(lst[i])
    ls.append(a)
m=ls.index(max(ls))
print(lst[m])
