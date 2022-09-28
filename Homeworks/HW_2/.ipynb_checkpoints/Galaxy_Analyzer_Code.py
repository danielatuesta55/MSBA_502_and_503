# Code created by Jorge Daniel Atuesta
# Submitted on September 27th 2022

#Create repeat for user while loop to run 
repeat = 'yes'

#User define while loop in case they want to analyze more quadrants
while repeat.strip().lower() == 'yes':
    #Set all counters and list to 0 and empty is new loop is initiated
    g=[]
    galaxy_list = []
    count_planet = 0
    total_income = 0
        
    #Set Galaxy Distribution counter
    galaxy_distribution_count_1 = 0
    galaxy_distribution_count_2 = 0
    galaxy_distribution_count_3 = 0
    galaxy_distribution_count_4 = 0
    galaxy_distribution_count_5 = 0                              
    
    #Getting user input to know number of galaxies
    number_of_galaxies = int(input("How many galaxies are we analyzing today?"))
    print()
    
    if number_of_galaxies > 0:

        #For loop - from user input number galaxies get the length of iteration 
        for i in range (1, number_of_galaxies +1):        
            planets_in_galaxy = int(input(f"How many planets are in Galaxy {i}?"))
            print()
            planet_income = []

            #Nested for loop- go through user number of planets and get each planets incomes
            for j in range(1,planets_in_galaxy+1):
                planet_income_input = float(input(f"What is planets {j}'s income in Galaxy {i}?"))
                total_income += planet_income_input
                count_planet += 1
                planet_income.append(planet_income_input)
            #Append the planet income in each galaxy  into main list for further analysis
            galaxy_list.append(planet_income)
            print()

        #Calculating planets per galaxy, avg planetary income and avg galactic income
        planets_per_galaxy = count_planet/number_of_galaxies
        avg_planetary_income = total_income/count_planet
        avg_galactic_income = total_income/number_of_galaxies

        #Create for loop to get the total amount per sub-list and then add it to a new list galaxy_total for further analysis
        for i in (galaxy_list):
            galaxy_total = sum(i)
            g.append(galaxy_total)
        # Create and additional for loop to get the galaxy distribution
        for j in g:

            #Created a conditional statement if, elif and else to add to counter and get precise count of galaxies according to galaxy distribution
            if j < 20000:
                galaxy_distribution_count_1 +=1

            elif 20000 <= j < 40000:
                galaxy_distribution_count_2 +=1


            elif 40000 <= j < 60000:
                galaxy_distribution_count_3 +=1


            elif 60000 <= j < 80000:
                galaxy_distribution_count_4 +=1


            elif j >= 80000:
                galaxy_distribution_count_5 +=1

            else:
                print("Ooops! it seems that there was a mistake...")


        #print number of plantes and number of galaxies
        print()
        print("Number of planets:",count_planet)
        print("Planets per galaxy:",planets_per_galaxy)
        print()

        #Print avg planetary income and galactic income in $ format
        print("Average planetary income: $","{:,}".format(avg_planetary_income))#the format will place , in the final output
        print("Average galactic income: $","{:,}".format(avg_galactic_income))#the format will place , in the final output
        print()

        #Print galaxy distribution
        print("Income distribution: Less than $20,000:",galaxy_distribution_count_1 , "galaxy(s)\n",
                          "At least $20,000 but less than $40,000:", galaxy_distribution_count_2,"galaxy(s)\n",
                          "At least $40,000 but less than $60,000:",galaxy_distribution_count_3 , "galaxy(s)\n",
                         "At least $60,000 but less than $80,000:",galaxy_distribution_count_4 ,"galaxy(s)\n",
                         "At least $80,000:", galaxy_distribution_count_5, "galaxy(s)")
        print()
        #User exit while loop
        repeat = input("Would you like to analyze another quadrant (yes/no)?")
        
        if repeat.lower().strip() == 'yes':
            continue
        elif repeat.lower().strip() == 'no':
            repeat == 'no'
        else:
            print(f"Your answer: {repeat}, seems like a typo")
            repeat = input("Would you like to analyze another quadrant (yes/no)?")
        
    else:
        #print error message and ask if they would like to try again
        print(f"Ooops! ({number_of_galaxies}) seems like a typo. Please try again and enter an positive integer greater than 0 to infinity!")
        repeat = input("Do you want to try again? (yes/no)?")
        print()
        
#Print final statement to user
print("Thank you for using the Galaxy Analyzer!")