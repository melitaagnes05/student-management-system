from services.database import get_connection
from utils.logger import logging


def add_student():

    print("\n========== ADD STUDENT ==========\n")

    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender (Male/Female/Other): ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    address = input("Enter Address: ")
    department_id = int(input("Enter Department ID: "))
    class_id = int(input("Enter Class ID: "))
    admission_date = input("Enter Admission Date (YYYY-MM-DD): ")

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        try:

            query = """
            INSERT INTO students
            (StudentName, Age, Gender, Email, Phone, Address,
            DepartmentID, ClassID, AdmissionDate)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """

            values = (
                name,
                age,
                gender,
                email,
                phone,
                address,
                department_id,
                class_id,
                admission_date
            )

            cursor.execute(query, values)

            connection.commit()

            print("\n✅ Student Added Successfully!")

            logging.info(f"Student Added : {name}")

        except Exception as e:

            print("Error :", e)

        finally:

            cursor.close()
            connection.close()


def view_students():

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        query = """
        SELECT
            s.StudentID,
            s.StudentName,
            s.Age,
            s.Gender,
            s.Email,
            s.Phone,
            s.Address,
            d.DepartmentName,
            c.ClassName,
            s.AdmissionDate
        FROM students s
        JOIN departments d
            ON s.DepartmentID=d.DepartmentID
        JOIN classes c
            ON s.ClassID=c.ClassID
        ORDER BY s.StudentID
        """

        cursor.execute(query)

        students = cursor.fetchall()

        print("\n" + "=" * 90)
        print("STUDENT RECORDS")
        print("=" * 90)

        if students:

            for student in students:

                print(f"""
Student ID      : {student[0]}
Name            : {student[1]}
Age             : {student[2]}
Gender          : {student[3]}
Email           : {student[4]}
Phone           : {student[5]}
Address         : {student[6]}
Department      : {student[7]}
Class           : {student[8]}
Admission Date  : {student[9]}
------------------------------------------------------------
""")

        else:

            print("No students found.")

        logging.info("Viewed Students")

        cursor.close()
        connection.close()


def search_student():

    student_id = input("Enter Student ID : ")

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        query = """
        SELECT
            s.StudentID,
            s.StudentName,
            s.Age,
            s.Gender,
            s.Email,
            s.Phone,
            s.Address,
            d.DepartmentName,
            c.ClassName,
            s.AdmissionDate
        FROM students s
        JOIN departments d
            ON s.DepartmentID=d.DepartmentID
        JOIN classes c
            ON s.ClassID=c.ClassID
        WHERE s.StudentID=%s
        """

        cursor.execute(query, (student_id,))

        student = cursor.fetchone()

        if student:

            print("\n========== STUDENT FOUND ==========\n")

            print(f"Student ID      : {student[0]}")
            print(f"Name            : {student[1]}")
            print(f"Age             : {student[2]}")
            print(f"Gender          : {student[3]}")
            print(f"Email           : {student[4]}")
            print(f"Phone           : {student[5]}")
            print(f"Address         : {student[6]}")
            print(f"Department      : {student[7]}")
            print(f"Class           : {student[8]}")
            print(f"Admission Date  : {student[9]}")

        else:

            print("Student Not Found.")

        cursor.close()
        connection.close()


def update_student():

    student_id = input("Enter Student ID : ")

    name = input("Enter New Name : ")
    age = int(input("Enter New Age : "))
    email = input("Enter New Email : ")
    phone = input("Enter New Phone : ")
    address = input("Enter New Address : ")

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        query = """
        UPDATE students
        SET
        StudentName=%s,
        Age=%s,
        Email=%s,
        Phone=%s,
        Address=%s
        WHERE StudentID=%s
        """

        values = (
            name,
            age,
            email,
            phone,
            address,
            student_id
        )

        cursor.execute(query, values)

        connection.commit()

        print("\n✅ Student Updated Successfully!")

        logging.info(f"Student Updated : {student_id}")

        cursor.close()
        connection.close()


def delete_student():

    student_id = input("Enter Student ID : ")

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        query = "DELETE FROM students WHERE StudentID=%s"

        cursor.execute(query, (student_id,))

        connection.commit()

        print("\n✅ Student Deleted Successfully!")

        logging.info(f"Student Deleted : {student_id}")

        cursor.close()
        connection.close()


def student_menu():

    while True:

        print("\n" + "=" * 45)
        print("        STUDENT MANAGEMENT")
        print("=" * 45)
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back")
        print("=" * 45)

        choice = input("Enter your choice : ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            break

        else:
            print("Invalid Choice.")