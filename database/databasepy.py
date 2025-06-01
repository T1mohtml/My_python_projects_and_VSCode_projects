import sqlite3



conn = sqlite3.connect('simple_database.db')


cursor = conn.cursor()



cursor.execute('''CREATE TABLE IF NOT EXISTS users ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER NOT NULL ) ''')



print("Database and table created successfully!")




def insert_data():
    name = input("Enter your name:  ")
    age = int(input("Enter your age:  "))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print("Data inserted successfully!")


def view_data():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print("\nUser Data1:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
    print()




while True:
    print("\n1. Add user")
    print("2. View users")
    print("3. Exit")
    choice = input("Enter your choice:  ")


    if choice == "1":
        insert_data()
    elif choice == "2":
        view_data()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")



conn.close()