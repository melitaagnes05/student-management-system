from services.database import get_connection
from utils.logger import logging


def add_marks():

    print("\n========== ADD MARKS ==========\n")

    student_id = input("Enter Student ID: ")
    subject = input("Enter Subject: ")
    marks = int(input("Enter Marks: "))
    semester = int(input("Enter Semester: "))

    if marks < 0 or marks > 100:
        print("\n❌ Marks must be between 0 and 100.")
        return

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            INSERT INTO marks
            (StudentID, Subject, Marks, Semester)
            VALUES (%s, %s, %s, %s)
            """

            cursor.execute(
                query,
                (student_id, subject, marks, semester)
            )

            connection.commit()

            print("\n✅ Marks Added Successfully!")

            logging.info(
                f"Marks added for Student {student_id}"
            )

        except Exception as e:

            connection.rollback()

            print(f"\n❌ Error: {e}")
            logging.error(f"Error adding marks: {e}")

        finally:

            cursor.close()
            connection.close()


def view_marks():

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            SELECT
                m.MarkID,
                s.StudentID,
                s.StudentName,
                m.Subject,
                m.Marks,
                m.Semester
            FROM marks m
            JOIN students s
                ON m.StudentID = s.StudentID
            ORDER BY s.StudentID, m.Semester, m.Subject
            """

            cursor.execute(query)

            records = cursor.fetchall()

            print("\n" + "=" * 85)
            print("MARKS RECORDS")
            print("=" * 85)

            if records:

                for record in records:

                    print(f"""
Mark ID      : {record[0]}
Student ID   : {record[1]}
Student Name : {record[2]}
Subject      : {record[3]}
Marks        : {record[4]}
Semester     : {record[5]}
------------------------------------------------------------
""")

            else:

                print("No marks records found.")

            logging.info("Viewed all marks records.")

        except Exception as e:

            print(f"\n❌ Error: {e}")
            logging.error(f"Error viewing marks: {e}")

        finally:

            cursor.close()
            connection.close()


def search_marks():

    student_id = input("\nEnter Student ID: ")

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            SELECT
                m.MarkID,
                s.StudentID,
                s.StudentName,
                m.Subject,
                m.Marks,
                m.Semester
            FROM marks m
            JOIN students s
                ON m.StudentID = s.StudentID
            WHERE s.StudentID = %s
            ORDER BY m.Semester, m.Subject
            """

            cursor.execute(query, (student_id,))

            records = cursor.fetchall()

            print("\n" + "=" * 85)
            print("STUDENT MARKS")
            print("=" * 85)

            if records:

                for record in records:

                    print(f"""
Mark ID      : {record[0]}
Student ID   : {record[1]}
Student Name : {record[2]}
Subject      : {record[3]}
Marks        : {record[4]}
Semester     : {record[5]}
------------------------------------------------------------
""")

            else:

                print("\n❌ No marks records found.")

            logging.info(
                f"Marks searched for Student {student_id}"
            )

        except Exception as e:

            print(f"\n❌ Error: {e}")
            logging.error(f"Error searching marks: {e}")

        finally:

            cursor.close()
            connection.close()


def update_marks():

    mark_id = input("\nEnter Mark ID: ")
    subject = input("Enter New Subject: ")
    marks = int(input("Enter New Marks: "))
    semester = int(input("Enter New Semester: "))

    if marks < 0 or marks > 100:
        print("\n❌ Marks must be between 0 and 100.")
        return

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            UPDATE marks
            SET
                Subject = %s,
                Marks = %s,
                Semester = %s
            WHERE MarkID = %s
            """

            cursor.execute(
                query,
                (subject, marks, semester, mark_id)
            )

            if cursor.rowcount > 0:

                connection.commit()

                print("\n✅ Marks Updated Successfully!")

                logging.info(
                    f"Marks Updated: {mark_id}"
                )

            else:

                print("\n❌ Mark Record Not Found.")

        except Exception as e:

            connection.rollback()

            print(f"\n❌ Error: {e}")
            logging.error(f"Error updating marks: {e}")

        finally:

            cursor.close()
            connection.close()


def delete_marks():

    mark_id = input("\nEnter Mark ID: ")

    confirmation = input(
        "Are you sure you want to delete this mark record? (Y/N): "
    )

    if confirmation.lower() != "y":

        print("\nDelete operation cancelled.")
        return

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = "DELETE FROM marks WHERE MarkID = %s"

            cursor.execute(query, (mark_id,))

            if cursor.rowcount > 0:

                connection.commit()

                print("\n✅ Marks Deleted Successfully!")

                logging.info(
                    f"Marks Deleted: {mark_id}"
                )

            else:

                print("\n❌ Mark Record Not Found.")

        except Exception as e:

            connection.rollback()

            print(f"\n❌ Error: {e}")
            logging.error(f"Error deleting marks: {e}")

        finally:

            cursor.close()
            connection.close()


def student_report_card():

    student_id = input("\nEnter Student ID: ")

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            SELECT
                s.StudentID,
                s.StudentName,
                m.Subject,
                m.Marks,
                m.Semester
            FROM marks m
            JOIN students s
                ON m.StudentID = s.StudentID
            WHERE s.StudentID = %s
            ORDER BY m.Semester, m.Subject
            """

            cursor.execute(query, (student_id,))

            records = cursor.fetchall()

            if not records:

                print("\n❌ No marks records found.")
                return

            student_name = records[0][1]

            total_marks = sum(record[3] for record in records)
            number_of_subjects = len(records)

            average = total_marks / number_of_subjects
            percentage = average

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 50:
                grade = "D"
            else:
                grade = "F"

            print("\n" + "=" * 70)
            print("              STUDENT REPORT CARD")
            print("=" * 70)

            print(f"Student ID   : {student_id}")
            print(f"Student Name : {student_name}")
            print("-" * 70)

            for record in records:

                print(
                    f"Semester: {record[4]} | "
                    f"Subject: {record[2]} | "
                    f"Marks: {record[3]}"
                )

            print("-" * 70)
            print(f"Total Marks  : {total_marks}")
            print(f"Subjects     : {number_of_subjects}")
            print(f"Average      : {average:.2f}")
            print(f"Percentage    : {percentage:.2f}%")
            print(f"Grade         : {grade}")
            print("=" * 70)

            logging.info(
                f"Report card generated for Student {student_id}"
            )

        except Exception as e:

            print(f"\n❌ Error: {e}")
            logging.error(
                f"Error generating report card: {e}"
            )

        finally:

            cursor.close()
            connection.close()


def marks_menu():

    while True:

        print("\n" + "=" * 45)
        print("          MARKS MANAGEMENT")
        print("=" * 45)
        print("1. Add Marks")
        print("2. View Marks")
        print("3. Search Marks")
        print("4. Update Marks")
        print("5. Delete Marks")
        print("6. Student Report Card")
        print("7. Back")
        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":

            add_marks()

        elif choice == "2":

            view_marks()

        elif choice == "3":

            search_marks()

        elif choice == "4":

            update_marks()

        elif choice == "5":

            delete_marks()

        elif choice == "6":

            student_report_card()

        elif choice == "7":

            break

        else:

            print("\n❌ Invalid Choice.")