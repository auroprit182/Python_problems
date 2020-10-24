# -*- coding: utf-8 -*-
"""
Spyder Editor

Calculate interest at end of each year using Decimal.
Decimal gives accurate representation instead of approx as given by float which gets stored as binary in memory

"""

from decimal import Decimal

principal = Decimal('1000')
rate = Decimal('0.05')

for time in range(1,11):
    amount = principal * ((1+rate)**time)
    # >2 indicates right alligned with field width 2
    print(f"The amount of money at end of {time:>2} year is {amount:>10.2f}") 

