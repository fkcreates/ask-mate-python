import connection
import time

def generate_id(filename):
    max_id = len(connection.csv_reader(filename))
    generated_id = max_id + 1
    return generated_id

def get_current_time():
    timestamp = time.time()

    return timestamp