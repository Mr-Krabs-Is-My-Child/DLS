#Imports for program operation
import time
import os
import datetime

#Variables
first = ""
surname = ""
phoneNumber = ""
fullName = ""
userFile = ""
timeStr = datetime.datetime.now()
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
    global first
    global firstNameLoop
    global commandCode
    while firstNameLoop == True:
        try:
            first = str(input("First?"))
        except ValueError:

            print("ValueError")
        else:
            firstNameLoop = False
            if first == "CMD":
                first = ""
                runConsole()
            else:
                surname()


def surname():
    global surname
    global surnameLoop
    global commandCode
    while surnameLoop == True:
        try:
            surname = str(input("Surname?"))
        except ValueError:

            print("ValueError")
        else:
            surnameLoop = False
            if surname == "CMD":
                surname = ""
                runConsole()
            else:
                phoneNumber()

def phoneNumber():
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
            phoneNumber = str(input("Phone Number?"))
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
                        userFile = open((fullName + ".txt"),"x")
                        userFile.close()
                        createFile = False
                        userFile = open((fullName + ".txt"),"a")
                        userFile.write(first)
                        userFile.write(surname)
                        userFile.write(phoneNumber)
                        userFile.write(timeStr)
                    except FileExistsError:
                        print("File Exists Error")
                        fullName = fullName + "_Test"



#Console
def runConsole():
    print("Test Console")


#Run Program Functions
firstName()
