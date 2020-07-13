# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 00:51:03 2020

@author: Suyash Chavan
"""
'''
x = 5
print(x)

x_data = {5,5.98,"hey there",4+6}
print(x_data)
'''
'''
FOUR BUILT-IN DATA STRUCTURES
1] LIST []
2] TUPLE()
3] Dicctionary{} with key value pair
4] Set {}
'''

'''
#---------------LIST--------------#
#Combination of data(each data is indexed 0 to - for left to right and -1 to -number for right to left)

my_list = [3,2,2,1,21,"Suyash",8.3476377,2,2,2,2]

print(my_list)
print(bool(my_list))

print(my_list[-3])

print(my_list[5][0:4])

print(my_list[:]) #prints the whole list

my_list[0] = "LOLOLOL"  #LISTS ARE MUTABLE, can be changed basically
print(my_list)

my_list[0] = "JKJK"

print(my_list)

#print(dir(my_list))


['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


print(my_list.index(2,2)) #displays the index at which "1" is present

print(my_list.count(2))

my_copy_list = my_list.copy();

print(fr'{my_copy_list},{id(my_copy_list)}')

my_copy_list.insert(2,4545353535353535353)

print(my_copy_list)

my_list.append(my_copy_list)
print(my_list)

my_list.extend(my_copy_list)
print(my_list)


list_l = [5.6, 3.3, 2, 33, 2, 2, 2]
abc = list_l.pop(2)

print(abc)

list_l.sort()
print(list_l)

#print(my_list.sort())

'''

'''
#-------------------TUPLES----------------#

#TUPLES ARE IMMUTABLE DATATYPES


my_tuple = (4,[34435,33,34,4,4,453],5,3443,4,56)
 
print(my_tuple)

print(my_tuple[5])

print(my_tuple[1][0:3])

print(my_tuple[:]) 

x=5, #it is single item tuple

print(x,type(x))

y=5,5,4,3,

print(y,type(y))

'''

'''
#------------------DICTIONARY-----------------#

#python2 had unordered dictionary while python3 has ordered dictionary following the user defined order of the dictionary elements

my_dict = {}

print(my_dict,type(my_dict))

print(bool(my_dict))

#my_dict = {'key':'value',key:'value','key':'value'}
my_dict = {'fruit':'mango',1:'number','animal':'elephant'}
print(my_dict)

print(my_dict['fruit'])

print(my_dict.get('fruit'))

my_dict['lololol'] = 'lmao'
print(my_dict)

my_dict['lololol'] = 'all_serious'
print(my_dict)

print(my_dict.keys())

print(my_dict.values())

print(my_dict.items())

xyz = my_dict.copy()

print(id(my_dict), id(xyz))

print(xyz)

y = my_dict.pop('fruit')

print(y)

y = my_dict.popitem()

print(my_dict)

print(y)
'''

'''
#--------------------------SETS---------------------#

new_set = {4,4,3,4,2,4,45,2,2,1,11,4343434}
print(new_set)

new_set = set({})

print(type(new_set),new_set)

print(bool(new_set))

my_list = [535,3,3,3,4,2,2]

print(my_list)

print(set(my_list)) #prints unique elements of the list.

'''
