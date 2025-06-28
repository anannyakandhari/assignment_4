"""This module contains a program that reads through transaction records
and reports the results.

Example:
    $ python pixell_transaction_report.py
"""

__author__ = "ANANNYA"
__version__ = "1.0"
__credits__ = "COMP-1327 Faculty"

import csv
import os
 
valid_transaction_types = ['deposit', 'withdraw']
customer_data = {}
rejected_transactions = []

transaction_counter = 0

total_transaction_amount = 0

# Clears the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Get the directory the script is saved to
SCRIPT_DIRECTORY = os.path.dirname(__file__)

# The name of the data file
DATA_FILENAME = "bank_data.csv"

# The absolute path to the data file
DATA_FILE_PATH = f"{SCRIPT_DIRECTORY}/{DATA_FILENAME}"

# STEP 5: Handle missing file 
with open(DATA_FILE_PATH, 'r') as csv_file:
    reader = csv.reader(csv_file)

    # Skip heading row
    next(reader)

    for transaction in reader:
        # Reset valid record and error message for each iteration
        is_valid_record = True
        
        # Stores validation error messages
        validation_errors = []

        # Gets the customer ID from the first column
        customer_id = transaction[0]
        
        # Gets the transaction type from the second column
        transaction_type = transaction[1].lower()
transaction_amount_str = transaction[2]

        ### VALIDATION 1 ###
if transaction_type not in valid_transaction_types:
                is_valid_record = False
                validation_errors.append(f'The transaction type "{transaction_type}" is invalid.')

        ### VALIDATION 2 ###
        # Gets the transaction amount from the third column
       try: 1
        transaction_amount = float(transaction[transaction_amount_str])
except ValueError:
                is_valid_record = False
                validation_errors.append(f'"{transaction_amount_str}" is an invalid transaction amount.')


        if is_valid_record:
            # Initialize the customer's account balance if it doesn't 
            # already exist
            if customer_id not in customer_data:
                customer_data[customer_id] = {'balance': 0, 'transactions': []}
            
            # Update the customer's account balance based on the 
            # transaction type
            if transaction_type == 'deposit':
                customer_data[customer_id]['balance'] += transaction_amount
            elif transaction_type == 'withdrawal':
                customer_data[customer_id]['balance'] += transaction_amount
                
            # Record transactions in the customer's transaction history
            customer_data[customer_id]['transactions'].append(
                (transaction_amount, transaction_type))
        
transaction_counter += 1
  total_transaction_amount += transaction_amount

        ### COLLECT INVALID RECORDS ###
        else:
rejected_transactions_append((transcation, validation_errors))
 
 except FileNotFoundError:
print(f"the bank data file ({DATA_FILENAME})cannot be found.")
sys.exit()

#report title
 report_title = "PiXELL River Transaction Report"
print(report_title)
print('=' * len(report_title))

# Print the final account balances and history for each customer
for customer_id, data in customer_data.items():
    balance = data['balance']

    print(f"Customer {customer_id} has a balance of {balance:,.2f}.")
    print("Transaction History:")

    for amount, transaction_type = ['transactions']:
print(f"AVERAGE TRANSACTION AMOUNT: ${average_transaction_amount}")
elseprint("AVERAGE TRANSACTION AMOUNT: $0.00")

#Rejected records
rejected_title = "REJECTED RECORDS"
print(rejected_title)
print('=' * len(rejected_title))


for report in rejected_transactions:
    print("REJECTED:", record)
