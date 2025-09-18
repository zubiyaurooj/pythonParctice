print("Login System")

# stored username and password
username = "zubiya"
password = "290103"

# user input
u = input("Enter username: ")
p = input("Enter password: ")

if u == username and p == password:
    print("Login successful! Welcome", u)
elif u == username and p != password:
    print("Wrong password.")
else:
    print("User not found.")
