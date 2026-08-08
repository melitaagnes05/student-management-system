import re
from datetime import datetime


def validate_email(email):

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(pattern, email) is not None


def validate_phone(phone):

    return phone.isdigit() and 10 <= len(phone) <= 15


def validate_positive_integer(value):

    try:

        return int(value) > 0

    except ValueError:

        return False


def validate_marks(marks):

    try:

        marks = int(marks)

        return 0 <= marks <= 100

    except ValueError:

        return False


def validate_date(date):

    try:

        datetime.strptime(date, "%Y-%m-%d")

        return True

    except ValueError:

        return False