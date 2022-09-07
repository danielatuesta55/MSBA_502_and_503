#Declare variables 

status = "enrolled"
signed_up = "no"

#If statement
if status == "enrolled" and signed_up == "yes":
    print("What classes are you taking?")
#second condition 
elif status == "enrolled" and signed_up == "no":
    print("That's okay, maybe next semester.")
#Finish if statement with else
else:
    print("Have you enrolled?")
#This needs to print on every entry so it has to be outside the code block 
print("Fall 2020 lets gooooo!!!")

#Four types of variables in python
#float, string, boolean, integer

#Math symbols 
#+,-,*-/,//,%,**

#use modulus (%) to find number divided by two 

test = 9007


if test % 2 == 0:
    print(test,'This number is even')
else:
    print('This number is odd')
