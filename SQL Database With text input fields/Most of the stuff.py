import sqlite3
from tkinter import *
from tkinter import messagebox


# Step 1: Database setup
def setup_database():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    # Add a test user (Optional)
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ('test', '1234'))
    conn.commit()
    conn.close()


# Step 2: Logic to handle login
def login():
    username = username_entry.get()  # Get the entered username
    password = password_entry.get()  # Get the entered password

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Check if the username and password match in the database
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()  # Fetch the first matching record

    conn.close()  # Close the database connection

    if user:  # If a user is found
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")  # Success message
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")  # Error message


# Step 3: GUI setup
def create_login_window():
    global username_entry, password_entry

    window = Tk()
    window.title("Login System")
    window.geometry("300x200")

    # Username Label and Entry
    Label(window, text="Username:").pack(pady=5)
    username_entry = Entry(window)
    username_entry.pack(pady=5)

    # Password Label and Entry
    Label(window, text="Password:").pack(pady=5)
    password_entry = Entry(window, show="*")
    password_entry.pack(pady=5)

    # Login Button
    Button(window, text="Login", command=login).pack(pady=10)

    window.mainloop()


# Main execution
if __name__ == "__main__":
    setup_database()  # Initialize the database with a sample user
    create_login_window()