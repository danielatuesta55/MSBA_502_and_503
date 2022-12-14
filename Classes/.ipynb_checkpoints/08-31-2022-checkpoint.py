#Today's Class

#Important to note that the teacher likes the syntax to be word_word_word make sure all your code is written in this format

""" Variables in python 

A variable is a container tat we can use to store values

Each variable has a unique name so that we can find, read, or update its value

Example:
"""

text = "Hello, world!"
motto = "Python is cool."
print(text,motto)

""" Python rules for variable naming are: 
1. A variable name is at least one character, but there is no upper limit for the length of the name
2. Variable names van use uppercase letters (A-Z), lowercase letters (a-z), digits (-9) and the underscore character(_)
3. A variable name cannot start with a digit (0-9) and cannot end with a letter

Python's conventions is usually to use lowercase letters, and if a variable name is multiple words, uses underscores to separate them.
For example,
variable_name
a_new_variable
"""

""" Types in Python:
1. Type int (short for integer)- values are integers like 5 or 7
2. Type float (short for floating point number)- values are decimal numbers like
3. Type str (short for string)- Values are snippets of text, like "hello"
4. Type bool (short for Boolean) - Values are True or False

"""

#Example using Variable 

#A marathon is 26.2 miles, and a mile is 1.61 km. How many Kilometers is a marathon
#marathon is 26.2 miles
#1 mile = 1.61 kilometers
#Print the number of kilometers in a marathon and

#name variables 
marathon_miles = 26.2 
kilometers = 1.61 
 
#Create new variable that states the calculation 
marathon_kilometers = marathon_miles * kilometers

#Print the result of the calculation
print("There are {} KM in a marathon".format(marathon_kilometers))

#In a function format
#Define the function
def marathon_in_kilometers(a,b):
    miles_to_km = a * b #Create the "formula" to calculate
    return miles_to_km

print("The total KM in a marathon is {}".format(marathon_in_kilometers(26.2,1.61)))

# We are going to create a calculator that creates any amount 

miles = 9000
km_from_miles= miles * 1.61

print(km_from_miles)

""" Variable (re)assignment

You can overwrite variables they are not immutable
"""

x=5
print(x)
x=9 # X will hold the value 9 and not 5
print(x)

seuss = "I do not like green eggs and ham"
print(seuss)
seuss = "I do not like them Sam I am"
print(seuss)

""" Conditions (IF) 
Often, we may want different code to run depending on the situation

Using an if block, any code in the block will run if the condition is true
"""
#example of IF statement
x = 19
if x>5:
    print("This only runs if x>5")
    print("This block is still running")
print("step 1 complete")
if x>12:
    print("x is enormous")
print("Done")

