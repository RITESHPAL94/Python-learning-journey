class Employee:        
    Language = "Python" 
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.Language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning")

ritesh = Employee() 
ritesh.Language = "javaScript"     # object Attributes/ instance Attributes   
print(ritesh.salary, ritesh.Language)  

ritesh.greet()
ritesh.getInfo()
# Employee.getInfo(ritesh)