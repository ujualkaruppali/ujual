class students:

    def __init__(self,x,y):
        self.name=x
        self.rollno=y

    def printData(self):
        print("name=",self.name)
        print("rollno",self.rollno)

    def getAge(self,myAge):
        print(" age is"+str(myAge))

s=students("rahul",1)

x=int(input("enter age"))

s.printData()
s.getAge(x)

