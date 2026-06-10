from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
students = []


@app.route("/")
def home():
    return redirect(url_for("add_student"))


# ---------------------------------
# TODO: IMPLEMENT THIS ROUTE
# ---------------------------------
@app.route("/add", methods=["GET", "POST"])
def add_student():
    error = None

    if request.method == "POST":
        name = request.form.get("name")
        grade = request.form.get("grade")

        # TODO:
        # 1. Validate name
        if not name:
            error = "Please enter a name"
        # 2. Validate grade is number
        elif not grade:
            error = "Please enter a grade"
        elif not grade.isnumeric():
            error = "Please enter an integer for the grade"
    # 3. Validate grade range 0–100
        elif int(grade) < 0 or int(grade) > 100:
            error = "Grade must be between 0 and 100"
    # 4. Add to students list as dictionary
    # 5. Redirect to /students
        elif error is None:
            students.append({"name": name, "grade": grade})
            return redirect(url_for("display_students"))



    return render_template("add.html", error=error)


# ---------------------------------
# TODO: IMPLEMENT DISPLAY
# ---------------------------------
@app.route("/students")
def display_students():

    return render_template("students.html", students=students)


# ---------------------------------
# TODO: IMPLEMENT SUMMARY
# ---------------------------------
@app.route("/summary")
def summary():
    if not students:
        return render_template("summary.html", context={
            "error": "There are no students *in a friendly way*",
            "total_students": 0,
            "average_grade": 0,
            "highest_grade": 0,
            "lowest_grade": 0
        })
    # TODO:
    # Calculate:
    # - total students
    total_students = len(students)
    grades = [int(s["grade"]) for s in students]

    average_grade = sum(grades) / total_students
    highest_grade = max(grades)
    lowest_grade = min(grades)

    context = {
        "total_students": total_students,
        "average_grade": average_grade,
        "highest_grade": highest_grade,
        "lowest_grade": lowest_grade
    }
    return render_template("summary.html", context=context)


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
