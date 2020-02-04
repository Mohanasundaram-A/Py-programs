n=input("Enter a Username : ")
while n[0].isdigit() or '@' not in n or '.' not in n or n.index('@')>n.index('.'):
    print("Invalid username")
    n=input("Enter a valid Username : ")
def pwd(p):
    sp="!”#$%&’()*+,-./:;<=>?@[\]^_`{|}~"
    u,l,d,c=0,0,0,0
    if len(p)>=5 and len(p)<=15:
        for i in p:
            if i.isupper():u+=1
            elif i.islower():l+=1
            elif i.isdigit():d+=1
            elif i in sp:c+=1
        else:
            if u>=1 and l>=1 and d>=1 and c>=1:return p
            else:
                print("Not a valid Password")
                p=input("Enter valid password : ")
                pwd(p)
    else:
        print("Not a valid Password")
        p=input("Enter valid password : ")
        pwd(p)
p=input("Enter your password : ")
p=pwd(p)
f=open("login.txt","a")
f.write(n+'\t'+p+'\n')
print("You're Registered")
f.close()
f=open("login.txt","r")
user=input("Enter your username : ")
c=0
while f.readline():
    r=f.readline()
    if user in r:
        c+=1        
pas=input("Enter your Password : ")
while f.readline():
    r=f.readline()
    if user in r:
        c+=1
print("Login Sucessfull") if c==2 else print("Username or Password wrong")
