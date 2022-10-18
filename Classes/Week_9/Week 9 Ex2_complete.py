# Ask user for radius of a circle
# Calculate the area (pi * r ^ 2)
# Write a report at calculations.txt

import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2

output_file = input("What would you like to name the output file? ")

first_line = "Circle data report"
second_line = "\nRadius: " + str(radius)
third_line = "\nArea: " + str(area)

with open(output_file, "w") as file:
    file.write(first_line)
    file.write(second_line)
    file.write(third_line)