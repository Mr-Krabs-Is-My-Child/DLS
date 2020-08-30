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


# Lists for program operation
recentEntries = []
commandList = ["Edit Disclaimer","Kill","Recent Entries","Search","Exit"]


# Disclaimer.txt Function
def disclaimerFN():
    try:
        disclaimerFile = open("Disclaimer.txt", "r")
        print(disclaimerFile.read())
        disclaimerFile.close()
    except FileNotFoundError:
        # Print an error message, Add code to create Disclaimer with default text if one is not found
        print('File "Disclaimer.txt" not found. Creating new disclaimer file with default disclaimer message')
        print("\n")
        time.sleep(2)
        disclaimerFile = open("Disclaimer.txt", "a")
        disclaimerFile.write("""Welcome visitor. Please follow the console's instructions so that we may collect some data.
This Data will be used by us if we may need to contact you for various reasons, and it helps
us keep track of our visitors. Your information will not be used anywhere else. By entering
your information, you agree that you have read this and accept the terms. Thank you for paying
attention""")
        disclaimerFile.close()
        disclaimerFile = open("Disclaimer.txt", "r")
        print(disclaimerFile.read())
        disclaimerFile.close()
    finally:
        print("\n")
        firstNameFN()

#Clear console for protecting data
clear = lambda: os.system("cls")

# User input functions
def firstNameFN():
    global first
    # Input Loop
    while True:
        print("Please type your first name in the bar below")
        try:
            first = str(input("[-->]"))
        except ValueError:
            print("ValueError")
        # Evaluating first name input
        else:
            if first == "CMD":
                first = ""
                runConsole()
                break
            elif first.isalpha() == False:
                print("That name contains numbers. Please enter a name that does not contain numbers")
            elif first == "":
                print("I'm sorry, but that isn't actually a name")
                print("\n")
            else:
                # Continue input sequence if CMD is not detected
                print("\n")
                surnameFN()
                break


def surnameFN():
    global surname
    while True:
        print("Please type your surname into the bar below")
        try:
            surname = str(input("[-->]"))
        except ValueError:

            print("ValueError")
        # Evaluating surname input
        else:
            if surname == "CMD":
                surname = ""
                runConsole()
                break
            elif surname.isalpha() == False:
                print("That surname contains numbers. Please enter a surname that does not contain numbers")
            elif surname == "":
                print("I'm sorry, but that isn't actually a surname")
                print("\n")
            else:
                # Continue input sequence if CMD is not detected
                print("\n")
                phoneNumberFN()
                break


def phoneNumberFN():
    # Global variables for writing to files
    global phoneNumber
    global fullName
    global first
    global surname
    global userFile
    global timeStr
    while True:
        print("Please enter your phone number, so that we may contact you if necessary")
        try:
            phoneNumber = str(input("[-->]"))
        except ValueError:
            print("I'm sorry, but that's not a phone number")
        # Evaluating phone number input
        else:
            if phoneNumber == "CMD":
                phoneNumber = ""
                runConsole()
                break
            elif phoneNumber == "":
                print("I'm sorry, but you've left it empty")
                print("\n")
            elif phoneNumber.isdigit() == False:
                print("That phone number contains letters and/or special characters")
            else:
                print("Thank you for you co-operation. We will contact you if necessary")
                fullName = first + "_" + surname
                recentEntries.append(fullName)
                while True:
                    try:
                        # User file creation and writing
                        userFile = open((fullName + ".txt"), "x")
                        userFile.close()
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
                        # Clear Console
                        clear()
                        disclaimerFN()
                        break
                        # End of user input sequence
                    except FileExistsError:
                        print("File Exists Error")
                        fullName = fullName + "_1"


# Console
def runConsole():
    clear()
    while True:
        global commandList
        global recentEntries
        print("Available commands:")
        print(commandList)
        print("Please enter a command")
        runCMD = str(input("[-->]"))
        runCMD = runCMD.lower()
        # Console commands
        if runCMD == "edit disclaimer":
            # Edit Disclaimer command
            print("Opening Disclaimer for editing.....")
            try:
                print("Type your disclaimer below, or type reset to set the disclaimer to its default message. Leave this open to cancel")
                edit = str(input("[-->]"))
                resetList = ["reset", "Reset", "RESET"]
                if edit in resetList:
                    print("Reset")
                    disclaimerFile = open("Disclaimer.txt", "w")
                    disclaimerFile.write("""Welcome visitor. Please follow the console's instructions so that we may collect some data.
This Data will be used by us if we may need to contact you for various reasons, and it helps
us keep track of our visitors. Your information will not be used anywhere else. By entering
your information, you agree that you have read this and accept the terms. Thank you for paying
attention""")
                    disclaimerFile.close()
                elif edit == "":
                    print("Cancelling...")
                else:
                    editDisclaimer = open("Disclaimer.txt","w")
                    editDisclaimer.write(edit)
                    editDisclaimer.close()
            except FileNotFoundError:
                print("Disclaimer.txt File Not Found")
        elif runCMD == "kill":
            # Kills program
            sys.exit()
        elif runCMD =="recent entries":
            # Recent Entries
            print("The recent entries include:")
            print(recentEntries)
        elif runCMD == "search":
            # Search command
            print("Please enter the requested name below")
            try:
                search = str(input("[-->]"))
                search = search + ".txt"
                print("Found file {}".format(search))
                f = open(search,"r")
                print(f.read())
                f.close()
            except FileNotFoundError:
                print("File {} not found".format(search))
        elif runCMD == "exit":
            # Resumes program
            clear()
            disclaimerFN()
            break
        else:
            # Do this if the input is not listed
            print("Command was not recognized. Please try again")


# Run Program Functions
disclaimerFN()

