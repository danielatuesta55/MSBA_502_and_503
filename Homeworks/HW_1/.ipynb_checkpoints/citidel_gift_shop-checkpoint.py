# Citidel giftshop Virtual Assistant
# Created by Jorge Daniel Atuesta

#Get the users name from input 

user_name = input('Hi and welcome to Citidel Gift Shop. Can I please get a name for the order?')

#Check if user input value is stored into username variable with print statement.
#print(user_name)

#Print nice to meet you name
print('Thank you {}, it is a pleasure to serve you today.'.format(user_name))

#List the products offered to the user before asking if they want to buy them or not
print("Here is a list of the products being offered today: 1. Plumbuses 2. Meeseeks Boxes and 3. Portal Fluid")

#First purchase
#Declare buy_plumbuses variable with user input
buy_plumbuses = input('{}, would you like to buy Plumbuses today?'.format(user_name))

#Created first IF statement
if buy_plumbuses == "yes":
    number_of_plumbuses = int(input('{}, how many Plumbuses do you need today?'.format(user_name)))
    #Nested IF to get total value of purchase
    if 0<= number_of_plumbuses <= 5:
        #Create variable to hold total price for the amount of boxes user required
        cost_plumbuses = 20.00 * number_of_plumbuses
        #create total_cart variable
        total_cart = cost_plumbuses
        #print current cart
        print("{}, your cart is at ${} Let's see what else I can get for you today.".format(user_name, total_cart))
    #Created elif statement to get discount between 5 - 15
    elif 5 <= number_of_plumbuses <= 15:
        #get value with discount
        cost_plumbuses = 17.5 * number_of_plumbuses
        #create total_cart variable
        total_cart = cost_plumbuses
        #print current cart value
        print("{}, your cart is at ${} Let's see what else I can get for you today.".format(user_name, total_cart))
    #Created else to finish nested if statement   
    elif number_of_plumbuses >15:
        #get value with discount
        cost_plumbuses = 15.25 * number_of_plumbuses
        #create total_cart variable
        total_cart = cost_plumbuses
        #print current cart
        print("{}, your cart is at ${} Let's see what else I can get for you today.".format(user_name, total_cart))
    else:
        print("{}, that is an invalid number. Please make sure you are typing in whole numbers from 0 to infinity. Let's move on to our next option".format(user_name))
        total_cart = 0
        cost_plumbuses = 0
elif buy_plumbuses == "no":
    #Make sure total cart is $0
    total_cart = 0
    #Make sure total number of plumbuses is 0
    number_of_plumbuses = 0
    print("That's ok {}, we will move to the next option...".format(user_name))
    #Make sure cost of plumbuses is 0
    cost_plumbuses = 0
#Make sure that if a user inputs something wrong it does not crash code so I put the else statement as follows
else:
    #Make sure total cart is $0
    total_cart = 0
    #Make sure total number of plumbuses is 0
    number_of_plumbuses = 0
    print("{}, can't process your response. Please make sure you are writing in lower case and stick to 'yes' or 'no' answer. We will move to the next option...".format(user_name))
    #Make sure cost of plumbuses is 0
    cost_plumbuses = 0

#Second purchase 
#Declare buy_meeseeks_boxes variable with user input
buy_meeseeks_boxes = input('{}, would you like to buy Meeseeks Boxes today?'.format(user_name))

