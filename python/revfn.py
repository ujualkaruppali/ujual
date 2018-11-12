
def rev(d):
    
    x=0
    while(d>0):
        y=d%10
        x=x*10+y
        d=d//10
    print(x)
    
t=int(input("num1"))
rev(t)




