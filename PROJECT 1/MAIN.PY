'''

ROCK FOR 1
PAPER FOR -1
SCISSOR FOR 0

'''


# FIRST METHOD

computer = -1

your_str = input("Enter your choice: ").lower()
your = {"rock" : 1 , "paper"  : -1 , "scissor" : 0}


if your_str not in your:
    print("Invalid choice")
else:
    you = your[your_str]

    if(computer == -1 and your_str == 1):
        print("You lose! Try again some time")

    elif(computer == -1 and your_str == 0):
        print("You win!")

    else:
        print("you choose same thing retry!")




# SECOND METHOD 

computer = 0
choice = int(input("Enter your choice scissor = 0,rock =  1,paper = -1: "))
your_choices = {1 : "rock" , -1 : "paper" , 0 : "scissor"}

if choice  not in (-1,1,0):
    print("Invalid choice")

elif(computer == 0 and choice == 1):
    print("You win!")

elif(computer == 0 and choice == -1):
    print("You lose!")

else:
    print("choose same thing try again")

# ALSO LEARN THE USES OF is, is not, in, not in 