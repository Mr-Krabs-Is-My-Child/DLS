#Imports for program operation
import time
import os
from datetime import datetime

#Disclaimer Function
def disclaimer():
    try:
        disclaimerFile = open("Disclaimer")
        print(disclaimerFile.read())
        disclaimerFile.close()
    except FileNotFoundError:
        print("Disclaimer file not found")
