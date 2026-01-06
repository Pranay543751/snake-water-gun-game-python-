import random

computer=random.choice([2,0,-2])
youstr= input("enter your choice :")
youdict={"s":2,"p":0,"z":-2}
reversedict={2:"stone",0:"paper",-2:"cissors"}
you= youdict[youstr]

print(f"your choice {reversedict[you]}\n  computer choice {reversedict[computer]}")

if computer==you:
    print("match is draw !")
else:
   #logic 1
    # if computer==2 and you==0:                    
    #     print("you win!")
    # elif computer==2 and you==-2:            
    #     print("you lose !")
    # elif computer==0 and you==2:       
    #     print(" you lose !")
    # elif computer==0 and you==-2:       
    #     print("you win !")
    # elif computer==-2 and you==2:       
    #     print("you win !")
    #     # elif computer==-2 and you==0:    
    #     print("you lose !")
    # else:
    #     print("somthinh went wrong !")    
#logic 2
   if computer-you==-2 or computer-you==4:
         print("you lose !")
   else:
     print("you win !")