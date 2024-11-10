class UserInterface:
    def show_login_signup_options(self):
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")
        return input("Select an option: ")

    def show_main_menu(self):
        print("\nMain Menu")
        print("1. Search Tweets")
        print("2. Search Users")
        print("3. Compose a Tweet")
        print("4. List Followers")
        print("5. Logout")
        return input("Select an option: ")