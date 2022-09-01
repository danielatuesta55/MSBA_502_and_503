#I created this workbook to play around with some if functions and blocks of code. 
#import dependencies
import pandas as pd
#This block of code is created to start the customer journey! The next block of code with heading "Checkout" will be the checkout portion 
#Creating df to serve as menu for customer
d = {'Item':["apples","banannas","meat","chicken","salad","drink","hotdog","pizza","french_fries","watermelon"],'Price $':[0.50,0.80,6.00,5.50,8.40,3.50,7.00,6.70,3.80,1.40]}
menu_df = pd.DataFrame(data=d)

#Create dictionary for items in menu 
items_in_menu_dict = {"apples" : 0.50,
"bananas" : 0.80,
"meat" : 6.00,
"chicken" : 5.50,
"salad" : 8.40,
"drink" : 3.50,
"hotdog" : 7.00,
"pizza" : 6.70,
"french_fries" : 3.80,
"watermelon" : 1.40
}

# Declare discounts percentages
discount_max_2_items= 0.20
discount_max_5_items= 0.35
discount_max_8_items=0.50

#Declare customer cart for checkout in list format

customer_cart = []

#user input for decision making
customer_name = input("Good morning! Welcome to my shop. what is the name for your order?")

#print name 
print("Nice to meet you " + customer_name + ". Please look at our menu and choose your items. Make sure you type them exactly as they are shown in the menu, ONLY CHOOSE ONE ITEM AT A TIME")
print(menu_df)
#ask user input for their order 
todays_order = input("What can I get ready for you? (Please remember to type all lowercase)")

#print name and ask if there is anything else you could get them
print("Great selection! Let me repeat your order to you: " + todays_order)
customer_cart.append(todays_order)

#create first If function 

more_items = input("is there anything else I can get for you?")

if more_items == "yes":
    more_items_1 = input("Great what else do you need?")
    print("your new order is: " + todays_order + ", " + more_items_1)
    #Append all items to list 
    customer_cart.append(more_items_1)
    checkout_ready_1 = input("is that all for today?")

    #Create nested if function     
    if checkout_ready_1 == "yes":
        print ("great, let's see what discounts we have for your today!") 
    else:
        more_items_2 = input("what else can I get for you?")
        print("your final order is: " + todays_order +", "+ more_items_1 + ", " + more_items_2)
        #Append all items to list 
        customer_cart.append(more_items_2)
        print("Let's get you to checkout!")

#Exit first if statement block!
elif more_items == "no":
    print("Lets head on out to checkout! to see all your available discounts")

else:
    print("Sorry that is not an option, we will continue with the previous input")



#Make sure that all items where appended to the list by using this statement: print(customer_cart)

customer_cart_final = customer_cart

#Checkout 
#count number of items in customer cart and convert to string
count_customer_cart = len(customer_cart)

#print(count_customer_cart)

#Double checking with customer their order. 
#convert list into string
double_check_list_customer = ' '.join(customer_cart)
#print(double_check_list_customer)

#customer consent
customer_confirmation_all_items_in_cart= input("Are all your items being displayed: " + double_check_list_customer)

#Create If statement to continue or restart
if customer_confirmation_all_items_in_cart == "yes":
    print("You have a total of " + str(count_customer_cart) + " items. Looking for discounts, please wait...")
else: 
    print("Sorry, please restart the program!")

#Discounts
if count_customer_cart <= 1:
    print("We have no discounts for your order today")
elif count_customer_cart <= 4:
    print("You get 20% off")
elif count_customer_cart <= 7:
    print("You get 35% off")
else:
    print("You get 50% off ")

#displaying total order cost before discount

#make df from my customers list
df1= pd.DataFrame(customer_cart_final, columns =['Item'])

#Created final customre df to get calculation
final_customer_df_with_price_df = pd.merge(menu_df, df1)

#print(final_customer_df_with_price_df)
user_total_no_discount = final_customer_df_with_price_df['Price $'].sum()
print("Your total for today is ${}, lets see if we can lower that for you!".format(user_total_no_discount))

#Create function to calculate final price after discount
#create variable
user_discount = 0.20 #manual input for now
#define function
def apply_discount(user_total_no_discount, user_discount):
    total_after_discount = user_total_no_discount - (user_total_no_discount*user_discount)
    return total_after_discount

#round total to two decimal places
total_after_discount = round(apply_discount(user_total_no_discount, user_discount),2)
#print final amount due
print("Your total for today after the discount was applied is ${}".format(total_after_discount))  

#Print thank you note
print("Thank you for shopping with us today! Until next time")