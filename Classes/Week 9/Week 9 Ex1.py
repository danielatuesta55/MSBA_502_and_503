# Read the file shakespeare.txt
# Ask the user for a search term
# Determine if the file contains the search term and report the results

with open("shakespeare.txt","r") as file:
    file_contents = file.read()

search = input("Enter a search term: ")

if search.lower().strip() in file_contents.lower():
    print("Your search was found!")
else:
    print("Sorry, your search was not found.")

print(file_contents)


