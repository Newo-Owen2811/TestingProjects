import os

print("___Welcome___")

FILE_PATH = r"D:\VS CODE PROJECT\Login\data.csv"


def sign_up():
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

    while True:
        email = input("Enter your email: ").strip().lower()
        if not email:
            print("You cannot leave email blank!")
        elif "@gmail.com" not in email:
            print("Please use a valid Gmail address!")
        else:
            break

    while True:
        password = input("Enter your password: ")
        if "," in password:
            print("No commas allowed!")
        elif " " in password:
            print("No space allowed!")
        elif len(password) < 8:
            print("Password is too short!")
        else:
            break

    key = f"{email},{password}"
    with open(FILE_PATH, "a") as file:
        file.write(f"{key}\n")
    print("Sign up successful!")


def sign_in():
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

    # Check if file exists to prevent FileNotFoundError
    if not os.path.exists(FILE_PATH):
        print("No accounts found. Please sign up first!")
        return None

    while True:
        email = input("Enter your email: ").strip().lower()
        password = input("Enter your password: ")
        key = f"{email},{password}"
        login_success = False
        cleaned_line = ""

        with open(FILE_PATH, "r") as file:
            for line in file:
                cleaned_line = line.strip()
                if key == cleaned_line:
                    print("Login successful!")
                    login_success = True
                    break

        if login_success:
            return cleaned_line
        else:
            print("Wrong Password or username, please try again!")
            retry = input("Do you want to try again? (y/n): ").lower()
            if retry != "y":
                return None


def edit_csv(current_email, current_password):
    while True:
        password = input("Enter your current password to confirm: ")
        if password != current_password:
            print("Wrong password!")
        else:
            break

    while True:
        newpassword = input("Enter your new password: ")
        if "," in newpassword:
            print("No commas allowed!")
        elif " " in newpassword:
            print("No space allowed!")
        elif len(newpassword) < 8:
            print("Password is too short!")
        else:
            break

    updatedpass = []

    with open(FILE_PATH, "r") as file:
        for line in file:
            cleaned = line.strip()
            if cleaned:
                email, stored_password = cleaned.split(",")
                if email == current_email:
                    updatedpass.append(f"{email},{newpassword}\n")
                else:
                    updatedpass.append(
                        line if line.endswith("\n") else line + "\n"
                    )

    # Write the updated records back to the CSV file
    with open(FILE_PATH, "w") as file:
        file.writelines(updatedpass)

    print("Password updated successfully!")


# Main Program Loop
logged_in_user = None

while True:
    if not logged_in_user:
        choice = input(
            "\n1. Sign up\n2. Sign in\n3. Exit\nChoose an option: "
        )
        if choice == "1":
            sign_up()
        elif choice == "2":
            user_data = sign_in()
            if user_data:
                logged_in_user = user_data
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Enter a valid choice!")
    else:
        email, password = logged_in_user.split(",")
        print(f"\nLogged in as: {email}")
        choice = input("1. Change Password\n2. Log out\nChoose an option: ")

        if choice == "1":
            edit_csv(email, password)
            logged_in_user = None
        elif choice == "2":
            logged_in_user = None
            print("Logged out successfully.")
        else:
            print("Enter a valid choice!")