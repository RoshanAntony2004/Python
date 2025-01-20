Exercise 1
Aim:
To create a Python program that demonstrates the use of basic data types and various operators 
Program:
# Various Data Types in Python
# Integer and Float
num1 = int(input("Enter an integer: "))
num2 = float(input("Enter a float: "))

# String
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# List
my_list = [num1, num2, str1, str2]

# Tuple
my_tuple = (num1, num2)

# Set
my_set = {num1, num2}

# Dictionary
my_dict = {
    'integer': num1,
    'float': num2,
    'first_string': str1,
    'second_string': str2
}

# Boolean
bool1 = True
bool2 = False

# Arithmetic Operations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 if num2 != 0 else "undefined (cannot divide by zero)"
remainder = num1 % num2
exponentiation = num1 ** 2
floor_division = num1 // 2

# Comparison Operators
is_equal = num1 == num2
is_not_equal = num1 != num2
is_greater = num1 > num2
is_less_or_equal = num1 <= num2

# Logical Operators
logical_and = bool1 and bool2
logical_or = bool1 or bool2
logical_not = not bool1

# Bitwise Operators
bitwise_and = num1 & 1
bitwise_or = num1 | 1
bitwise_xor = num1 ^ 1

# Membership Operators
is_in_list = num1 in my_list
is_in_dict = 'integer' in my_dict

# Print Results
print(f"\nArithmetic Results:")
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")
print(f"{num1} raised to the power of 2: {exponentiation}")
print(f"Floor division of {num1} by 2: {floor_division}")

print(f"\nComparison Results:")
print(f"Is {num1} equal to {num2}? : {is_equal}")
print(f"Is {num1} not equal to {num2}? : {is_not_equal}")
print(f"Is {num1} greater than {num2}? : {is_greater}")
print(f"Is {num1} less than or equal to {num2}? : {is_less_or_equal}")

print(f"\nLogical Results:")
print(f"{bool1} AND {bool2} : {logical_and}")
print(f"{bool1} OR {bool2} : {logical_or}")
print(f"NOT {bool1} : {logical_not}")

print(f"\nBitwise Results:")
print(f"{num1} AND 1: {bitwise_and}")
print(f"{num1} OR 1: {bitwise_or}")
print(f"{num1} XOR 1: {bitwise_xor}")

print(f"\nMembership Results:")
print(f"Is {num1} in the list? : {is_in_list}")
print(f"Is 'integer' a key in the dictionary? : {is_in_dict}")

print(f"\nData Structures:")
print(f"List: {my_list}")
print(f"Tuple: {my_tuple}")
print(f"Set: {my_set}")
print(f"Dictionary: {my_dict}")
Result:
The Python program was successfully created to demonstrate basic data types and operators, allowing users to perform and view results of various operations.
________________________________________________________________________________________________________________________________________________________________

Exercise 2
Aim:
To create a calculator program that performs various mathematical operations and functions based on user input 
Program:
import math

# Display the available operations to the user
print("\nAvailable operations:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Square Root (√)")
print("6. Exponentiation (x^y or exp)")
print("7. Sine (sin) in radians")
print("8. Cosine (cos) in radians")
print("9. Tangent (tan) in radians")
print("10. Logarithm (log base 10)")

# Get the user's choice of operation
operation = int(input("\nChoose an operation (1-10): "))

# Handle operations that require two numbers
if operation in [1, 2, 3, 4, 6]:
    num1 = float(input("\nEnter the first number: "))
    num2 = float(input("Enter the second number: "))

# Handle operations that require only one number
elif operation in [5, 7, 8, 9, 10]:
    num1 = float(input("Enter the number: "))
    
else:
    print("\nInvalid operation! Please choose a valid option.")
    exit()

# Perform the chosen operation using the math functions
if operation == 1:  # Addition
    result = num1 + num2
elif operation == 2:  # Subtraction
    result = num1 - num2
elif operation == 3:  # Multiplication
    result = num1 * num2
elif operation == 4:  # Division
    result = num1 / num2 if num2 != 0 else "undefined (cannot divide by zero)"
elif operation == 5:  # Square Root
    result = math.sqrt(num1) if num1 >= 0 else "undefined (negative number)"
elif operation == 6:  # Exponentiation (x^y or exp)
    result = math.pow(num1, num2)  # Raises num1 to the power of num2
elif operation == 7:  # Sine
    result = math.sin(math.radians(num1))  # Convert degrees to radians before calculating
