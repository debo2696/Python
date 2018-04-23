import datetime
class Person:
        def __init__(self,nm,age,sex):
                self.nm=nm
                self.age=age
                self.sex=sex
                self.reg=datetime.datetime.now()
                print("Hello, {}".format(nm))
        def __str__(self):
                return str(print("Name:{}\nAge:{}\nSex:{}\nCreated on:{}".format(self.nm,self.age,self.sex,self.reg)))
        def __del__(self):
                return str(print("{}'s memory has been de-allocated.".format(self.nm)))
"""nm=str(input("Enter the name:"))
age=int(input("Enter the age"))
sex=str(input("Enter the sex"))"""
P1=Person("Arnold",23,"M")
P2=Person("Schwartz",45,"M")
P3=Person("Natasha",25,"F")
P4=Person("Riley",19,"F")
"""P1=Person(nm,age,sex)"""
print(P1)
print(P2)
print(P3)
print(P4)
del(P2)
print(P2)
