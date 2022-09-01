#Declare variables food items price

apples = 0.50
bananas = 0.80
meat = 6.00
chicken = 5.50
salad = 8.40
drink = 3.50
hotdog = 7.00
pizza = 6.70
french_fries = 3.80
watermelon = 1.40

# Declare discounts percentages
discount_max_2_items= 0.20
discount_max_5_items= 0.35
discount_max_8_items=0.50

#user input for decision making
customer_name = input("Good morning! Welcome to my shop. what is the name for your order?")
#print name 
print("Nice to meet you " + customer_name)
#ask user input for their order 
todays_order = input("what can I get ready for you? (Please remember to type all lowercase)")
#print name and ask if there is anything else you could get them
print("Great selection! Let me repeat your order to you: " + todays_order)

#create first If function 

more_items = input("is there anything else I can get for you?")

if more_items == "yes":
    more_items_1 = input("Great what else do you need?")
    print("your new order is: " + todays_order + ", " + more_items_1)
    checkout_ready_1 = input("is that all for today?")
    if checkout_ready_1 == "yes":
        print ("great, let's see what discounts we have for your today!") 
    else:
        more_items_2 = input("what else can I get for you?")
        print("your final order is: " + todays_order +", "+ more_items_1 + ", " + more_items_2)
        print("Let's get you to checkout!")
else:
    print("Lets head on out to checkout! to see all your available discounts") 
