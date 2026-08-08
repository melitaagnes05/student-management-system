import bcrypt

from services.database import get_connection
from utils.logger import logging


def login():

    username = input("\nEnter Username : ")
    password = input("Enter Password : ")

    connection = get_connection()

    if not connection:
        return False

    cursor = connection.cursor()

    try:

        query = """
        SELECT Username, Password, Role
        FROM users
        WHERE Username = %s
        """

        cursor.execute(query, (username,))

        user = cursor.fetchone()

        if user:

            stored_password = user[1]

            if bcrypt.checkpw(
                password.encode("utf-8"),
                stored_password.encode("utf-8")
            ):

                logging.info(
                    f"{username} logged in successfully."
                )

                print("\n✅ Login Successful!")
                print(f"Welcome {user[0]} ({user[2]})")

                return True

        logging.warning(
            f"Failed login attempt for {username}"
        )

        print("\n❌ Invalid Username or Password")

        return False

    except Exception as e:

        print(f"\n❌ Login Error: {e}")

        logging.error(
            f"Login error: {e}"
        )

        return False

    finally:

        cursor.close()
        connection.close()


def logout():

    print("\n✅ Logged Out Successfully!")

    logging.info("User Logged Out")