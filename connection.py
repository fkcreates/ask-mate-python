import csv
import os


QUESTIONS_HEADER = ["id", "submission_time", "view_number", "vote_number", "title", "message", "image"]
ANSWERS_HEADER = ["id", "submission_time", "vote_number", "question_id", "message", "image"]

ANSWERS_PATH = "sample_data/answer.csv"
QUESTIONS_PATH = "sample_data/question.csv"


def read_data_from_file(filename):
    data = []
    with open(filename) as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(dict(row))

    return data


def write_data_to_file(dictionary, filename, fieldnames):
    data = read_data_from_file(filename)

    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            writer.writerow(row)
        writer.writerow(dictionary)


def delete_question_from_file(question_id):
    data = read_data_from_file(QUESTIONS_PATH)

    with open(QUESTIONS_PATH, "w") as file:
        writer = csv.DictWriter(file, QUESTIONS_HEADER)
        writer.writeheader()

        for row in data:
            if row["id"] != question_id:
                writer.writerow(row)

    return data


def delete_answer_by_question_id(question_id):
    data = read_data_from_file(ANSWERS_PATH)

    with open(ANSWERS_PATH, "w") as file:
        writer = csv.DictWriter(file, ANSWERS_HEADER)
        writer.writeheader()

        for row in data:
            if row["question_id"] != question_id:
                writer.writerow(row)

    return data