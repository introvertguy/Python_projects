# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 00:26:31 2020

@author: Suyash Chavan
"""

my_string = "WADDUP"

print(my_string)

print(my_string.lower()) #casefold works similar

my_string_upper = my_string.upper()
print(my_string_upper)

#print(dir(my_string)) #displays all possible string functions

my_string1 = "well hello there!"

my_new = my_string1.capitalize()

print(my_new)

my_new1 = my_string1.swapcase()
print(my_new1)

#BOOLEAN RESULTS OPERATIONS

print(my_string1.endswith('?'))

print(my_string1.endswith('!'))


#islower, isupper, isspace,istitle, isalpha(only alphabets?) --> access mulitple others using print(dir(string_name)) 

print(my_string1.isspace())
