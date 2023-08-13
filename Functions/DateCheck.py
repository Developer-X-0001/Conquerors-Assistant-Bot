import re
import config
from datetime import datetime

def isDateFormat(input: str):
    match = re.match(config.DATE_PATTERN, input)
    if match:
        return True
    else:
        return False

def isFutureDate(input: str):
    today = datetime.today().date()
    input_date = datetime.strptime(input, "%m/%d/%Y").date()

    return input_date > today

def isPastDate(input: str):
    today = datetime.today().date()
    input_date = datetime.strptime(input, "%m/%d/%Y").date()

    return today > input_date

def formatDate(date_input: str):
    parts = date_input.split('/')
    month = parts[0].rjust(2, '0')
    day = parts[1].rjust(2, '0')
    year = parts[2]
    return f"{month}/{day}/{year}"
