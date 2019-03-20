import connection
from datetime import datetime
import time
import data_manager
import csv


def get_current_time():
    timestamp = time.time()
    timestamp = round(timestamp)

    return timestamp


def sort_questions_by_timestamp():
    data = connection.read_data_from_file(connection.QUESTIONS_PATH)

    sorted_data = sorted(data, key=lambda k: k["submission_time"], reverse=True)

    return sorted_data


def sort_answers_by_timestamp():
    data = connection.read_data_from_file(connection.ANSWERS_PATH)

    sorted_data = sorted(data, key=lambda k: k["submission_time"], reverse=True)

    return sorted_data


def get_date_format_for_sorted_data(data):

    for row in data:
        timestamp = int(row["submission_time"])
        row["submission_time"] = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M")

    return data

