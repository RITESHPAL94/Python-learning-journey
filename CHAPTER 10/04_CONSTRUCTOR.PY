class Employee:        
    Language = "Python" 
    salary = 1200000

    def __init__(self, name, salary, Language): # dunder method which is automatically called
        self . name = name
        self.salary = salary
        self.Language = Language
        print("I am creating an object")
    def getInfo(self):
        print(f"The language is {self.Language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning")

ritesh = Employee("Ritesh", 130000, "Javascript") 
# ritesh.name = "Ritesh"
print(ritesh.name, ritesh.salary)