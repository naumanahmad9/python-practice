# single line comment
""" 
multi line
commment 
"""

a = 2

b = [1,2,3]

c = { "favColor" : "Blue"}

print a
print b[0]
print c["favColor"]

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

print factorial(5)

def kneeMatch(opp):
  if opp == "Arslan Ash":
    return "Result: Defeat"
  else:
    return "Result: Win"

print kneeMatch("Anakin")
print kneeMatch("Arslan Ash")

try:
  print(b[2])
except IndexError:
  print("Item not in the list")

mySet = {1,2,2,3,3,3}
print mySet

"""
class Person:
  def __init__(self):
    print("New Person")

p = Person()

class John(Person):
  def __init__(self):
    super().__init__()
    print("My name is John")

 j = John()
"""

#import math
#print(math.pi)

# --------------------
# A Python program to demonstrate inheritance
class Person(object): 
       
    # Constructor 
    def __init__(self, name): 
        self.name = name 
   
    # To get name 
    def getName(self): 
        return self.name 
   
    # To check if this person is employee 
    def isEmployee(self): 
        return False
   
   
# Inherited or Sub class (Note Person in bracket) 
class Employee(Person): 
   
    # Here we return true 
    def isEmployee(self): 
        return True
   
# Driver code 
emp = Person("Geek1")  # An Object of Person 
print(emp.getName(), emp.isEmployee()) 
   
emp = Employee("Geek2") # An Object of Employee 
print(emp.getName(), emp.isEmployee()) 