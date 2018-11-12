a=int(input("enter a num"))
h=a
x=0
while(a>0):
    y=a%10
    x=x*10+y
    a=a//10
if(x==h):
    print("number is palindrome")
else:
    print("numer is not palindrome")