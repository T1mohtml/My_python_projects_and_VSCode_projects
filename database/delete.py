import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('simple_database.db')
cursor = conn.cursor()

# Command to delete all records from the 'users' table
cursor.execute("DELETE FROM users")
conn.commit()
print("All data has been cleared from the 'users' table.")

# Verify the table is empty
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
if not rows:
    print("The table is now empty.")
else:
    print("Data still exists:", rows)

# Close the connection
conn.close()