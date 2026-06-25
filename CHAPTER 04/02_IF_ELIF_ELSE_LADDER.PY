a = int(input("Enter you age: "))

#If elif else ladder

if(a>=18):
    print("You are obove the age of consent")

elif(a<0):
    print("You are entering an Invalid negative age")

elif(a==0):
    print("You are entering an Invalid age")

else:
    print("You are below the age of consent") 

print("The end of program")