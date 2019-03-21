import connection
import util


def get_data_from_file(filename):

    return connection.read_data_from_file(filename)


def get_all_questions():

    return get_data_from_file(connection.QUESTIONS_PATH)


def get_all_answers():

    return get_data_from_file(connection.ANSWERS_PATH)


def generate_question_id():
    file = connection.read_data_from_file(connection.QUESTIONS_PATH)
    list_of_ids = [item["id"] for item in file]
    return int(list_of_ids[-1])+1


def generate_answer_id():
    file = connection.read_data_from_file(connection.ANSWERS_PATH)
    list_of_ids = [item["id"] for item in file]
    return int(list_of_ids[-1]) + 1


def write_questions(dictionary):
    return connection.write_data_to_file(dictionary, connection.QUESTIONS_PATH, connection.QUESTIONS_HEADER)


def write_answers(dictionary):
    return connection.write_data_to_file(dictionary, connection.ANSWERS_PATH, connection.ANSWERS_HEADER)


def delete_question(question_id):
    return connection.delete_question_from_file(question_id)


def delete_answer_by_question_id(question_id):
    return connection.delete_answer_by_question_id(question_id)