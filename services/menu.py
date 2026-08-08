from services.auth_service import login, logout
from services.student_service import student_menu
from services.teacher_service import teacher_menu
from services.department_service import department_menu

def dashboard():

    while True:

        print("\n" + "=" * 50)
        print("      STUDENT MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Student Management")
        print("2. Teacher Management")
        print("3. Department Management")
        print("4. Class Management")
        print("5. Attendance Management")
        print("6. Marks Management")
        print("7. Reports")
        print("8. Logout")
        print("9. Exit")
        print("=" * 50)

        choice = input("Enter your choice : ")

        if choice == "1":
            student_menu()

        elif choice == "2":
            teacher_menu()

        elif choice == "3":
            department_menu()

        elif choice == "4":
            print("Class Module Coming Soon")

        elif choice == "5":
            print("Attendance Module Coming Soon")

        elif choice == "6":
            print("Marks Module Coming Soon")

        elif choice == "7":
            print("Reports Module Coming Soon")

        elif choice == "8":
            logout()
            break

        elif choice == "9":
            print("\nThank you for using Student Management System.")
            exit()

        else:
            print("Invalid Choice")


def home_menu():

    while True:

        print("\n" + "=" * 50)
        print("      STUDENT MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Login")
        print("2. Exit")
        print("=" * 50)

        choice = input("Enter your choice : ")

        if choice == "1":

            if login():
                dashboard()

        elif choice == "2":

            print("\nThank you for using Student Management System.")
            break

        else:

            print("Invalid Choice")