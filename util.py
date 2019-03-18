import connection

def generate_id(filename):
    max_id = len(connection.csv_reader(filename))
    generated_id = max_id + 1
    return generated_id
