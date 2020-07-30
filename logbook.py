#Imports for program operation
import time
import os
from datetime import datetime

#Variables
try:
    commandFile = open("Program Data","r")
    commandCode = commandFile.readline()
    commandFile.close()
except FileNotFoundError:
    print('File"Program" Data not found')
continueInput = 1
firstNameLoop = 1
surnameLoop = 1
phoneNumberLoop = 1
#Recent Entries List
recentEntries = []

#Disclaimer Function
def disclaimer():
    try:
        disclaimerFile = open("Disclaimer","r")
        print(disclaimerFile.read())
        disclaimerFile.close()
    except FileNotFoundError:
        print("Disclaimer file not found")

#Program Functions
def firstName():
    global firstNameLoop
    print("Test Firstname")
    while firstNameLoop == 1:
        try:
            first = str(input("First"))
            firstNameLoop = 0
        except ValueError:
            print("Value Error Message")
def surname():
    print("Test Surname")

def phoneNumber():
    print("Test Phone")


#User Data Collection
def userInput(continueInput):
    if continueInput == 1:
        firstName()
    elif continueInput == 0:
        runConsole()
    else:
        continueInput = 2
    if continueInput == 1:
        surname()
    elif continueInput == 0:
        runConsole()
    else:
        continueInput = 2
    if continueInput == 1:
        phoneNumber()
    elif continueInput == 0:
        runConsole()
    else:
        continueInput = 1
        firstNameLoop = 1
        surnameLoop = 1
        phoneNumberLoop = 1


#Console
def runConsole():
    print("Test Console")


#Run Program Functions
userInput(continueInput)
