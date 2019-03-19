from flask import Flask, render_template, request, redirect, url_for
import data_manager
import util


app = Flask(__name__)


@app.route('/')
@app.route('/list')
def list_questions():
    questions = data_manager.get_all_questions()
    sorted_questions = util.sort_questions_by_timestamp()
    return render_template("list_questions.html", questions=sorted_questions)


@app.route('/question/<question_id>')
def display_question(question_id: int):
    answers = data_manager.get_all_answers()
    questions = data_manager.get_all_questions()

    return render_template("display_question.html", answers=answers, questions=questions, question_id=question_id)


@app.route("/add-question", methods=["GET"])
def route_add_question():
    return render_template("new_question_form.html")

@app.route("/add-question", methods=["POST"])
def add_new_question():

    new_question = {
        "id": data_manager.generate_question_id(),
        "submission_time": util.get_current_time(),
        "view_number": 0,
        "vote_number": 0,
        "title": request.form.get("title"),
        "message": request.form.get("message"),
    }

    data_manager.write_questions(new_question)
    return redirect("/")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
