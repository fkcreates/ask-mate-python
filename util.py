import connection
import time
import data_manager


def get_current_time():
    timestamp = time.time()

    return timestamp

def sort_questions_by_timestamp():
    data = connection.read_data_from_file(connection.QUESTIONS_PATH)

    sorted_data = sorted(data, key=lambda k: k["submission_time"], reverse=True)

    return sorted_data

def sort_answers_by_timestamp():
    data = connection.read_data_from_file(connection.ANSWERS_PATH)

    sorted_data = sorted(data, key=lambda k: k["submission_time"], reverse=True)

    return sorted_data
