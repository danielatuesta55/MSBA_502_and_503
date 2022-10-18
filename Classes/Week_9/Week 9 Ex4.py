# Ask the user which company’s file to look up
# Ask the user which date to look up the price
# Print out the desired price

import csv

which_file = input("Which file do you want to analyze? apple/google/microsoft: ")
which_date = input("For what date do you want to look up? ")

try:
    with open(which_file, "r") as file:
        reader = csv.reader(file)
        for line in reader:
            date = line[0]
            price = float(line[1])
            if date == which_date:
                print("Price", price)
except:
    print("Sorry, that file was not found. Please try again:")