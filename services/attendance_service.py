from services.database import get_connection
from utils.logger import logging


def mark_attendance():

    print("\n========== MARK ATTENDANCE ==========\n")

    student_id = input("Enter Student ID: ")
    attendance_date = input("Enter Date (YYYY-MM-DD): ")
    status = input("Enter Status (Present/Absent): ")

    status = status.capitalize()

    if status not in ["Present", "Absent"]:
        print("\n❌ Invalid attendance status.")
        return

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            INSERT INTO attendance
            (StudentID, AttendanceDate, Status)
            VALUES (%s, %s, %s)
            """

            cursor.execute(
                query,
                (student_id, attendance_date, status)
            )

            connection.commit()

            print("\n✅ Attendance Marked Successfully!")

            logging.info(
                f"Attendance marked for Student {student_id}"
            )

        except Exception as e:

            connection.rollback()

            print(f"\n❌ Error: {e}")
            logging.error(
                f"Error marking attendance: {e}"
            )

        finally:

            cursor.close()
            connection.close()


def view_attendance():

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            SELECT
                a.AttendanceID,
                s.StudentID,
                s.StudentName,
                d.DepartmentName,
                c.ClassName,
                a.AttendanceDate,
                a.Status
            FROM attendance a
            JOIN students s
                ON a.StudentID = s.StudentID
            JOIN departments d
                ON s.DepartmentID = d.DepartmentID
            JOIN classes c
                ON s.ClassID = c.ClassID
            ORDER BY a.AttendanceDate DESC, a.AttendanceID DESC
            """

            cursor.execute(query)

            attendance_records = cursor.fetchall()

            print("\n" + "=" * 90)
            print("ATTENDANCE RECORDS")
            print("=" * 90)

            if attendance_records:

                for record in attendance_records:

                    print(f"""
Attendance ID : {record[0]}
Student ID    : {record[1]}
Student Name  : {record[2]}
Department    : {record[3]}
Class         : {record[4]}
Date          : {record[5]}
Status        : {record[6]}
------------------------------------------------------------
""")

            else:

                print("No attendance records found.")

            logging.info("Viewed attendance records.")

        except Exception as e:

            print(f"\n❌ Error: {e}")
            logging.error(
                f"Error viewing attendance: {e}"
            )

        finally:

            cursor.close()
            connection.close()


def search_attendance():

    student_id = input("\nEnter Student ID: ")

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            SELECT
                a.AttendanceID,
                s.StudentID,
                s.StudentName,
                d.DepartmentName,
                c.ClassName,
                a.AttendanceDate,
                a.Status
            FROM attendance a
            JOIN students s
                ON a.StudentID = s.StudentID
            JOIN departments d
                ON s.DepartmentID = d.DepartmentID
            JOIN classes c
                ON s.ClassID = c.ClassID
            WHERE s.StudentID = %s
            ORDER BY a.AttendanceDate DESC
            """

            cursor.execute(query, (student_id,))

            records = cursor.fetchall()

            print("\n" + "=" * 90)
            print("STUDENT ATTENDANCE")
            print("=" * 90)

            if records:

                for record in records:

                    print(f"""
Attendance ID : {record[0]}
Student ID    : {record[1]}
Student Name  : {record[2]}
Department    : {record[3]}
Class         : {record[4]}
Date          : {record[5]}
Status        : {record[6]}
------------------------------------------------------------
""")

            else:

                print("\n❌ No attendance records found.")

            logging.info(
                f"Attendance searched for Student {student_id}"
            )

        except Exception as e:

            print(f"\n❌ Error: {e}")
            logging.error(
                f"Error searching attendance: {e}"
            )

        finally:

            cursor.close()
            connection.close()


def attendance_report():

    student_id = input("\nEnter Student ID: ")

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            SELECT
                COUNT(*) AS TotalDays,
                SUM(CASE WHEN Status = 'Present' THEN 1 ELSE 0 END) AS PresentDays,
                SUM(CASE WHEN Status = 'Absent' THEN 1 ELSE 0 END) AS AbsentDays
            FROM attendance
            WHERE StudentID = %s
            """

            cursor.execute(query, (student_id,))

            report = cursor.fetchone()

            total_days = report[0] or 0
            present_days = report[1] or 0
            absent_days = report[2] or 0

            if total_days > 0:

                percentage = (present_days / total_days) * 100

            else:

                percentage = 0

            print("\n" + "=" * 50)
            print("       ATTENDANCE REPORT")
            print("=" * 50)
            print(f"Total Days     : {total_days}")
            print(f"Present Days   : {present_days}")
            print(f"Absent Days    : {absent_days}")
            print(f"Attendance %   : {percentage:.2f}%")
            print("=" * 50)

            logging.info(
                f"Attendance report generated for Student {student_id}"
            )

        except Exception as e:

            print(f"\n❌ Error: {e}")
            logging.error(
                f"Error generating attendance report: {e}"
            )

        finally:

            cursor.close()
            connection.close()


def attendance_menu():

    while True:

        print("\n" + "=" * 45)
        print("       ATTENDANCE MANAGEMENT")
        print("=" * 45)
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Search Attendance")
        print("4. Attendance Report")
        print("5. Back")
        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":

            mark_attendance()

        elif choice == "2":

            view_attendance()

        elif choice == "3":

            search_attendance()

        elif choice == "4":

            attendance_report()

        elif choice == "5":

            break

        else:

            print("\n❌ Invalid Choice.")
            