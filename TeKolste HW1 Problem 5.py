# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 20:17:46 2018

@author: Becca
"""

#TeKolste HW1 Problem 5

word = str(input("Which month are you looking for? Enter a word: "))
print(word + " is the")
if word=="January":
    print("first month.")
elif word=="February":
    print("second month.")
elif word=="March":
    print("third month.")
elif word=="April":
    print("forth month.")
elif word=="May":
    print("fifth month.")
elif word=="June":
    print("sixth month.")
elif word=="July":
    print("seventh month.")
elif word=="August":
    print("eighth month.")
elif word=="September":
    print("ninth month.")
elif word=="October":
    print("tenth month.")
elif word=="November":
    print("eleventh month.")
elif word=="December":
    print("twelfth month.")

month = [1, "January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December"]
num = int(input("Which month are you looking for? Enter a number: "))
print(month[num] + " is month " + str(num) + ".")
