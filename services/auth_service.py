from services.database import get_connection
from utils.logger import logging


def login():

    username = input("\nEnter Username : ")
    password = input("Enter Password : ")

    connection = get_connection()

    if connection:

        cursor = connection.cursor()

        query = "SELECT Username, Role FROM users WHERE Username=%s AND Password=%s"

        cursor.execute(query, (username, password))

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:

            logging.info(f"{username} logged in successfully.")

            print(f"\n✅ Login Successful!")
            print(f"Welcome {user[0]} ({user[1]})")

            return True

        else:

            logging.warning(f"Failed login attempt for {username}")

            print("\n❌ Invalid Username or Password")

            return False


def logout():

    print("\n✅ Logged Out Successfully!")

    logging.info("User Logged Out")