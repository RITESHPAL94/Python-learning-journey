'''
class Employee:         # Defined a class named Employee
    name = "Ritesh"
    Language = "Py"  # class Attributes
    salary = 1200000


ritesh = Employee()         # Store a class in variable
print(ritesh.name, ritesh.Language)     # ritesh.name gives name = "Ritesh" and ritesh.Language gives Py from class
'''
class Employee:        
    Language = "Py" 
    salary = 1200000


ritesh = Employee() 
ritesh.name = "Ritesh"     # object Attributes/ instance Attributes   
print(ritesh.name, ritesh.salary, ritesh.Language)     

rohan = Employee()
rohan.name = "Rohan Robin Hood"
print(rohan.name, rohan.salary, rohan.Language)

# Here name is object/instance attributes and salary and language are class 
# attributes as they directly belong to the class 