
which_file = input("Which file do you like to analyze?")
which_date = input("Which date do you want to look up?")

try:
    with open (which_file,"r") as file:
        reader = csv.reader(file)
        for line in reader:
            date = line[0]
            price = float(line[1])
            
            if date == which_date:
                print("Price:", price)
            
    
except:
    print("Sorry, we don't have that info ")