"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 4 inputs have 'while' loop validation.
[ ] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[ ] 4. I have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""
# Assignment – Registration Practice
# Name: Humza Bangash

# Get first name (cannot be blank)
first_name = input(f"Enter first name:")
while first_name == "":
    print(f"Error: First name cannot be blank")
    first_name = input(f"Please enter first name:")

# Get last name (cannot be blank)
last_name = input(f"Enter last name:")
while last_name == "":
    print(f"Error: Last name cannot be blank")
    last_name = input(f"Please enter last name:")

# Confirm there is a chaperone
chaperone = input(f"Chaperone present?")
while chaperone != "Y" and chaperone != "N" and chaperone != "y" and chaperone != "n":
    print(f"Error: please enter only Y or N.")
    chaperone = input("Chaperone present?:")

# Get the phone number
phone_number = input("Enter phone number: ")
while phone_number == "":
    print("Error: Phone number cannot be blank.")
    phone_number = input("Please enter phone number: ")

# Get ticket count (must be integer > 0, crash-proof)
while True:
    try:
        ticket_count = int(input("Enter number of tickets: "))
        if ticket_count > 0:
            break
        else:
            print("Error: Ticket count must be greater than 0.")
    except ValueError:
        print("Error: Please enter a valid whole number.")