#Created second IF statement for the meeseeks boxes
if buy_meeseeks_boxes == "yes":
    number_of_meeseeks_boxes = int(input('{}, how many Meeseeks Boxes do you need today?'.format(user_name)))
    
    #Nested IF to get total value of purchase
    if 0 <= number_of_meeseeks_boxes <= 9:
        
        #Create variable to hold total price for the amount of boxes user required
        cost_meeseeks_boxes = 1.75 * number_of_meeseeks_boxes
        
        #Add total_cart to keep track of total payment
        total_cart = total_cart + cost_meeseeks_boxes
        
        #print current cart
        print("{}, your cart is at ${}. Let's see what else I can get for you today.".format(user_name,total_cart))
   
    #Created elif statement to get discount between 10 - 18
    elif 10 <= number_of_meeseeks_boxes <= 18:
        
        #get value with discount
        cost_meeseeks_boxes = 1.50 * number_of_meeseeks_boxes
        
        #Add total_cart to keep track of total payment
        total_cart = total_cart + cost_meeseeks_boxes
        
        #print current cart value
        print("{}, your cart is at ${}. Let's see what else I can get for you today.".format(user_name,total_cart))
        
    #Created else to finish nested if statement   
    elif number_of_meeseeks_boxes > 18:
        #get value with discount
        cost_meeseeks_boxes = 1.25 * number_of_meeseeks_boxes
        
        #Add total_cart to keep track of total payment
        total_cart = total_cart + cost_meeseeks_boxes
        
        #print current cart
        print("{}, your cart is at ${} Let's see what else I can get for you today.".format(user_name,total_cart))
    #Make sure that if a user inputs something wrong it does not crash code so I put the else statement as follows
    else:
        print("{}, that is an invalid number. Please make sure you are typing in whole numbers from 0 to infinity. Let's move on to our next option".format(user_name))
        total_cart = 0
        cost_meeseeks_boxes = 0
        number_of_meeseeks_boxes = 0
elif buy_meeseeks_boxes == "no":
    #Create print statement to take client to final product order
    print("That's ok, we will move to our final product...")
    #Make sure number of meeseeks boxes is 0
    number_of_meeseeks_boxes=0 
    #Make sure total cart is $0
    total_cart = 0 + total_cart
else:
     #Create print statement to take client to final product order
    print("{}, can't process your response. Please make sure you are writing in lower case and stick to 'yes' or 'no' answer. We will move to the next option...".format(user_name))
    #Make sure number of meeseeks boxes is 0
    number_of_meeseeks_boxes=0 
    #Make sure total cart is $0
    total_cart = 0 + total_cart
    

# Third purchase

#Declare portal_fluid variable with user input
buy_portal_fluid = input('{}, would you like to buy Portal Fluid today?'.format(user_name))

#Created first IF statement
if buy_portal_fluid == "yes":
    number_of_portal_fluid = int(input('{}, how many gallons of Portal Fluid do you need today?'.format(user_name)))
    
    #Nested IF to get total value of purchase
    if 0 <= number_of_portal_fluid <= 2.99:
        
        #Create variable to hold total price for the amount of boxes user required
        cost_portal_fluid = 8.00 * number_of_portal_fluid
        
        #Add total_cart to keep track of total payment
        total_cart = total_cart + cost_portal_fluid
        
        #print current cart
        print("{}, your cart is at ${}. Let's head out to checkout.".format(user_name,total_cart))
   
    #Created elif statement to get discount between 10 - 18
    elif 3 <= number_of_portal_fluid <= 7:
        
        #get value with discount
        cost_portal_fluid = 7.00 * number_of_portal_fluid
        
        #Add total_cart to keep track of total payment
        total_cart = total_cart + cost_portal_fluid
        
        #print current cart value
        print("{}, your cart is at ${}. Let's head out to checkout.".format(user_name,total_cart))
        
    #Created else to finish nested if statement   
    else:
        #get value with discount
        cost_portal_fluid = 6.00 * number_of_portal_fluid
        
        #Add total_cart to keep track of total payment
        total_cart = total_cart + cost_portal_fluid
        
        #print current cart
        print("{}, your cart is at ${} Let's head out to checkout.".format(user_name,total_cart))
elif buy_portal_fluid == "no":
    #Print statement to take customer to checkout
    print("That's ok, Let's head out to checkout...")   
    #Make sure number of portal fluid  is 0
    number_of_portal_fluid = 0 
    #Make sure total cart is $0
    total_cart = 0 + total_cart
else:
    #Create print statement to take client to final product order
    print("{}, can't process your response. Please make sure you are writing in lower case and stick to 'yes' or 'no' answer. We will move to checkout".format(user_name))
    #Make sure number of meeseeks boxes is 0
    number_of_portal_fluid = 0 
    #Make sure total cart is $0
    total_cart = 0 + total_cart
#Print Final statement with clients name total purchase order
print("{}, your final purchase includes: {} Plumbuses, {} Meeseeks Boxes, and {} gallons Portal Fluid. The final amount to pay is ${}, We hope to see you again soon!".format(user_name,number_of_plumbuses,number_of_meeseeks_boxes,number_of_portal_fluid,total_cart))