elif operation == 8:  # Cosine
    result = math.cos(math.radians(num1))  # Convert degrees to radians before calculating
elif operation == 9:  # Tangent
    result = math.tan(math.radians(num1))  # Convert degrees to radians before calculating
elif operation == 10:  # Logarithm (base 10)
    result = math.log10(num1) if num1 > 0 else "undefined (non-positive number)"

# Display the result of the operation
print(f"\nResult: {result}")

# Optionally print a message when the calculator ends
print("\nCalculator program ended.")
Result:
The Python calculator program was successfully created and executed, performing various mathematical operations based on user input.
_______________________________________________________________________________________________________________________________________________

Exercise 3
Aim
To develop a program that demonstrates the use of List, Tuple, Set, and Dictionary data structures in Python
Program:
# 1. List: Create a list of numbers and find the sum
numbers = input("Enter values for List separated by commas (e.g., 1,2): ")
numbers_list = [int(num) for num in numbers.split(',')]
sum_of_numbers = sum(numbers_list)

# 2. Tuple: Create a tuple of student information
student_name = input("\nEnter student's name: ")
student_age = int(input("Enter student's age: "))
student_major = input("Enter student's major: ")
student_info = (student_name, student_age, student_major)

# 3. Set: Perform set operations
set1_values = input("\nEnter values for Set 1 separated by commas: ")
set1 = {int(x) for x in set1_values.split(',')}
set2_values = input("Enter values for Set 2 separated by commas: ")
set2 = {int(x) for x in set2_values.split(',')}
intersection = set1.intersection(set2)
union = set1.union(set2)

# 4. Dictionary: Create a dictionary of contact information
contact_info = {}
num_contacts = int(input("\nHow many contacts do you want to add? "))
for _ in range(num_contacts):
    name = input("Enter name: ")
    email = input("Enter email: ")
    contact_info[name] = email

# Display Results
print("\n--- Results ---")

# List Results
print("\nList\n")
print("numbers_list =", numbers_list)
print("Sum of numbers:", sum_of_numbers)

# Tuple Results
print("\nTuple\n")
print("student_info =", student_info)
print("Name:", student_info[0])
print("Age:", student_info[1])
print("Major:", student_info[2])

# Set Results
print("\nSet\n")
print("Set 1 =", set1)
print("Set 2 =", set2)
print("Intersection:", intersection)
print("Union:", union)

# Dictionary Results
print("\nDictionary\n")
print("Contact Information =",contact_info)  # Display the dictionary as is
for name, email in contact_info.items():
    print("Key =", name)   # Print key
    print("Value =", email)  # Print value

# Lookup for a specific name
name_to_lookup = input("\nEnter a name to look up their email: ")
if name_to_lookup in contact_info:
    email = contact_info[name_to_lookup]
    print(f"{name_to_lookup}'s email is {email}")
else:
    print(f"{name_to_lookup} is not in the contact list.")
Result:
The Python program to demonstrate List, Tuple, Set, and Dictionary data structures was successfully implemented and executed.
________________________________________________________________________________________________________________________________________________

Exercise 4
Aim
To build a Python program that calculates electricity bills for various consumer categories based on units consumed, using control statements.
Program:
def calculate_bill(category, units):
    # Define the energy charges based on consumer category and slabs
    if category == "Domestic":
        if units <= 400:
            rate = 4.60
        elif units <= 500:
            rate = 6.15
        elif units <= 600:
            rate = 8.15
        elif units <= 800:
            rate = 9.20
        elif units <= 1000:
            rate = 10.20
        else:
            rate = 11.25

    elif category == "Industrial":
        if units <= 400:
            rate = 5.50
        elif units <= 500:
            rate = 7.00
        elif units <= 600:
            rate = 8.50
        elif units <= 800:
            rate = 9.80
        elif units <= 1000:
            rate = 10.50
        else:
            rate = 11.75

    elif category == "Bulk Supply":
        if units <= 400:
            rate = 8.15
        elif units <= 500:
            rate = 9.00
        elif units <= 600:
            rate = 10.00
        elif units <= 800:
            rate = 11.00
        elif units <= 1000:
            rate = 12.00
        else:
            rate = 13.50

    else:
        return "Invalid consumer category."

    # Calculate the total bill
    total_bill = units * rate
    return total_bill

