#Imports for program operation
import time
import os
from datetime import datetime

#Variables

continueInput = True
firstNameLoop = True
surnameLoop = True
phoneNumberLoop = True

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
    global commandCode
    print("Test First")
    while firstNameLoop == True:
        try:
            first = str(input("First?"))
        except ValueError:

            print("ValueError")
        else:
            firstNameLoop = False
            if first == "CMD":
                runConsole()
            else:
                pass


def surname():
    print("Test Surname")

def phoneNumber():
    print("Test Phone")


#User Data Collection
def userInput():
    print("User Input Function")



#Console
def runConsole():
    print("Test Console")


#Run Program Functions
userInput()
firstName()
