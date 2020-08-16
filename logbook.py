# Imports for program operation
import sys
import time
import os
from datetime import datetime

# Variables for program operation
first = ""
surname = ""
phoneNumber = ""
fullName = ""
userFile = ""
timeStr = ""
continueInput = True
firstNameLoop = True
surnameLoop = True
phoneNumberLoop = True

# Lists for program operation
recentEntries = []
commandList = ["Edit Disclaimer","Kill","Recent Entries","Search"]


# Disclaimer Function
def disclaimerFN():
    global firstNameLoop
    global surnameLoop
    global phoneNumberLoop
    firstNameLoop = True
    surnameLoop = True
    phoneNumberLoop = True
    try:
        disclaimerFile = open("Disclaimer", "r")
        print(disclaimerFile.read())
        disclaimerFile.close()
    except FileNotFoundError:
        # Print an error message, Add code to create Disclaimer with default text if one is not found
        print("Disclaimer file not found. Creating new disclaimer file")
        disclaimerFile = open("Disclaimer", "a")
        disclaimerFile.write("Default disclaimer")
        disclaimerFile.close()
        disclaimerFile = open("Disclaimer", "r")
        print(disclaimerFile.read())
        disclaimerFile.close()
    finally:
        firstNameFN()


# User input functions
def firstNameFN():
    global first
    global firstNameLoop
    global commandCode
    # Input Loop
    while firstNameLoop == True:
        try:
            print("Please input you First name:")
            first = str(input("[-->]"))
        except ValueError:
            print("ValueError")
        else:
            firstNameLoop = False
            if first == "CMD":
                first = ""
                runConsole()
            else:
                # Continue input sequence if CMD is not detected
                surnameFN()


def surnameFN():
    global surname
    global surnameLoop
    global commandCode
    while surnameLoop == True:
        try:
            print("Please input you Surname:")
            surname = str(input("[-->]"))
        except ValueError:

            print("ValueError")
        else:
            surnameLoop = False
            if surname == "CMD":
                surname = ""
                runConsole()
            else:
                # Continue input sequence if CMD is not detected
                phoneNumberFN()


def phoneNumberFN():
    # Global variables for writing to files
    global phoneNumber
    global phoneNumberLoop
    global commandCode
    global fullName
    global first
    global surname
    global userFile
    global timeStr
    createFile = True
    while phoneNumberLoop == True:
        try:
            print("Please enter your phone number, so that we may contact you if necessary")
            phoneNumber = str(input("[-->]"))
        except ValueError:

            print("ValueError")
        else:
            phoneNumberLoop = False
            if phoneNumber == "CMD":
                phoneNumber = ""
                runConsole()
            else:
                print("Thank you message")
                fullName = first + "_" + surname
                recentEntries.append(fullName)
                while createFile == True:
                    try:
                        # User file creation and writing
                        userFile = open((fullName + ".txt"), "x")
                        userFile.close()
                        createFile = False
                        # Datetime to string formatting
                        dateTime = datetime.now()
                        timeStr = dateTime.strftime("%a %d %b %Y (%H:%M:%S)")
                        # Open file for appending and adding stored data to file
                        userFile = open((fullName + ".txt"), "a")
                        userFile.write(first)
                        userFile.write(" ")
                        userFile.write(surname)
                        userFile.write("\n")
                        userFile.write(phoneNumber)
                        userFile.write("\n")
                        userFile.write(timeStr)
                        userFile.close()
                        disclaimerFN()
                        # End of user input sequence
                    except FileExistsError:
                        print("File Exists Error")
                        fullName = fullName + "_Test"


# Console
def runConsole():
    while True:

        global firstNameLoop
        global surnameLoop
        global phoneNumberLoop
        firstNameLoop = False
        surnameLoop = False
        phoneNumberLoop = False
        global commandList
        global recentEntries
        print("Available commands:")
        print(commandList)
        runCMD = str(input("Command Entry"))
        runCMD = runCMD.lower()
        # Console commands
        if runCMD == "edit disclaimer":
            # Edit Disclaimer command
            print("Edit disclaimer")
        elif runCMD == "kill":
            # Kills program
            sys.exit()
        elif runCMD =="recent entries":
            # Recent Entries
            print("The recent entries include:")
            print(recentEntries)
        elif runCMD == "search":
            # Search command
            print("search")
            try:
                search = str(input("Search name"))
                search = search + ".txt"
                print("Found file {}".format(search))
                f = open(search,"r")
                print(f.read())
                f.close()
            except FileNotFoundError:
                print("File not found")
        elif runCMD == "exit":
            disclaimerFN()
            break
        else:
            print("Not recognized")


# Run Program Functions
disclaimerFN()