# Main loop for user input
while True:
    print("Select your consumer category:")
    print("1. Domestic")
    print("2. Industrial")
    print("3. Bulk Supply")

    choice = input("Enter the number corresponding to your category (1/2/3): ")

    if choice == '1':
        category = "Domestic"
    elif choice == '2':
        category = "Industrial"
    elif choice == '3':
        category = "Bulk Supply"
    else:
        print("Invalid choice. Please select again.")
        continue

    try:
        units = float(input("Enter the number of Units consumed: "))
        if units < 0:
            print("Please enter a non-negative number.")
            continue

        total_bill = calculate_bill(category, units)
        if isinstance(total_bill, str):
            print(total_bill)  # Print error message if invalid
        else:
            print(f"Your total electricity bill: Rs. {total_bill:.2f}")

    except ValueError:
        print("Invalid input. Please enter a numeric value for kWh.")

    # Option to exit the loop
    if input("Do you want to calculate another bill? (yes/no): ").lower() != 'yes':
        break
Result: 
Python program to calculate electricity bills based on consumer categories and units consumed has been successfully developed and executed.
____________________________________________________________________________________________________________________________________________________

Exercise 5
Aim
To create a simple banking system using loops, where users can create accounts, deposit money, withdraw money, and check their balance.
Program:
# Create an empty list to store accounts as dictionaries
accounts = []

# Main program loop
while True:
    print("\n--------- Welcome to the ABC Banking System ---------")
    print("1. Create a new account")
    print("2. Access an existing account")
    print("3. Exit")
    choice = input("\nEnter your choice (1/2/3): ")

    if choice == "1":
        # Create account
        account_number = len(accounts) + 1
        name = input("Enter your full name: ")
        initial_balance = float(input("Enter the initial deposit amount (Rs.): "))
        new_account = {
            "account_number": account_number,
            "name": name,
            "balance": initial_balance
        }
        accounts.append(new_account)
        print(f"\nAccount created successfully! Your Account Number is: {account_number}")
        print(f"Initial Deposit: Rs.{initial_balance:.2f}")
        
    elif choice == "2":
        # Access existing account
        if len(accounts) == 0:
            print("\nNo accounts available. Please create an account first.")
            continue

        print("\nList of Existing Accounts:")
        for account in accounts:
            print(f"Account Number: {account['account_number']}, Name: {account['name']}")

        account_number = int(input("\nEnter your Account Number to access: "))
        
        # Find the account by number
        current_account = None
        for account in accounts:
            if account['account_number'] == account_number:
                current_account = account
                break

        if current_account is None:
            print("\nInvalid Account Number. Please try again.")
            continue

        print(f"\nWelcome, {current_account['name']}!")

        while True:
            print("\nAccount Options:")
            print("A. Check Balance")
            print("B. Deposit Money")
            print("C. Withdraw Money")
            print("D. Back to Main Menu")
            account_choice = input("\nChoose an option (A/B/C/D): ")

            if account_choice == "A":
                print(f"\nYour current balance is: Rs.{current_account['balance']:.2f}")
            elif account_choice == "B":
                amount = float(input("\nEnter the amount to deposit (Rs.): "))
                if amount > 0:
                    current_account['balance'] += amount
                    print(f"\nDeposited Rs.{amount:.2f}. New balance: Rs.{current_account['balance']:.2f}")
                else:
                    print("\nInvalid deposit amount. Please enter a positive value.")
            elif account_choice == "C":
                print(f"\nYour current balance is: Rs.{current_account['balance']:.2f}")
                
                # Calculate maximum withdrawal amount (balance - Rs. 500)
                max_withdrawable = current_account['balance'] - 500
                print(f"Maximum amount you can withdraw: Rs.{max_withdrawable:.2f}")

                # Ask for the withdrawal amount
                amount = float(input("\nEnter the amount to withdraw (Rs.): "))

                if 0 < amount <= max_withdrawable:
                    current_account['balance'] -= amount
                    print(f"\nWithdrew Rs.{amount:.2f}. New balance: Rs.{current_account['balance']:.2f}")
                else:
                    print("\nInvalid amount. You must maintain a minimum balance of Rs. 500.")
            elif account_choice == "D":
                break
            else:
                print("\nInvalid option. Please try again.")

    elif choice == "3":
        print("\nThank you for using our services!")
        break
    else:
        print("\nInvalid choice. Please select a valid option (1/2/3).")

print("Your session has ended. Have a great day ahead!")
Result:
The program successfully implements a simple banking system that allows users to manage their accounts efficiently





