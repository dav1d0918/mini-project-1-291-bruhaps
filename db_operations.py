import sqlite3
from datetime import datetime

class DatabaseOperations:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.conn.row_factory = sqlite3.Row

    def login(self):
        email = input("Enter email: ")
        pwd = input("Enter password: ")
        query = "SELECT * FROM users WHERE email = ? AND pwd = ?"
        cur = self.conn.cursor()
        cur.execute(query, (email, pwd))
        return cur.fetchone()  # Will return None if credentials are incorrect


    def signup(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        pwd = input("Create a password: ")
        
        query = "INSERT INTO users (name, email, phone, pwd) VALUES (?, ?, ?, ?)"
        try:
            cur = self.conn.cursor()
            cur.execute(query, (name, email, phone, pwd))
            self.conn.commit()
            print("Sign-up successful!")
        except sqlite3.IntegrityError:
            print("Email already exists.")

    def search_tweets(self):
        term = input("Enter keyword to search tweets: ")
        query = """
        SELECT * FROM tweets 
        WHERE text LIKE ?
        """
        cur = self.conn.cursor()
        cur.execute(query, ('%' + term + '%',))
        results = cur.fetchall()
        if results:
            for row in results:
                print(f"Tweet ID: {row['tid']} | Writer ID: {row['writer_id']} | Text: {row['text']}")
        else:
            print("No tweets found.")

    def search_users(self):
        name = input("Enter name to search users: ")
        query = "SELECT * FROM users WHERE name LIKE ?"
        cur = self.conn.cursor()
        cur.execute(query, ('%' + name + '%',))
        results = cur.fetchall()
        if results:
            for row in results:
                print(f"User ID: {row['usr']} | Name: {row['name']} | Email: {row['email']}")
        else:
            print("No users found.")

    def compose_tweet(self, user_id):
        text = input("Enter your tweet: ")
        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M:%S")
        
        query = "INSERT INTO tweets (writer_id, text, tdate, ttime) VALUES (?, ?, ?, ?)"
        cur = self.conn.cursor()
        cur.execute(query, (user_id, text, date, time))
        self.conn.commit()
        print("Tweet posted successfully.")

    def list_followers(self, user_id):
        query = """
        SELECT u.usr, u.name, u.email 
        FROM users u 
        JOIN follows f ON u.usr = f.flwer 
        WHERE f.flwee = ?
        """
        cur = self.conn.cursor()
        cur.execute(query, (user_id,))
        results = cur.fetchall()
        if results:
            print("Followers:")
            for row in results:
                print(f"User ID: {row['usr']} | Name: {row['name']} | Email: {row['email']}")
        else:
            print("No followers found.")

    def __del__(self):
        self.conn.close()