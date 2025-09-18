#ATM CASH WITHDRAWAL USING NESTED IF- ALSE
print ("=== Welcome to Zubi's Bank ATM===")

balance= 5000

amount = int(input("Enter the amount you want to withdraw: "))

if amount <= balance:
    if amount % 100 == 0:
        balance -= amount
        print(f"Transaction successful! You withdrew ₹{amount}.")
        print(f"Remaining balance: ₹{balance}")
    else:
        print("Please enter the amount in multiples of 100.")
else:
    print("Insufficient balance.")