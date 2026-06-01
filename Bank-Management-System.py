# Banking Management System

accounts = {}

while True:

    print("\n===== SHIVAM BANK OF INDIA =====")
    print("1. Create Account")
    print("2. Log In")
    print("3. Exit")

    choice = input("Enter Your Choice: ")

    # CREATE ACCOUNT

    if choice == "1":

        name = input("Enter Full Name: ")
        age = int(input("Enter Age: "))
        mobile = input("Enter Mobile Number: ")
        aadhaar = input("Enter Aadhaar Number: ")
        address = input("Enter Address: ")
        username = input("Create Username: ")
        password = input("Create Password: ")

        if username in accounts:
            print("Username Already Exists!")
            continue

        accounts[username] = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "aadhaar": aadhaar,
            "address": address,
            "password": password,
            "balance": 0
        }

        print("Account Successfully Created!")

    # LOGIN

    elif choice == "2":

        login_username = input("Enter Username: ")
        login_password = input("Enter Password: ")

        if login_username in accounts:

            if login_password == accounts[login_username]["password"]:

                print("Login Successful!")

                # BANKING MENU

                while True:

                    print("\n===== BANKING MENU =====")
                    print("1. Deposit Money")
                    print("2. Check Balance")
                    print("3. Withdraw Money")
                    print("4. View Profile")
                    print("5. Logout")

                    bank_choice = input("Enter Choice: ")

                    # DEPOSIT

                    if bank_choice == "1":

                        amount = int(input("Enter Deposit Amount: "))

                        accounts[login_username]["balance"] += amount

                        print("Amount Deposited Successfully!")
                        print(
                            "Current Balance:",
                            accounts[login_username]["balance"]
                        )

                    # CHECK BALANCE

                    elif bank_choice == "2":

                        print(
                            "Current Balance:",
                            accounts[login_username]["balance"]
                        )

                    # WITHDRAW

                    elif bank_choice == "3":

                        amount = int(input("Enter Withdraw Amount: "))

                        if amount <= accounts[login_username]["balance"]:

                            accounts[login_username]["balance"] -= amount

                            print("Amount Withdrawn Successfully!")
                            print(
                                "Current Balance:",
                                accounts[login_username]["balance"]
                            )

                        else:
                            print("Insufficient Balance!")

                    # VIEW PROFILE

                    elif bank_choice == "4":

                        print("\n===== PROFILE =====")
                        print("Username:", login_username)
                        print("Name:", accounts[login_username]["name"])
                        print("Age:", accounts[login_username]["age"])
                        print("Mobile:", accounts[login_username]["mobile"])
                        print("Aadhaar:", accounts[login_username]["aadhaar"])
                        print("Address:", accounts[login_username]["address"])
                        print("Balance:", accounts[login_username]["balance"])

                    # LOGOUT

                    elif bank_choice == "5":

                        print("Logout Successful!")
                        break

                    else:
                        print("Invalid Choice!")

            else:
                print("Incorrect Password!")

        else:
            print("Username Not Found!")

    # EXIT
    
    elif choice == "3":

        print("Thank You For Using SHIVAM BANK OF INDIA!")
        break

    else:
        print("Invalid Choice!")