import sqlite3

from sqlite3 import Error


def sql_connection():
    try:

        sqlite_connection = sqlite3.connect('mydatabase.db')

        return sqlite_connection

    except Error:

        print(Error)


def sql_table(sqlite_connection):
    cursor1_1 = sqlite_connection.cursor()
    cursor2_1 = sqlite_connection.cursor()
    cursor3_1 = sqlite_connection.cursor()

    cursor1_1.execute('''create table if not exists Students(
                                                id integer PRIMARY KEY,
                                                name text, 
                                                surname text, 
                                                age integer, 
                                                city text
                                                )''')
    cursor2_1.execute('''create table if not exists Courses(
                                                id integer PRIMARY KEY,
                                                name text, 
                                                time_start text, 
                                                time_end text 
                                                )''')
    cursor3_1.execute('''create table if not exists Student_courses(
                                                id integer PRIMARY KEY,
                                                student_id integer, 
                                                course_id integer, 
                                                FOREIGN KEY (student_id) REFERENCES Students(id)
                                                FOREIGN KEY (course_id) REFERENCES Courses(id)
                                                )''')

    sqlite_connection.commit()


def Students(sqlite_connection, entities):
    cursorObj = sqlite_connection.cursor()

    cursorObj.execute('INSERT INTO Students(id, name, surname, age, city) VALUES(?, ?, ?, ?, ?)', entities)

    sqlite_connection.commit()


def Courses(sqlite_connection, entities):
    cursorObj = sqlite_connection.cursor()

    cursorObj.execute('INSERT INTO Courses(id, name, time_start, time_end) VALUES(?, ?, ?, ?)', entities)

    sqlite_connection.commit()


def Student_courses(sqlite_connection, entities):
    cursorObj = sqlite_connection.cursor()

    cursorObj.execute('INSERT INTO Student_courses(id, student_id, course_id) VALUES(?, ?, ?)', entities)

    sqlite_connection.commit()


def Elder_30(sqlite_connection):
    cursorObj = sqlite_connection.cursor()

    cursorObj.execute('SELECT id, name FROM Students WHERE age > 30.0')

    rows = cursorObj.fetchall()

    for row in rows:
        print(row)


def List_of_py_students(sqlite_connection):
    cursorId = sqlite_connection.cursor()
    cursorName = sqlite_connection.cursor()

    cursorId.execute('SELECT student_id FROM Student_courses WHERE course_id = 1')

    id_from_courses = cursorId.fetchall()
    cursorName.execute('SELECT name FROM Students WHERE id in (2, 3)')

    rows = cursorName.fetchall()

    for row in rows:
        print(row)


sqlite_connection = sql_connection()
sql_table(sqlite_connection)
'''
Students(sqlite_connection, (1, 'Max', 'Brooks', 24, 'Spb'))
Students(sqlite_connection, (2, 'John', 'Stones', 15, 'Spb'))
Students(sqlite_connection, (3, 'Andy', 'Wings', 45, 'Manhester'))
Students(sqlite_connection, (4, 'Kate', 'Brooks', 34, 'Spb'))

Courses(sqlite_connection, (1, 'python', '21.07.21', '21.08.21'))
Courses(sqlite_connection, (2, 'java', '13.07.21', '16.08.21'))

Student_courses(sqlite_connection, (1, 1, 1))
Student_courses(sqlite_connection, (2, 2, 1))
Student_courses(sqlite_connection, (3, 3, 1))
Student_courses(sqlite_connection, (4, 4, 2))
'''
cursor0 = sqlite_connection.cursor()
print("Data from Students")
for i in cursor0.execute("SELECT * FROM Students"):
    print(i)
print("Data from Courses")
for i in cursor0.execute("SELECT * FROM Courses"):
    print(i)
print("Data from Student_courses")
for i in cursor0.execute("SELECT * FROM Student_courses"):
    print(i)
List_of_py_students(sqlite_connection)
sqlite_connection.close()