from flask import Flask, render_template, request, redirect, url_for
import data_manager
import util


app = Flask(__name__)


@app.route('/')
@app.route('/list')
def list_questions():
    sorted_questions_by_timestamp = util.sort_questions_by_timestamp()
    sorted_questions_date_format = util.get_date_format_for_sorted_data(sorted_questions_by_timestamp)

    return render_template("list_questions.html", questions=sorted_questions_date_format)


@app.route('/question/<question_id>')
def display_question(question_id: int):

    sorted_answers = util.sort_answers_by_timestamp()
    sorted_answers_date_format = util.get_date_format_for_sorted_data(sorted_answers)

    sorted_questions = util.sort_questions_by_timestamp()
    sorted_questions_date_format = util.get_date_format_for_sorted_data(sorted_questions)

    return render_template("display_question.html", answers=sorted_answers_date_format, questions=sorted_questions_date_format, question_id=question_id)


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


@app.route("/question/<int:question_id>/new-answer", methods=["GET"])
def route_add_answer(question_id):
    return render_template("new_answer_form.html", question_id=question_id)


@app.route("/question/<question_id>/new-answer", methods=["POST"])
def add_new_answer(question_id):

    new_answer = {
        "id": data_manager.generate_answer_id(),
        "submission_time": util.get_current_time(),
        "vote_number": 0,
        "question_id": question_id,
        "message": request.form.get("message"),
    }

    data_manager.write_answers(new_answer)

    return redirect(url_for("display_question", question_id=question_id))


@app.route("/question/<question_id>/delete", methods=["GET"])
def confirm_delete_question(question_id):
    return render_template("confirm_delete_question.html", question_id=question_id)


@app.route("/question/<question_id>/delete", methods=["POST"])
def delete_question(question_id):

    data_manager.delete_question(question_id)
    data_manager.delete_answer_by_question_id(question_id)

    return redirect(url_for("list_questions"))


@app.route('/answer/<answer_id>/delete')
def delete_answer(answer_id):
    question_id = request.args.get("question_id")
    data_manager.delete_answer_by_answer_id(answer_id)

    return redirect(url_for("display_question", question_id=question_id))


@app.route("/question/<question_id>/edit", methods=["GET"])
def route_edit_question(question_id):
    data = data_manager.get_all_questions()
    return render_template("edit_question_form.html", question_id=question_id, questions=data)

@app.route('/question/<question_id>/edit', methods=[ "POST"])
def edit_question(question_id):

    edited_question = {
        "id": question_id,
        "submission_time": util.get_current_time(),
        "view_number": 0,
        "vote_number": 0,
        "title": request.form.get("title"),
        "message": request.form.get("message"),
    }


    questions = data_manager.update_question(edited_question, question_id)

    return redirect(url_for("display_question", question_id=question_id))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )
