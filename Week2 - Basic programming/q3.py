# Pooja would like to withdraw X $US from an ATM. The cash machine will only accept
# the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 $US. Calculate Pooja's account balance after an attempted transaction.
# Input:
# Aug 2, 2023
# 1. Positiveinteger0<x<=2000-theamountofcashwhichPoojawishesto withdraw.
# 2. Non-negativenumber0<=y<=2000-Pooja'sinitialaccountbalance.
# Output: Output the account balance after the attempted transaction, given as a number. If there is not enough money in the account to complete the transaction, output the current bank balance.



def calculate_account_balance(x, y):
    # Check if x is a multiple of 5 and if there's enough money in the account
    if x % 5 == 0 and x + 0.50 <= y:
        # Calculate the new account balance after the transaction
        remaining_balance = y - x - 0.50
        return remaining_balance
    else:
        # If the conditions are not met, return the current bank balance
        return y

# Example usage:
x = int(input("Enter the amount to withdraw: "))
y = float(input("Enter Pooja's initial account balance: "))

result = calculate_account_balance(x, y)
print("Account balance after the attempted transaction: $", result)
