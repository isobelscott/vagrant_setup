#!/usr/bin/env python

import sys
import os
import currency_converter


# get the current budget available
def pull_budget(file_name):
    with open(file_name) as file:
      last_line = file.readlines()[-1]
    number = float(last_line.strip('\n').strip(' '))
    return number

#write the total to database                                    
def write_new_total(subtracted_amount):
    db_filename = "budget_database.txt"
    db_path = os.path.join('/Users/isobel/nyu-python/project1',
            db_filename)
   
    with open(db_path, "a") as myfile:
        myfile.write(subtracted_amount)
        myfile.write("\n")

if __name__ == '__main__': 
    # get the currency and the cost of the thing in that currency
    currency = input("What foreign currency are you using? ")
    foreign_cost  = input("Enter the amount: ")
    # define the costs
    usd_cost = currency_converter.foreign_currency_to_usd(foreign_cost, currency)
    file_name = "budget_database.txt"
    new_total = str(pull_budget(file_name) - float(usd_cost))
    print("You have spent " + str(round(foreign_cost), 2))
    print("Which is $" + str(round(usd_cost, 2)) + " USD")
    pull_budget("budget_database.txt")
    write_new_total(new_total)
    new_budget = pull_budget("budget_database.txt")
    new_budget_fc = currency_converter.usd_to_foreign_currency(new_budget, currency)
    print("Your new budget is" + " $" + str(round(new_budget, 2)) + " USD.") 
    print("Which is " + str(round(new_budget_fc, 2)) + " in " + str(currency))
