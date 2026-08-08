from services.database import get_connection
from utils.logger import logging


def add_class():

    print("\n========== ADD CLASS ==========\n")

    name = input("Enter Class Name: ")
    department_id = input("Enter Department ID: ")

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            INSERT INTO classes (ClassName, DepartmentID)
            VALUES (%s, %s)
            """

            cursor.execute(query, (name, department_id))
            connection.commit()

            print("\n✅ Class Added Successfully!")

            logging.info(f"Class Added: {name}")

        except Exception as e:

            connection.rollback()

            print(f"\n❌ Error: {e}")
            logging.error(f"Error adding class: {e}")

        finally:

            cursor.close()
            connection.close()


def view_classes():

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            SELECT
                c.ClassID,
                c.ClassName,
                d.DepartmentName,
                c.CreatedAt
            FROM classes c
            JOIN departments d
                ON c.DepartmentID = d.DepartmentID
            ORDER BY c.ClassID
            """

            cursor.execute(query)

            classes = cursor.fetchall()

            print("\n" + "=" * 75)
            print("CLASS RECORDS")
            print("=" * 75)

            if classes:

                for class_data in classes:

                    print(f"""
Class ID       : {class_data[0]}
Class Name     : {class_data[1]}
Department     : {class_data[2]}
Created At     : {class_data[3]}
------------------------------------------------------------
""")

            else:

                print("No classes found.")

            logging.info("Viewed all classes.")

        except Exception as e:

            print(f"\n❌ Error: {e}")
            logging.error(f"Error viewing classes: {e}")

        finally:

            cursor.close()
            connection.close()


def search_class():

    class_id = input("\nEnter Class ID: ")

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            SELECT
                c.ClassID,
                c.ClassName,
                d.DepartmentName,
                c.CreatedAt
            FROM classes c
            JOIN departments d
                ON c.DepartmentID = d.DepartmentID
            WHERE c.ClassID = %s
            """

            cursor.execute(query, (class_id,))

            class_data = cursor.fetchone()

            if class_data:

                print("\n========== CLASS FOUND ==========\n")

                print(f"Class ID       : {class_data[0]}")
                print(f"Class Name     : {class_data[1]}")
                print(f"Department     : {class_data[2]}")
                print(f"Created At     : {class_data[3]}")

            else:

                print("\n❌ Class Not Found.")

            logging.info(f"Class Search: {class_id}")

        except Exception as e:

            print(f"\n❌ Error: {e}")
            logging.error(f"Error searching class: {e}")

        finally:

            cursor.close()
            connection.close()


def update_class():

    class_id = input("\nEnter Class ID: ")
    name = input("Enter New Class Name: ")
    department_id = input("Enter New Department ID: ")

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            UPDATE classes
            SET
                ClassName = %s,
                DepartmentID = %s
            WHERE ClassID = %s
            """

            cursor.execute(
                query,
                (name, department_id, class_id)
            )

            if cursor.rowcount > 0:

                connection.commit()

                print("\n✅ Class Updated Successfully!")

                logging.info(f"Class Updated: {class_id}")

            else:

                print("\n❌ Class Not Found.")

        except Exception as e:

            connection.rollback()

            print(f"\n❌ Error: {e}")
            logging.error(f"Error updating class: {e}")

        finally:

            cursor.close()
            connection.close()


def delete_class():

    class_id = input("\nEnter Class ID: ")

    confirmation = input(
        "Are you sure you want to delete this class? (Y/N): "
    )

    if confirmation.lower() != "y":

        print("\nDelete operation cancelled.")

        return

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = "DELETE FROM classes WHERE ClassID = %s"

            cursor.execute(query, (class_id,))

            if cursor.rowcount > 0:

                connection.commit()

                print("\n✅ Class Deleted Successfully!")

                logging.info(f"Class Deleted: {class_id}")

            else:

                print("\n❌ Class Not Found.")

        except Exception as e:

            connection.rollback()

            print(f"\n❌ Error: {e}")
            logging.error(f"Error deleting class: {e}")

        finally:

            cursor.close()
            connection.close()


def class_menu():

    while True:

        print("\n" + "=" * 45)
        print("          CLASS MANAGEMENT")
        print("=" * 45)
        print("1. Add Class")
        print("2. View Classes")
        print("3. Search Class")
        print("4. Update Class")
        print("5. Delete Class")
        print("6. Back")
        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":

            add_class()

        elif choice == "2":

            view_classes()

        elif choice == "3":

            search_class()

        elif choice == "4":

            update_class()

        elif choice == "5":

            delete_class()

        elif choice == "6":

            break

        else:

            print("\n❌ Invalid Choice.")
            