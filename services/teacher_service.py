from services.database import get_connection
from utils.logger import logging


def add_teacher():

    print("\n========== ADD TEACHER ==========\n")

    name = input("Enter Teacher Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    department_id = input("Enter Department ID: ")

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            INSERT INTO teachers
            (TeacherName, Email, Phone, DepartmentID)
            VALUES (%s, %s, %s, %s)
            """

            values = (name, email, phone, department_id)

            cursor.execute(query, values)
            connection.commit()

            print("\n✅ Teacher Added Successfully!")

            logging.info(f"Teacher Added: {name}")

        except Exception as e:

            print(f"\n❌ Error: {e}")
            logging.error(f"Error adding teacher: {e}")

        finally:

            cursor.close()
            connection.close()


def view_teachers():

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
                d.DepartmentName,
                t.CreatedAt
            FROM teachers t
            JOIN departments d
                ON t.DepartmentID = d.DepartmentID
            ORDER BY t.TeacherID
            """

            cursor.execute(query)

            teachers = cursor.fetchall()

            print("\n" + "=" * 80)
            print("TEACHER RECORDS")
            print("=" * 80)

            if teachers:

                for teacher in teachers:

                    print(f"""
Teacher ID   : {teacher[0]}
Name         : {teacher[1]}
Email        : {teacher[2]}
Phone        : {teacher[3]}
Department   : {teacher[4]}
Created At   : {teacher[5]}
------------------------------------------------------------
""")

            else:

                print("No teachers found.")

            logging.info("Viewed all teachers.")

        except Exception as e:

            print(f"\n❌ Error: {e}")
            logging.error(f"Error viewing teachers: {e}")

        finally:

            cursor.close()
            connection.close()


def search_teacher():

    teacher_id = input("\nEnter Teacher ID: ")

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
                d.DepartmentName,
                t.CreatedAt
            FROM teachers t
            JOIN departments d
                ON t.DepartmentID = d.DepartmentID
            WHERE t.TeacherID = %s
            """

            cursor.execute(query, (teacher_id,))

            teacher = cursor.fetchone()

            if teacher:

                print("\n========== TEACHER FOUND ==========\n")

                print(f"Teacher ID   : {teacher[0]}")
                print(f"Name         : {teacher[1]}")
                print(f"Email        : {teacher[2]}")
                print(f"Phone        : {teacher[3]}")
                print(f"Department   : {teacher[4]}")
                print(f"Created At   : {teacher[5]}")

            else:

                print("\n❌ Teacher Not Found.")

            logging.info(f"Teacher Search: {teacher_id}")

        except Exception as e:

            print(f"\n❌ Error: {e}")
            logging.error(f"Error searching teacher: {e}")

        finally:

            cursor.close()
            connection.close()


def update_teacher():

    teacher_id = input("\nEnter Teacher ID: ")

    name = input("Enter New Name: ")
    email = input("Enter New Email: ")
    phone = input("Enter New Phone: ")
    department_id = input("Enter New Department ID: ")

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            UPDATE teachers
            SET
                TeacherName = %s,
                Email = %s,
                Phone = %s,
                DepartmentID = %s
            WHERE TeacherID = %s
            """

            values = (
                name,
                email,
                phone,
                department_id,
                teacher_id
            )

            cursor.execute(query, values)

            if cursor.rowcount > 0:

                connection.commit()

                print("\n✅ Teacher Updated Successfully!")

                logging.info(f"Teacher Updated: {teacher_id}")

            else:

                print("\n❌ Teacher Not Found.")

        except Exception as e:

            connection.rollback()

            print(f"\n❌ Error: {e}")
            logging.error(f"Error updating teacher: {e}")

        finally:

            cursor.close()
            connection.close()


def delete_teacher():

    teacher_id = input("\nEnter Teacher ID: ")

    confirmation = input(
        "Are you sure you want to delete this teacher? (Y/N): "
    )

    if confirmation.lower() != "y":

        print("\nDelete operation cancelled.")

        return

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = "DELETE FROM teachers WHERE TeacherID = %s"

            cursor.execute(query, (teacher_id,))

            if cursor.rowcount > 0:

                connection.commit()

                print("\n✅ Teacher Deleted Successfully!")

                logging.info(f"Teacher Deleted: {teacher_id}")

            else:

                print("\n❌ Teacher Not Found.")

        except Exception as e:

            connection.rollback()

            print(f"\n❌ Error: {e}")
            logging.error(f"Error deleting teacher: {e}")

        finally:

            cursor.close()
            connection.close()


def teacher_menu():

    while True:

        print("\n" + "=" * 45)
        print("        TEACHER MANAGEMENT")
        print("=" * 45)
        print("1. Add Teacher")
        print("2. View Teachers")
        print("3. Search Teacher")
        print("4. Update Teacher")
        print("5. Delete Teacher")
        print("6. Back")
        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":

            add_teacher()

        elif choice == "2":

            view_teachers()

        elif choice == "3":

            search_teacher()

        elif choice == "4":

            update_teacher()

        elif choice == "5":

            delete_teacher()

        elif choice == "6":

            break

        else:

            print("\n❌ Invalid Choice.")