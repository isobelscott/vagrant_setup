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
        myfile.write(str(round(budgetfloat, 2)).strip() + "\n")


# do the whole thing: convert, substract budget, convert back again, give infomation

if __name__ == "__main__":

    get_currency = input("What currency are you using? ").upper() 
    get_amount = float(input("How much does it cost? "))
    
    while True:
        try:
            get_amount_usd = round(converter.foreign_currency_to_usd(get_amount, get_currency), 2)
        except KeyError:
            print("That is not a supported currency. The supported foreign currencies are AUS, GBP, CAD, EUR, and MXN.") 
            break
        except ValueError:
            print("That is not a number.")
            break
        
        old_budget = getrest('budget_database.txt')
        new_budget = float(old_budget) - float(get_amount)
        new_budget_fc = converter.usd_to_foreign_currency(new_budget, get_currency)
        savebudget(new_budget)
        print("You spent " + str(round(get_amount, 2)) + " " +  str(get_currency) + ".")
        print("Which is $" + str(get_amount_usd)  + " USD.")
        print("Your remaining budget is $" + str(round(new_budget, 2)) + " USD.")
        print("Which is " + str(round(new_budget_fc, 2)) + " " + str(get_currency) + ".")
        break
