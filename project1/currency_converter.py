#!/usr/bin/env python

import sys

def foreign_currency_to_usd(foreign_cost, currency):
    usd_dict = {"GBP": 1.30, "AUS": 0.77, "EUR": 1.14}
    value_usd_to_fc = usd_dict[currency]
    usd = round((foreign_cost * value_usd_to_fc), 2)
    return usd

def usd_to_foreign_currency(usd, currency):
    fc_dict = {"GBP": 0.77, "AUS": 1.30, "EUR": 0.88}
    value_fc_to_usd = fc_dict[currency]
    foreign_currency = round((usd * value_fc_to_usd), 2)
    return foreign_currency
