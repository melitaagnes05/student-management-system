from services.database import get_connection
from utils.logger import logging


def add_department():

    print("\n========== ADD DEPARTMENT ==========\n")

    name = input("Enter Department Name: ")

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = "INSERT INTO departments (DepartmentName) VALUES (%s)"

            cursor.execute(query, (name,))
            connection.commit()

            print("\n✅ Department Added Successfully!")

            logging.info(f"Department Added: {name}")

        except Exception as e:

            connection.rollback()

            print(f"\n❌ Error: {e}")
            logging.error(f"Error adding department: {e}")

        finally:

            cursor.close()
            connection.close()


def view_departments():

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            SELECT
                DepartmentID,
                DepartmentName,
                CreatedAt
            FROM departments
            ORDER BY DepartmentID
            """

            cursor.execute(query)

            departments = cursor.fetchall()

            print("\n" + "=" * 70)
            print("DEPARTMENT RECORDS")
            print("=" * 70)

            if departments:

                for department in departments:

                    print(f"""
Department ID   : {department[0]}
Department Name : {department[1]}
Created At      : {department[2]}
------------------------------------------------------------
""")

            else:

                print("No departments found.")

            logging.info("Viewed all departments.")

        except Exception as e:

            print(f"\n❌ Error: {e}")
            logging.error(f"Error viewing departments: {e}")

        finally:

            cursor.close()
            connection.close()


def search_department():

    department_id = input("\nEnter Department ID: ")

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            SELECT
                DepartmentID,
                DepartmentName,
                CreatedAt
            FROM departments
            WHERE DepartmentID = %s
            """

            cursor.execute(query, (department_id,))

            department = cursor.fetchone()

            if department:

                print("\n========== DEPARTMENT FOUND ==========\n")

                print(f"Department ID   : {department[0]}")
                print(f"Department Name : {department[1]}")
                print(f"Created At      : {department[2]}")

            else:

                print("\n❌ Department Not Found.")

            logging.info(f"Department Search: {department_id}")

        except Exception as e:

            print(f"\n❌ Error: {e}")
            logging.error(f"Error searching department: {e}")

        finally:

            cursor.close()
            connection.close()


def update_department():

    department_id = input("\nEnter Department ID: ")
    name = input("Enter New Department Name: ")

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            UPDATE departments
            SET DepartmentName = %s
            WHERE DepartmentID = %s
            """

            cursor.execute(query, (name, department_id))

            if cursor.rowcount > 0:

                connection.commit()

                print("\n✅ Department Updated Successfully!")

                logging.info(f"Department Updated: {department_id}")

            else:

                print("\n❌ Department Not Found.")

        except Exception as e:

            connection.rollback()

            print(f"\n❌ Error: {e}")
            logging.error(f"Error updating department: {e}")

        finally:

            cursor.close()
            connection.close()


def delete_department():

    department_id = input("\nEnter Department ID: ")

    confirmation = input(
        "Are you sure you want to delete this department? (Y/N): "
    )

    if confirmation.lower() != "y":

        print("\nDelete operation cancelled.")

        return

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = "DELETE FROM departments WHERE DepartmentID = %s"

            cursor.execute(query, (department_id,))

            if cursor.rowcount > 0:

                connection.commit()

                print("\n✅ Department Deleted Successfully!")

                logging.info(f"Department Deleted: {department_id}")

            else:

                print("\n❌ Department Not Found.")

        except Exception as e:

            connection.rollback()

            print(f"\n❌ Error: {e}")
            logging.error(f"Error deleting department: {e}")

        finally:

            cursor.close()
            connection.close()


def department_menu():

    while True:

        print("\n" + "=" * 45)
        print("       DEPARTMENT MANAGEMENT")
        print("=" * 45)
        print("1. Add Department")
        print("2. View Departments")
        print("3. Search Department")
        print("4. Update Department")
        print("5. Delete Department")
        print("6. Back")
        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":

            add_department()

        elif choice == "2":

            view_departments()

        elif choice == "3":

            search_department()

        elif choice == "4":

            update_department()

        elif choice == "5":

            delete_department()

        elif choice == "6":

            break

        else:

            print("\n❌ Invalid Choice.")