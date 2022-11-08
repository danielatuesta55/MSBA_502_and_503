# Import dependencies 
import csv
from csv import writer
import os
from operator import itemgetter
import time 

#Create Stats function 

#Stats function 
def statistics():
    """Created a function that runs all code for statistics option"""
    
    # Set counters and empty lists for data collection
    total_rows = 0
    pending = []
    total_pending = 0
    total_pending_money_only=[]
    
    # Created a conditional statement to check if the "main" file exists or not
    if os.path.exists("transaction_ledger.csv"):
        is_file='yes'
    else:
        is_file='no'
    
    # Created a conditional statement if the file does or doesn't exist to preform actions
    if is_file == 'no':
        #If the file doesn't exist prompt the user and ask them to try again
        print("Sorry, no transaction data was loaded yet. Please try again.")
        

    if is_file == 'yes':
        #If the file does exist then open it in read mode and perform calculations
        with open('transaction_ledger.csv','r') as file:
            reader = csv.reader(file)
            header = next(file)
            for i in reader:
                total_rows += 1
                #print(i)
                #Extracting only the values that have pending 
                if i[4]=='PENDING':
                    pending.append(i)
                
            #Created inner function in order to grab the value on index 3 (amount) and create calculations
            #Used this as a resource for the code https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
            def Extract(pending):
                """Created this function to be able to extract the value from the list using itemgetter"""
                return list(map(itemgetter(3), pending))
            
            #Storing the previous step into a variable
            final_list_with_values = Extract(pending)
            
            # Since python reads in values as strings I converted the strings to floats
            total_pending_money_only = [round(float(i)) for i in final_list_with_values]
            
            # Created this for loop to add all the values and show them to user
            for i in total_pending_money_only:
                total_pending += i
           
            # Formatting print statement
            print()
            # Printed the results to the user    
            print(f"Number of current transactions {total_rows}")
            print("Total Amount pending: $","{:,}".format(total_pending))
            # Formatting print statement
            print()

#Create empty list that will hold all unique ID's in the transaction_ledgers csv that will be compared to identify duplicate transactions
unique_id_transaction_ledgers = []

#Create the Import function
def ImportFunction():
    
    #Create empty list to hold duplicate ID's found on the imported file
    duplicate_trans = []
    total_rows = 0
    duplicate_counter = 0
    # First step is to ask the user what file they would like to import
    which_file = input("Which file would you like to import?")
    print()
    
    #Using os.path.exists check if the 'main' file transaction_ledger.csv exists. if it does set variable to 'yes' if not set variable to 'no'
    if os.path.exists('transaction_ledger.csv'):
        main_file ='yes'
    else:
        main_file = 'no'
    
    # Created a conditional statement to check if the "user choice" file exists or not
    if os.path.exists(which_file):
        is_file='yes'
    else:
        #Prompt the user the file doesn't exist in this file path
        print()
        print(f"This file '{which_file}' does not exist.")
        is_file='no'
    # Created a conditional statement if the file does or doesn't exist to preform actions
    if main_file == 'yes':    
        # If true than open the file and preform actions
        if is_file == 'yes':
            
            #Second step is to load the file into python. 
            with open(which_file,'r') as file:
                user_file = file.read()
            #print(user_file)             
            print("File Imported successfully, checking for possible duplicate transactions...")    
            print("Checking for duplicates...")
            time.sleep(0.5)
            print("Almost done...")
            time.sleep(0.8)
            print("Done!")
            time.sleep(0.5)
            # Reading in the transaction_ledger.csv Since its true
            with open('transaction_ledger.csv','r') as file:
                trans_file = csv.reader(file)
                header = next(trans_file) #This will skip the headers on CSV to be able to compare ID in column one and see if there is duplicate values
                #Created loop with the help @craigb anwser on my quesiton on stackover overflow
                for i in trans_file:
                    unique_id_transaction_ledgers.append(i[0].strip().upper())

            # NEW FILE WITH UNIQUE TRANSACTION CONTENT ONLY NO DUPLICATES
            with open(which_file,'r') as file:
                reader = csv.reader(file)
                for i in reader:
                    total_rows += 1
                    if i[0].strip().upper() in unique_id_transaction_ledgers:
                        duplicate_trans.append(i[0])
                        duplicate_counter +=1
                    else:
                        with open('transaction_ledger.csv','a+', newline='') as outfile: # Missing this part as to how to append properly line by line! 
                            #header = next(outfile)
                            writer=csv.writer(outfile,delimiter=",")
                            writer.writerow(i)
                print()
                print(f"The following transactions have already been recorded: {duplicate_trans} ")
                time.sleep(0.5)
                print(f"Number of current transactions:{total_rows-duplicate_counter}")

        #If file doesn't exist set flag true
        else:
            flag = True
    # If main file does not exist than create it and preform the actions needed        
    if main_file == 'no':
        
         #Open user file and read it to be able to append to the new empty file transaction_ledger.csv
        with open(which_file,'r') as old_file:
            reader_obj = csv.reader(old_file) #read the current csv file
            #Write transactions_ledgers.csv and preform actions
            with open('transaction_ledger.csv', 'w') as new_file:
                writer_obj = csv.writer(new_file, delimiter=",",lineterminator = "\n")
                header = ['ID', 'COMPANY NAME', 'DATE', 'AMOUNT', 'STATUS']
                writer_obj.writerow(header)
                for data in reader_obj:
                    total_rows += 1
                    #loop through the read data and write each row in transaction_Ledger.csv
                    writer_obj.writerow(data)
                print()
                print("New file created and filled in with imported file data")
                time.sleep(0.2)
                print(f"Number of current transactions:{total_rows}")
                print()
        
#Create boolean value for while loop name it flag
flag = True

#Created while loop
while flag:
    # Ask the user what action they want to preform. 
    user_selection = input("What would you like to perform (import/statistics) or end the simulation?")
    # Conditional - if they choose stats then call the function statistics
    if user_selection.strip().lower() == 'statistics':
        statistics()
        #Ask user if they want to run another analysis 
        repeat1 = input('Would you like to run any further analyses (yes/no)?' )
        if 'y' in repeat1.strip().lower():
            #ask user what they want to do
            next_step = input("What would you like to perform (import/statistics)?")
            if next_step.lower().strip() == 'statistics':
                #if statistics than run the statistics function
                statistics()
                #keep flag true to loop again if the user wants to 
                flag = True
                
                #If import run the ImportFunction and keep flag true
            elif next_step.lower().strip() == 'import':
                ImportFunction()
                flag = True
       
        # If they dont want to continue than end simulation turn flag False        
        else:
            print()
            print("Thanks for using this simulation")
            flag = False
        
    # Conditional -  if they choose the import function then call the ImportFunction
    elif user_selection.lower().strip() == 'import':
        ImportFunction()
        #Ask user if they want to run another analysis 
        repeat = input('Would you like to run any further analyses (yes/no)?' )
        if 'y' in repeat.strip().lower():
            flag = True
        else:
            print("Thanks for using this simulation")
            flag = False
    elif 'e' in user_selection[0].lower().strip():
        print()
        print("Thanks for using this simulation")
        flag = False
    # If the user inputs an invalid operation than prompt them that the program doesn't preform the action and ask them to try again
    else:
        print()
        print("Sorry, this program can only run the following two functions: 1. Import 2. Statistics or you can end the simulation")
        flag = True

        
    
