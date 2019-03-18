import csv
import os
QUESTIONS_HEADER = ["id", "submission_time", "view_number", "vote_number", "title", "message", "image"]
ANSWERS_HEADER = ["id", "submission_time", "vote_number", "question_id", "message", "image"]

ANSWERS_PATH = "sample_data/answer.csv"
QUESTIONS_PATH = "sample_data/question.csv"

def csv_reader(filename):
    answers = []
    with open(filename) as file:
        reader = csv.DictReader(file)

        for row in reader:
            answers.append(dict(row))

    return answers