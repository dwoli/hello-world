import imp
from msilib import _directories
from unittest import result
#user defined module

#import my_module
#print(dir(my_module))

#my_module.my_func()
#result= my_module.add_numbers(1,2)
#print(result)

#built-in module

#import math as m

#x= m.factorial(3)
#print(x)

#x= m.sqrt(16)
#print(x)

#import random as r

#r.seed(10)
#print(r.random())

#print(r.randrange(35,40))

#print(r.randint(2,8))

#mylist = ["apple", "banana", "cherry"]
#r.shuffle(mylist)

#print(mylist)
#print(r.choice(mylist))

#import datetime as dt
#print(dt.datetime.now())

#import os
#cwd= os.getcwd()
#directories= os.listdir(cwd)
#print(cwd)
#print(directories)

#import sys
#pathforallmodules=sys.path
#print(pathforallmodules)

#modules attributes

import math
import my_module

math.__name__ 
my_module.__name__ 


