print("Login System")

# stored username and password
username = "zubiya"
password = "290103"

# user input
u = input("Enter username: ")
p = input("Enter password: ") 

lenofp=len(p)
lenpassword=len(password)

if lenofp == lenpassword:
    if u == username and p == password:
        print("Login successful! Welcome", u)
    elif u == username and p != password:
        print("Wrong password.")
    else:
        print("User not found.")

else:
    print('user password should be 6 digit')
     
    

