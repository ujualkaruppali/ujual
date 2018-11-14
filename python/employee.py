class employe:

    def __init__(self,x,y):
        self.name=x
        self.code=y

    def printData(self):
        print("name=",self.name)
        print("rollno",self.code)

    def getAge(self,myAge,salary):
        print(" age is"+str(myAge))
        print(" salary is"+str(salary))

s=employe("rahul",1)

h=int(input("enter age"))
i=int(input("enter salary"))
s.printData()
s.getAge(h)
s.getAge(i)

