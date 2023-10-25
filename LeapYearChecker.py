# Program name: LeapYearChecker.py
# Checks to see whether a year is a leap year or not.

print("[Leap Year Checker]")
print("\nWelcome! This is where you can check to see if a year is a leap year or not.")

year = int(input("Enter the year you want to check: ")) # Allows for the user to input the year
if (year % 400 == 0): # If the year is divisible by 400, it is a leap year
    print("This year is a leap year.")
    
elif (year % 4 == 0):
    print("This year is a leap year.") # If the year is divisible by 4, it is a leap year
    

elif (year % 100 == 0):
    print("This year is not a leap year.") 
    
else:
    print("This year is not a leap year.")