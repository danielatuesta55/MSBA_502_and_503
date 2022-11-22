#This code was created by Jorge Daniel Atuesta Nov 13 2022
"""Before you start read this: Make sure to pick which API you want to hit on line 17 or 18. 
I did it this way since I am uploading to github and I don't want other people to hit my API.
If you are testing use my repo on github if you are evaluating than please comment line 18 and uncomment line 17"""

# Import dependencies 
import pandas as pd 
import numpy as np
import tkinter 
import tkinter.messagebox
import tkinter.ttk
import requests
import json
import sys

#Step 1: Try and except block to hit the API
try:
    #response = requests.get('http://api.coinlayer.com/api/live?access_key=5c5f1acb20cc2f5f539ac097f3234258&symbols=BTC,ETH,BNB,XRP')
    response = requests.get("https://raw.githubusercontent.com/danielatuesta55/MSBA_502_and_503/main/Homeworks/HW_5/json/json_static.txt")
    data = json.loads(response.text)
    #print(json.dumps(data, indent = 4))
    rates= data["rates"]
    #print(rates)
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise Exception("Double check the website/API link")
    sys.exit(1)

# Step 2: Create the functions 
# Two functions for two buttons. 1 convert currency 2. Close Converter

#Function 1
def convertCurrency():
    """Using this function to convert user input into $ for crypto"""
    #Make variables global
    global btc_box,bnb_box,eth_box,xrp_box        
    #Get quant values from user input and check if they are float if not than error message box
    try:
        value1 = float(btc_box.get()) 
        value2 = float(bnb_box.get())
        value3 = float(eth_box.get())
        value4 = float(xrp_box.get())
        #Create list quant to hold the user quant values 
        quant = [value2,value1,value3,value4]
        #Showinfo message using tkinter to tell user the conversions file was a success
        tkinter.messagebox.showinfo("Complete", "The conversions where stored in crypto_conversion.csv")
        
        #Clear content of text box
        btc_box.delete(0, tkinter.END)
        bnb_box.delete(0, tkinter.END)
        eth_box.delete(0, tkinter.END)
        xrp_box.delete(0, tkinter.END)
        
        #Make sure that 1 is the default value for the text box
        btc_box.insert(0, 1)
        bnb_box.insert(0, 1)
        eth_box.insert(0, 1)
        xrp_box.insert(0, 1)
        
    #If values in boxes can not be converted to a float than display error 
    except ValueError:
        tkinter.messagebox.showerror("Error","Sorry, the report could not be written. Check that only numeric values are entered.")
       

    # Get values in list format to create df from dic
    price = rates.values()
    #convert to list
    price = list(price)
    currency = rates.keys()
    #multiply and convert results to list
    cost = list(np.multiply(price,quant))
    exchange = list(np.divide(1,price))
    #Create dic content to create df
    details = {'Currency':currency,
               'Price': price,
               'Quantity':quant,
               'Cost (USD)': cost,
               'Exchange Rate USD:COIN':exchange
              }  
    # creating a Dataframe object 
    df = pd.DataFrame(details)
    #Sum all values in the cost USD column to prompt the user what is the total of their transaction
    total_cost = df['Cost (USD)'].sum()
    #Create the two new rows to append to existing df
    new_row = {'Currency':'--','Price':'--','Quantity':'--','Cost (USD)':'--','Exchange Rate USD:COIN':'--'}
    new_row2 = {'Currency':'Total','Price':'--','Quantity':'--','Cost (USD)':total_cost,'Exchange Rate USD:COIN':'--'}
    #Append rows to df
    df2 = df.append(new_row, ignore_index=True)
    df3 = df2.append(new_row2, ignore_index=True)
    #Save last version of df into a CSV in the same folder of the workbook
    df3.to_csv('crypto_conversion.csv',index=False)


#Second Function

def closeConverter():
    """Created this function to use for the button to close the GUI"""
    root.destroy()


#Create root
root = tkinter.Tk()
root.title("Exchange rate calculator")
root.configure(bg = "light salmon")
#root.geometry("400x100")

#Create labels
btc_box = tkinter.Label(root, text = "BTC:")
btc_box.configure(bg = "light salmon")
btc_box.grid(row = 0, column = 0)

bnb_box = tkinter.Label(root, text = "BNB:")
bnb_box.configure(bg = "light salmon")
bnb_box.grid(row = 1, column = 0)

eth_box = tkinter.Label(root, text = "ETH:")
eth_box.configure(bg = "light salmon")
eth_box.grid(row = 0, column = 2)

xrp_box = tkinter.Label(root, text = "XRP:")
xrp_box.configure(bg = "light salmon")
xrp_box.grid(row = 1, column = 2)


#Placing boxes in the grid
btc_box = tkinter.Entry(root, width = 15)
btc_box.insert(0, 1)
btc_box.grid(row = 0, column = 1)

bnb_box = tkinter.Entry(root, width = 15)
bnb_box.insert(0, 1)
bnb_box.grid(row = 1, column = 1)

eth_box = tkinter.Entry(root, width = 15)
eth_box.insert(0, 1)
eth_box.grid(row = 0, column = 3)

xrp_box = tkinter.Entry(root, width = 15)
xrp_box.insert(0, 1)
xrp_box.grid(row = 1, column = 3)

#Create the buttons

convert_currency_button = tkinter.Button(root, text = "Convert Currency", command = convertCurrency)
convert_currency_button.configure(bg= 'pale green')
convert_currency_button.grid(row = 0, column = 4,sticky = "w", padx = 5, pady = 5)

convert_currency_button = tkinter.Button(root, text = "Close Converter", command = closeConverter)
convert_currency_button.configure(bg= 'dark orange')
convert_currency_button.grid(row = 1, column = 4,sticky = "w", padx = 5, pady = 5)

#init root with command 
root.mainloop()
