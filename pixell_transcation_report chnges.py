"""This module contains a program that reads through transaction records
and reports the results.

Example:
    $ python pixell_transaction_report.py
"""

_author_ = "Anannya"
_version_ = "1.0.0"
_credits_ = "COMP-1327 Faculty"

import csv
import os

valid_transaction_types = ['deposit', 'withdraw']
customer_data = {}
rejected_transactions = []
transaction_counter = 0
total_transaction_amount = 0

# Clears the terminal
os.system('cls' if os.name == 'nt' else 'clear')

import os

# File paths
SCRIPT_DIRECTORY = os.path.dirname(__file__)
DATA_FILENAME = "bank_data.csv"
DATA_FILE_PATH = os.path.join(SCRIPT_DIRECTORY, DATA_FILENAME)

try:
    with open(DATA_FILE_PATH, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header

        for transaction in reader:
            is_valid_record = True
            validation_errors = []

            customer_id = transaction[0]
            transaction_type = transaction[1]

            ### VALIDATION 1 ###
            if transaction_type not in valid_transaction_types:
                is_valid_record = False
                validation_errors.append(f'The transaction type "{transaction_type}" is invalid.')

            ### VALIDATION 2 ###
            try:
                transaction_amount = float(transaction[2])
            except ValueError:
                is_valid_record = False
                validation_errors.append(f'"{transaction[2]}" is an invalid transaction amount.')

            ### VALID ###
            if is_valid_record:
                if customer_id not in customer_data:
                    customer_data[customer_id] = {'balance': 0.0, 'transactions': []}

                if transaction_type == 'deposit':
                    customer_data[customer_id]['balance'] += transaction_amount
                elif transaction_type == 'withdraw':
                    customer_data[customer_id]['balance'] -= transaction_amount

                customer_data[customer_id]['transactions'].append(
                    (transaction_amount, transaction_type)
                )

                transaction_counter += 1
                total_transaction_amount += transaction_amount

            ### COLLECT INVALID RECORDS ###
            else:
                rejected_transactions.append((transaction, validation_errors))

except FileNotFoundError:
    print(f"The bank data file ({DATA_FILENAME}) cannot be found.")
    exit()

# === Reporting Section ===
report_title = "PiXELL River Transaction Report"
print(report_title)
print("=" * len(report_title))

# Customer summaries
for customer_id, data in customer_data.items():
    balance = data['balance']
    print(f"\nCustomer {customer_id} has a balance of ${balance:,.2f}.")
    print("Transaction History:")
    for amount, trans_type in data['transactions']:
        print(f"{trans_type.capitalize():>16}: {amount:>12,.2f}")

# Average transaction amount
if transaction_counter > 0:
    average = total_transaction_amount / transaction_counter
    print(f"\nAVERAGE TRANSACTION AMOUNT: ${average:,.2f}")
else:
    print("\nAVERAGE TRANSACTION AMOUNT: $0.00")

# Rejected transactions
rejected_report_title = "REJECTED RECORDS"
print("\n" + rejected_report_title)
print("=" * len(rejected_report_title))

for rejected in rejected_transactions:
    print("REJECTED:", rejected)