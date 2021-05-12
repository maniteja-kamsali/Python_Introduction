# class and object
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("maniteja", 27)
p1.myfunc()

#inheritance
class Person(object):
       
    # Constructor
    def __init__(self, name):
        self.name = name
   
    # To get name
    def getName(self):
        return self.name
   
    # To check if this person is an employee
    def isEmployee(self):
        return False
   
   
# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
   
    # Here we return true
    def isEmployee(self):
        return True
   
# Driver code
emp = Person("Mani")  # An Object of Person
print(emp.getName(), emp.isEmployee())
   
emp = Employee("Mani") # An Object of Employee
print(emp.getName(), emp.isEmployee())