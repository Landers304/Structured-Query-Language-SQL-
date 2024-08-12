#Task 1:


import sqlite3

# Step 1: Connect to the database
conn = sqlite3.connect('fitness_center.db')
cursor = conn.cursor()

# Step 2: Create the Members table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS Members (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT
);
''')

# Step 3: Create the WorkoutSessions table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS WorkoutSessions (
    session_id INT PRIMARY KEY,
    member_id INT,
    session_date DATE,
    session_time VARCHAR(50),
    activity VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES Members(id)
);
''')

# Step 4: Define the members to be inserted
members = [
    (1, 'John Doe', 25),
    (2, 'Emma Smith', 29),
    (3, 'David Johnson', 35),
    (4, 'Olivia Brown', 21),
    (5, 'Lucas Davis', 32)
]

# Step 5: Insert records into the Members table with a check for uniqueness
for member in members:
    try:
        cursor.execute('INSERT INTO Members (id, name, age) VALUES (?, ?, ?)', member)
    except sqlite3.IntegrityError:
        print(f"Member with id {member[0]} already exists. Skipping insert.")

# Step 6: Define the workout sessions to be inserted
workouts = [
    (201, 1, '2023-08-01', '07:00 AM', 'Swimming'),
    (202, 2, '2023-08-01', '08:30 AM', 'Cycling'),
    (203, 3, '2023-08-02', '06:00 PM', 'Zumba'),
    (204, 4, '2023-08-03', '07:00 AM', 'Aerobics'),
    (205, 5, '2023-08-03', '05:00 PM', 'Tennis'),
    (206, 1, '2023-08-04', '09:00 AM', 'CrossFit'),
    (207, 2, '2023-08-04', '08:00 AM', 'Powerlifting'),
    (208, 3, '2023-08-05', '06:30 PM', 'Pilates'),
    (209, 4, '2023-08-06', '08:00 AM', 'Basketball'),
    (210, 5, '2023-08-07', '10:00 AM', 'Badminton')
]

# Step 7: Insert records into the WorkoutSessions table with a check for uniqueness
for workout in workouts:
    try:
        cursor.execute('INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity) VALUES (?, ?, ?, ?, ?)', workout)
    except sqlite3.IntegrityError:
        print(f"Workout session with session_id {workout[0]} already exists. Skipping insert.")

# Step 8: Commit the changes to the database
conn.commit()

# Step 9: Close the connection
conn.close()




#Task 2: 


import sqlite3

# Step 1: Connect to the database
conn = sqlite3.connect('fitness_center.db')
cursor = conn.cursor()

# Step 2: Find Jane Doe's member ID
cursor.execute("SELECT id FROM Members WHERE name = 'Jane Doe'")
jane_doe_id = cursor.fetchone()

if jane_doe_id:
    jane_doe_id = jane_doe_id[0]

    # Step 3: Update Jane Doe's workout session from morning to evening
    cursor.execute('''
    UPDATE WorkoutSessions
    SET session_time = '06:00 PM'
    WHERE member_id = ? AND session_time = '09:00 AM'
    ''', (jane_doe_id,))

    # Commit the changes
    conn.commit()

    # Step 4: Check if the update was successful
    cursor.execute("SELECT * FROM WorkoutSessions WHERE member_id = ?", (jane_doe_id,))
    updated_sessions = cursor.fetchall()

    for session in updated_sessions:
        print(session)
else:
    print("Jane Doe wasn't found in Members table.")

# Step 5: Close the connection
conn.close()




#Task 3:


import sqlite3

# Step 1: Connect to the database
conn = sqlite3.connect('fitness_center.db')
cursor = conn.cursor()

# Step 2: Find John Smith's member ID
cursor.execute("SELECT id FROM Members WHERE name = 'John Smith'")
john_smith_id = cursor.fetchone()

if john_smith_id:
    john_smith_id = john_smith_id[0]

    # Step 3: Delete John Smith's records from the WorkoutSessions table
    cursor.execute("DELETE FROM WorkoutSessions WHERE member_id = ?", (john_smith_id,))

    # Step 4: Delete John Smith's record from the Members table
    cursor.execute("DELETE FROM Members WHERE id = ?", (john_smith_id,))

    # Commit the changes
    conn.commit()

    print("John Smith's not found in Member's table.")
else:
    print("John Smith records have been successfully removed from the database .")

# Step 5: Close the connection
conn.close()


