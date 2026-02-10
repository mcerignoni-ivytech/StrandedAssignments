"""
Author: Marco Antônio Sanches Cerignoni
File Name: M02 Lab.py
Description: This application accepts student names and GPAs. It checks if the 
             student qualifies for the Dean's List (GPA 3.5+) or the Honor 
             Roll (GPA 3.25+) and prints a corresponding message. Processing 
             stops when the last name 'ZZZ' is entered.
"""

print("--- Student Academic Recognition App ---")

while True:
    #Ask for last name
    last_name = input("\nEnter the student's last name (Enter 'ZZZ' to quit): ")
    
    #Quit if the last name entered is 'ZZZ'
    if last_name == "ZZZ":
        print("Processing complete.")
        break
        
    #Ask for first name
    first_name = input("Enter the student's first name: ")
    
    #Ask for GPA as a float
    try:
        gpa = float(input("Enter the student's GPA: "))
    except ValueError:
        print("Invalid input. Please enter a numeric GPA.")
        continue

    #Test if student qualifies for Dean list
    if gpa >= 3.5:
        print(f"Result: {first_name} {last_name} has made the Dean's List.")
        
    #Test if student qualifies for Honor Roll
    elif gpa >= 3.25:
        print(f"Result: {first_name} {last_name} has made the Honor Roll.")
        
    else:
        print(f"Result: {first_name} {last_name} did not qualify for special recognition.")