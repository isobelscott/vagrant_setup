#!/usr/bin/env python

import sys
import os
import converter

# Get remaining budget

def getrest(dbFilename):
    with open('budget_database.txt') as dbFilename:
        lines = dbFilename.readlines()
        remaining_budget = float(lines[-1])
        return remaining_budget

# Put new budget in the file

def savebudget(budgetfloat):
    dbPath = '/Users/isobel/nyu-python/Project1V2/budget_database.txt'
    with open(dbPath, "a") as myfile:
        myfile.write(str(budgetfloat).strip() + "\n")


# do the whole thing: convert, substract budget, convert back again, give infomation

if __name__ == "__main__":

    get_currency = input("What currency are you using? ").upper() 
    get_amount = float(input("How much does it cost? "))
    
    while True:
        try:
            get_amount_usd = converter.foreign_currency_to_usd(get_amount, get_currency)
        except KeyError:
            print("That is not a supported currency.") 
            break
        except ValueError:
            print("That is not a number.")
            break
        
        old_budget = getrest('budget_database.txt')
        new_budget = float(old_budget) - float(get_amount)
        new_budget_fc = converter.usd_to_foreign_currency(new_budget, get_currency)
        savebudget(new_budget)
        print("You spent " + str(round(get_amount, 2)) + " " +  str(get_currency) + ".")
        print("Which is $" + str(round(get_amount_usd, 2))  + " USD.")
        print("Your remaining budget is $" + str(round(new_budget, 2)) + " USD.")
        print("Which is " + str(round(new_budget_fc, 2)) + " " + str(get_currency) + ".")
        break
