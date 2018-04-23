class Person:
	def __init__(self,nm,age):
		self.nm=nm
		self.age=age
		print("Name is:{} and Age is:{}".format(nm,age))
	def __str__(self):
		return str("Name:{}\nAge:{}".format(self.nm,self.age))
class Teacher(Person):
	def __init__(self,nm,age,sub):
		Person.__init__(self,nm,age)
		self.sub=sub
	def __str__(self):
		return str(Person.__str__(self)+"\nSubject:{}".format(self.sub))
	def a(self,nm,age):
		Person.__init__(self,nm,age)
class Student(Teacher):
        
	def b(self,nm,age):
		Teacher.__init__(self,nm,age)
		
