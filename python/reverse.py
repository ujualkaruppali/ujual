a=int(input("enter a num"))
h=a
x=0
while(a>0):
    y=a%10
    x=x*10+y
    a=a//10
print(x)