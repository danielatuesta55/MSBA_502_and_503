# Ask the user what to write to a file
# Allow an unlimited number of responses
# Append each response to output.txt

repeat = "yes"

while repeat.lower().strip() == "yes" :
    response = input('What would you like to append?: ')

    with open("output.txt", "a") as croutons:
        croutons.write(response + "\n")

    repeat = input("Would you like to append more things? yes/no ")