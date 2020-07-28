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

def surname():

def phoneNumber():



#User Data Collection
def userInput():
    if continueInput == 1:
        firstName()
    else:
        runConsole()
    if continueInput == 1:
        surname()
    else:
        runConsole()
    if continueInput == 1:
        phoneNumber()
    else:
        runConsole()

#Console
def runConsole():
    print("Hi")


#Run Program Functions
userInput()
