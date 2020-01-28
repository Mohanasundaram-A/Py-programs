n=int(input())
lst=list(map(int,input().split()))
ls=[]
c=0
for i in range(len(lst)):
	c+=lst[i]
	ls.append(c)
print(*ls)
