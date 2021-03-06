# The program will first run the disclaimer code, and this will run the first name input function. The code will then
# decide to either open the command window when parameters are met, or to continue onto the next input function.
# This will continue to loop forever unless the program is either closed or killed using the "kill" command in the
# command console

# Imports for program operation
import sys
import time
import os
from datetime import datetime


# Variables for program operation
firstName = ""
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
        # Default Disclaimer
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
        # Continue program after reading the disclaimer
        print("\n")
        firstNameFN()

# Clear console for protecting data
clear = lambda: os.system("cls")

# User input functions

# Function asks for first name input and continues accordingly
def firstNameFN():
    global firstName
    # Input Loop
    while True:
        print("Please type your first name in the bar below")
        try:
            firstName = str(input("[-->]"))
        except ValueError:
            print("I'm sorry. There was an error")
        # Evaluating first name input
        else:
            # Checks if the user is requesting the command console
            if firstName == "CMD":
                firstName = ""
                runConsole()
                break
            # Check for numbers
            elif firstName.isalpha() == False:
                print("That name contains numbers and/or special characters. Please enter a name that does not contain numbers or special characters")
            # Empty Prompt
            elif firstName == "":
                print("I'm sorry, but that isn't actually a name")
                print("\n")
            elif firstName == "Anakin":
                print("You are the chosen one!")
                print("\n")
                surnameFN()
                break
            else:
                # Continue input sequence if CMD is not detected
                print("\n")
                surnameFN()
                break

# If the first name is not CMD then this function is run
def surnameFN():
    global surname
    while True:
        print("Please type your surname into the bar below")
        try:
            surname = str(input("[-->]"))
        except ValueError:

            print("I'm sorry. There was an error")
        # Evaluating surname input
        else:
            # Checks if the user is requesting the command console
            if surname == "CMD":
                surname = ""
                runConsole()
                break
            # Check for numbers
            elif surname.isalpha() == False:
                print("That name contains numbers and/or special characters. Please enter a name that does not contain numbers or special characters")
            # Empty Prompt
            elif surname == "":
                print("I'm sorry, but that isn't actually a surname")
                print("\n")
            elif surname == "Kenobi":
                print("Hello There")
                print("\n")
                phoneNumberFN()
                break
            else:
                # Continue input sequence if CMD is not detected
                print("\n")
                phoneNumberFN()
                break

# If the surname is not CMD then this function is run
def phoneNumberFN():
    # Global variables for writing to files
    global phoneNumber
    global fullName
    global firstName
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
            # Checks if the user is requesting the command console
            if phoneNumber == "CMD":
                phoneNumber = ""
                runConsole()
                break
            # Empty Prompt
            elif phoneNumber == "":
                print("I'm sorry, but you've left it empty")
                print("\n")
            # Check for letters / special characters
            elif phoneNumber.isdigit() == False:
                print("That phone number contains letters and/or special characters")
            else:
                print("Thank you for you co-operation. We will contact you if necessary")
                time.sleep(5)
                fullName = firstName + "_" + surname
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
                        userFile.write(firstName)
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
                        print("File Exists. Creating new file")
                        fullName = fullName + "_1"


# Console function runs if any input is CMD
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
            print("\n")
            try:
                print("The current disclaimer reads:")
                disclaimerFile = open("Disclaimer.txt", "r")
                print(disclaimerFile.read())
                disclaimerFile.close()
                print("\n")
                print("Type your disclaimer below, or type reset to set the disclaimer to its default message. Leave this open to cancel")
                edit = str(input("[-->]"))
                # Code to reset disclaimer
                resetList = ["reset", "Reset", "RESET"]
                if edit in resetList:
                    print("Reset Disclaimer")
                    disclaimerFile = open("Disclaimer.txt", "w")
                    disclaimerFile.write("""Welcome visitor. Please follow the console's instructions so that we may collect some data.
This Data will be used by us if we may need to contact you for various reasons, and it helps
us keep track of our visitors. Your information will not be used anywhere else. By entering
your information, you agree that you have read this and accept the terms. Thank you for paying
attention""")
                    disclaimerFile.close()
                elif edit == "":
                    # Cancels disclaimer editing if the input is empty
                    print("Cancelling...")
                else:
                    editDisclaimer = open("Disclaimer.txt","w")
                    editDisclaimer.write(edit)
                    editDisclaimer.close()
            # Disclaimer not found
            except FileNotFoundError:
                print("Disclaimer.txt File Not Found")
        elif runCMD == "kill":
            # Kills program
            sys.exit()
        elif runCMD =="recent entries":
            # Recent Entries
            if len(recentEntries) == 0:
                print("There are no recent entries")
            else:
                # Option to clear recent entries list if it is not empty
                print("The recent entries include:")
                print(recentEntries)
                print("Would you like to clear the recent entries? Type [Y] to clear")
                clearRecent = str(input("[-->]"))
                clearRecent = clearRecent.lower()
                # Clears the recent entries
                if clearRecent == "y":
                    recentEntries.clear()
                    print("The recent entries have been removed")
                else:
                    print("Returning to console...")
        elif runCMD == "search":
            # Search command
            print("Please enter the requested name below")
            try:
                # Gets user input for file name and attempts to locate it. If it is found it will be opened
                search = str(input("[-->]"))
                search = search + ".txt"
                print("Found file {}".format(search))
                print("\n")
                f = open(search,"r")
                print(f.read())
                f.close()
                print("\n")
            except FileNotFoundError:
                # Presents file not found error to user
                print("File {} not found".format(search))
        elif runCMD == "exit":
            # Resumes program
            clear()
            disclaimerFN()
            break
        # Roger easter egg
        elif runCMD == "roger":
            print("Roger Roger")
            print("\n")
        # 66 easter egg
        elif runCMD == "66":
            print("Of course, my Lord...")
            time.sleep(3)
            print("\n")
            print("...Wait, I'm not a clone")
        else:
            # Do this if the input is not listed
            print("Command was not recognized. Please try again")
            print("\n")


# Call for disclaimerFN to start function loop
disclaimerFN()

