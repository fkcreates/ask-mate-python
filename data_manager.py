import connection
import util


def get_data_from_file(filename):

    return connection.read_data_from_file(filename)


def get_all_questions():

    return get_data_from_file(connection.QUESTIONS_PATH)


def get_all_answers():

    return get_data_from_file(connection.ANSWERS_PATH)


def generate_question_id():
    max_id = len(connection.read_data_from_file(connection.QUESTIONS_PATH)) - 1
    generated_id = max_id + 1
    return generated_id


def generate_answer_id():
    max_id = len(connection.read_data_from_file(connection.ANSWERS_PATH)) - 1
    generated_id = max_id + 1
    return generated_id


def write_questions(dictionary):
    return connection.write_data_to_file(dictionary, connection.QUESTIONS_PATH, connection.QUESTIONS_HEADER)


def write_answers(dictionary):
    return connection.write_data_to_file(dictionary, connection.ANSWERS_PATH, connection.ANSWERS_HEADER)