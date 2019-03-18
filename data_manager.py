import connection


def get_data_from_file(filename):

    return connection.csv_reader(filename)

def get_all_questions():

    return get_data_from_file(connection.QUESTIONS_PATH)

def get_all_answers():

    return get_data_from_file(connection.ANSWERS_PATH)