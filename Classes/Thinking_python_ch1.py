"""This are some of the exercises suggested at the end of chapter 1
Exercise 1 
In a print statement, what happens if you leave out the ()? """
#print("Hello, World!" # It will show a syntax error EOF while parsing
""" Exercise 2 
If you are trying to print a string, what happens if you leave out the quotation marks, or both?"""
#print(Hello,world!)#It has a syntax error: Invalid syntax
""" Exercise 3 you can use a minus sign to make a negative number like -2. What happends if you put a plus sign before a number? what about 2++2""" 
from ast import Str


print(-1)
print(+2)
print(2++2) #nothing happened it renders without mistakes
print(2++10)

""" Exercise 4 in math notation leading 0 are ok, as in 09. what happens if you try this in python 011"""
#print(011)#SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
""" Exercise 5 what happens when you have two values with no operator between them?"""
#print(20 87)#invalid syntax 

""" Exercise 6 how many seconds are there in 42 minutes and 42 seconds"""
print(42*60+22)
seconds_in_minute = 60
minutes = 42
existing_seconds = 22
#another way of doing it is by writing a function like this
def minutesinseconds(seconds_in_minute, minutes,existing_seconds):
    total_seconds=(seconds_in_minute*minutes)+existing_seconds
    return total_seconds
trial1= minutesinseconds(60,42,22)
print(trial1)

""" Exercise 7 how many MILES ARE THERE IN 10 KM hint 1.61 km per mile"""
def kmtomiles(km,ml):
    miles = km*ml
    return miles
print("BREAK")
print(kmtomiles(10,1.61))
anwserchallenge5=kmtomiles(10,1.61)
print("There are {} miles in 10km".format(anwserchallenge5))

"""If you run a 10km race in 42 minutes 42 seconds, what is your avg pace (time per mile in mins and seconds)? What is your ag speed in miles per hour"""
average_pace = trial1/anwserchallenge5
time_in_minutes = average_pace/60
print("Your average time per mile is {} minutes".format(time_in_minutes))

minutes_to_hours = trial1/60
avg_speed = anwserchallenge5/minutes_to_hours

print("your avg speed per mile is {} miles per hour".format(avg_speed))
