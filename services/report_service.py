from services.database import get_connection
from utils.logger import logging


def student_report():

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            SELECT
                s.StudentID,
                s.StudentName,
                d.DepartmentName,
                c.ClassName,
                s.Email,
                s.Phone,
                s.AdmissionDate
            FROM students s
            JOIN departments d
                ON s.DepartmentID = d.DepartmentID
            JOIN classes c
                ON s.ClassID = c.ClassID
            ORDER BY s.StudentID
            """

            cursor.execute(query)

            students = cursor.fetchall()

            print("\n" + "=" * 100)
            print("                 STUDENT REPORT")
            print("=" * 100)

            if students:

                for student in students:

                    print(f"""
Student ID      : {student[0]}
Name            : {student[1]}
Department      : {student[2]}
Class           : {student[3]}
Email           : {student[4]}
Phone           : {student[5]}
Admission Date  : {student[6]}
------------------------------------------------------------
""")

            else:

                print("No student records found.")

            logging.info("Student report generated.")

        except Exception as e:

            print(f"\n❌ Error: {e}")
            logging.error(f"Error generating student report: {e}")

        finally:

            cursor.close()
            connection.close()


def teacher_report():

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            SELECT
                t.TeacherID,
                t.TeacherName,
                t.Email,
                t.Phone,
                d.DepartmentName
            FROM teachers t
            JOIN departments d
                ON t.DepartmentID = d.DepartmentID
            ORDER BY t.TeacherID
            """

            cursor.execute(query)

            teachers = cursor.fetchall()

            print("\n" + "=" * 90)
            print("                 TEACHER REPORT")
            print("=" * 90)

            if teachers:

                for teacher in teachers:

                    print(f"""
Teacher ID   : {teacher[0]}
Name         : {teacher[1]}
Email        : {teacher[2]}
Phone        : {teacher[3]}
Department   : {teacher[4]}
------------------------------------------------------------
""")

            else:

                print("No teacher records found.")

            logging.info("Teacher report generated.")

        except Exception as e:

            print(f"\n❌ Error: {e}")
            logging.error(f"Error generating teacher report: {e}")

        finally:

            cursor.close()
            connection.close()


def attendance_report():

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            SELECT
                s.StudentID,
                s.StudentName,
                COUNT(a.AttendanceID) AS TotalDays,
                SUM(
                    CASE
                        WHEN a.Status = 'Present' THEN 1
                        ELSE 0
                    END
                ) AS PresentDays,
                SUM(
                    CASE
                        WHEN a.Status = 'Absent' THEN 1
                        ELSE 0
                    END
                ) AS AbsentDays
            FROM students s
            LEFT JOIN attendance a
                ON s.StudentID = a.StudentID
            GROUP BY
                s.StudentID,
                s.StudentName
            ORDER BY s.StudentID
            """

            cursor.execute(query)

            records = cursor.fetchall()

            print("\n" + "=" * 90)
            print("               ATTENDANCE REPORT")
            print("=" * 90)

            if records:

                for record in records:

                    total_days = record[2] or 0
                    present_days = record[3] or 0
                    absent_days = record[4] or 0

                    if total_days > 0:
                        percentage = (
                            present_days / total_days
                        ) * 100
                    else:
                        percentage = 0

                    print(f"""
Student ID     : {record[0]}
Student Name   : {record[1]}
Total Days     : {total_days}
Present Days   : {present_days}
Absent Days    : {absent_days}
Attendance %   : {percentage:.2f}%
------------------------------------------------------------
""")

            else:

                print("No attendance records found.")

            logging.info("Attendance report generated.")

        except Exception as e:

            print(f"\n❌ Error: {e}")
            logging.error(
                f"Error generating attendance report: {e}"
            )

        finally:

            cursor.close()
            connection.close()


def marks_report():

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            SELECT
                s.StudentID,
                s.StudentName,
                COUNT(m.MarkID) AS Subjects,
                SUM(m.Marks) AS TotalMarks,
                AVG(m.Marks) AS AverageMarks
            FROM students s
            LEFT JOIN marks m
                ON s.StudentID = m.StudentID
            GROUP BY
                s.StudentID,
                s.StudentName
            ORDER BY s.StudentID
            """

            cursor.execute(query)

            records = cursor.fetchall()

            print("\n" + "=" * 90)
            print("                  MARKS REPORT")
            print("=" * 90)

            if records:

                for record in records:

                    subjects = record[2] or 0
                    total_marks = record[3] or 0
                    average = record[4] or 0

                    if average >= 90:
                        grade = "A+"
                    elif average >= 80:
                        grade = "A"
                    elif average >= 70:
                        grade = "B"
                    elif average >= 60:
                        grade = "C"
                    elif average >= 50:
                        grade = "D"
                    else:
                        grade = "F"

                    print(f"""
Student ID     : {record[0]}
Student Name   : {record[1]}
Subjects       : {subjects}
Total Marks    : {total_marks}
Average Marks  : {average:.2f}
Grade          : {grade}
------------------------------------------------------------
""")

            else:

                print("No marks records found.")

            logging.info("Marks report generated.")

        except Exception as e:

            print(f"\n❌ Error: {e}")
            logging.error(
                f"Error generating marks report: {e}"
            )

        finally:

            cursor.close()
            connection.close()


def report_menu():

    while True:

        print("\n" + "=" * 45)
        print("          REPORTS")
        print("=" * 45)
        print("1. Student Report")
        print("2. Teacher Report")
        print("3. Attendance Report")
        print("4. Marks Report")
        print("5. Back")
        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":

            student_report()

        elif choice == "2":

            teacher_report()

        elif choice == "3":

            attendance_report()

        elif choice == "4":

            marks_report()

        elif choice == "5":

            break

        else:

            print("\n❌ Invalid Choice.")