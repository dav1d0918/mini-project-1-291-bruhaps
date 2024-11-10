from db_operations import DatabaseOperations
from ui import UserInterface

def main():
    db_file = 'mini_project1.db'
    db_ops = DatabaseOperations(db_file)
    ui = UserInterface()

    while True:
        user_action = ui.show_login_signup_options()
        
        if user_action == '1':  # Login
            user = db_ops.login()
            if user:
                print(f"Welcome, {user['name']}!")  # Greet the user by name
                while True:
                    choice = ui.show_main_menu()
                    if choice == '1':
                        db_ops.search_tweets()
                    elif choice == '2':
                        db_ops.search_users()
                    elif choice == '3':
                        db_ops.compose_tweet(user['usr'])  # Pass user ID to compose tweet
                    elif choice == '4':
                        db_ops.list_followers(user['usr'])  # Pass user ID to list followers
                    elif choice == '5':
                        print("Logging out.")
                        break
                    else:
                        print("Invalid option.")
            else:
                print("Invalid email or password.")
                
        elif user_action == '2':  # Sign-up
            db_ops.signup()
        elif user_action == '3':  # Exit
            print("Exiting application.")
            break

if __name__ == "__main__":
    main()