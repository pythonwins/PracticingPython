# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:02:00 2018

@author: dhoop
"""
import math
def get_num():
    num = int(input("Please enter a number: "))
    i = 1
    while i <= math.sqrt(num):
        i = i + 1
        if num % i == 0:
            if num / i == i:
                print (i)
               
            else:
                
                print (i, num/i)
               
    
get_num()
               
              
