#The following code has been written and created by Jorge Daniel Atuesta on 10/16/2022

#Import Dependencies 
import random
import time

# Create the FishingSim Function 
def FishingSim():
    """Fishing simulator to help the company know what and when to harvest. Also if they should sell the business or retire"""
    
    #Start While loop with repeat statement 
    repeat = 'yes'
    
    #While user uses the letter 'y' in the first letter position on his response to repeat run the code again. 
    while 'y' in repeat[0].lower().strip():
        
        #Set counters to 0
        counter_year = 0 
        price = 0
        cumulative_price = 0
        price_counter = 0
        
        # Create while loop that will run while its true
        while True:
            #Add to years counter
            counter_year +=1
            
            #Print heading for each year the simulation runs
            print('* Year',(counter_year),"*")
            
            #Conditional telling what to run each year. I used modulus function for this 
            if counter_year%4 == 1:
                print("Focus this year: Lobsters")
                
                # Used the random library to calculate the probability of event happening
                probability = random.random()
                
                #Conditional to tell the program what the revenues or loss are for that year
                if probability <=0.1:
                    price = 125000
                elif probability <=0.8:
                    price=50000
                else:
                    price = -10000
                
                #Add to the cumulative price counter the price 
                cumulative_price += price
                
                #Print profit or loss for the year & total profit or loss 
                print("This year's profit (or loss): $","{:,}".format(price))
                print("Total profit (or loss): $","{:,}".format(cumulative_price))
            
            #Create conditional with modulus to set Kelp 
            elif counter_year%4 == 2 or counter_year%4 == 0 :
                print("Focus this year: Bullwhip Kelp")
                
                #Use random to calculate probability of event 
                probability = random.random()
                
                #Create conditional that will run if event happens thanks to probability
                if probability <=0.6:
                    price=45000
                else:
                    price=-10000
                
                #Add to cumulative_price counter 
                cumulative_price +=price
                
                #Print profit or loss for the year & total profit or loss 
                print("This year's profit (or loss): $","{:,}".format(price))
                print("Total profit (or loss): $","{:,}".format(cumulative_price))
            else:
                print("Focus this year: Urchins")
                #Use random to calculate probability of event 
                probability = random.random()
                
                #Create conditional that will run if event happens thanks to probability
                if probability <= 0.75:
                    price = 30000
                else:
                    price = -5000
                
                #Add to cumulative_price counter 
                cumulative_price +=price
                
                #Print profit or loss for the year & total profit or loss 
                print("This year's profit (or loss): $","{:,}".format(price))
                print("Total profit (or loss): $","{:,}".format(cumulative_price))
            
            #use time sleep function so that the user can follow the simulation year by year. This prevents the code to be printed all at once.
            time.sleep(1) 
            
            #Create conditional for price counter
            if price > 0:
                #Add to price counter this will track 5 consecutive years of profit
                price_counter += 1
            else:
                price_counter = 0 
            
            #Using flag I can tell the while loop to stop running its more or less like the repeat user based while loop running. 
            flag = False
            print()
            
            #Created conditionals to print to terminal 
            if cumulative_price < 0:
                #make flag True so that at the end it can break
                flag = True
                print("The total profit is negative at year-end. The owner will close the fishing operation and look for a new business venture.")
            if cumulative_price >=325000:
                #make flag True so that at the end it can break
                flag = True
                print("The total profit reaches at least $325,000 at year-end. The owner will happily retire.")
            if price_counter == 5:
                #make flag True so that at the end it can break
                flag = True
                print("There are five consecutive years of positive profit. The manager will happily retire.")
                
            # If flag true than it can break the while loop and avoid an infinite loop
            if flag:
                break
            #Used empty print statement to make it visually for the user
            print()
        #Used empty print statement to make it visually for the user
        print()
        #User input to see if they want to run another simulation or not! 
        repeat = input("Would you like to run another simulation (yes/no)?")

#Called my function for all the code to run!         
FishingSim()

#This code has been written and created by Jorge Daniel Atuesta -- 10/16/2022
