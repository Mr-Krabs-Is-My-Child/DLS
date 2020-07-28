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

#User Data Collection
def userInput():
    firstName = str(input("Name?"))
