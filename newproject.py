import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll_no TEXT,
    math_marks INTEGER,
    physics_marks INTEGER,
    chemistry_marks INTEGER,
    total INTEGER,
    grade TEXT
)
''')
conn.commit()

# Function to calculate grade
def calculate_grade(total):
    if total >= 270:
        return 'A'
    elif total >= 240:
        return 'B'
    elif total >= 210:
        return 'C'
    elif total >= 180:
        return 'D'
    else:
        return 'F'

# Function to add student
def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll Number: ")
    math = int(input("Math Marks: "))
    physics = int(input("Physics Marks: "))
    chemistry = int(input("Chemistry Marks: "))
    
    total = math + physics + chemistry
    grade = calculate_grade(total)
    
    cursor.execute('''
    INSERT INTO students (name, roll_no, math_marks, physics_marks, chemistry_marks, total, grade)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, roll, math, physics, chemistry, total, grade))
    conn.commit()
    print("Student added successfully!\n")

# Function to view all students
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if rows:
        print(f"{'ID':<5}{'Name':<20}{'Roll':<10}{'Math':<6}{'Physics':<8}{'Chemistry':<10}{'Total':<6}{'Grade':<6}")
        print("-"*75)
        for row in rows:
            print(f"{row[0]:<5}{row[1]:<20}{row[2]:<10}{row[3]:<6}{row[4]:<8}{row[5]:<10}{row[6]:<6}{row[7]:<6}")
    else:
        print("No records found.\n")

# Function to search student by Roll Number
def search_student():
    roll = input("Enter Roll Number to search: ")
    cursor.execute("SELECT * FROM students WHERE roll_no=?", (roll,))
    row = cursor.fetchone()
    if row:
        print(f"{'ID':<5}{'Name':<20}{'Roll':<10}{'Math':<6}{'Physics':<8}{'Chemistry':<10}{'Total':<6}{'Grade':<6}")
        print("-"*75)
        print(f"{row[0]:<5}{row[1]:<20}{row[2]:<10}{row[3]:<6}{row[4]:<8}{row[5]:<10}{row[6]:<6}{row[7]:<6}")
    else:
        print("Student not found.\n")

# Function to update student marks
def update_student():
    roll = input("Enter Roll Number to update: ")
    cursor.execute("SELECT * FROM students WHERE roll_no=?", (roll,))
    row = cursor.fetchone()
    if row:
        math = int(input("Enter new Math marks: "))
        physics = int(input("Enter new Physics marks: "))
        chemistry = int(input("Enter new Chemistry marks: "))
        total = math + physics + chemistry
        grade = calculate_grade(total)
        
        cursor.execute('''
        UPDATE students
        SET math_marks=?, physics_marks=?, chemistry_marks=?, total=?, grade=?
        WHERE roll_no=?
        ''', (math, physics, chemistry, total, grade, roll))
        conn.commit()
        print("Student updated successfully!\n")
    else:
        print("Student not found.\n")

# Function to delete a student
def delete_student():
    roll = input("Enter Roll Number to delete: ")
    cursor.execute("SELECT * FROM students WHERE roll_no=?", (roll,))
    row = cursor.fetchone()
    if row:
        cursor.execute("DELETE FROM students WHERE roll_no=?", (roll,))
        conn.commit()
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")

# Main menu
def menu():
    while True:
        print("\n===== Student Result Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    menu()
    conn.close()
