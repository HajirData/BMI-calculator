from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return  # Put any string here


if __name__ == "__main__":
    app.run(debug=True)


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello index page"


@app.route("/greet/<name>")
def greet(name):
    # modify this function to return "Hello, name"
    return f"Hello, {'replace_me'}"


@app.route("/multiply/<int:first_arg>/<int:second_arg>")
def multiply(first_arg: int, second_arg:int):
    return f"{'replace_me'}" # multiply args


if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello index page"


@app.route("/greet/<name>")
def greet(name):
    # modify this function to return "Hello, name"
    return f"Hello, {name}"


@app.route("/multiply/<int:first_arg>/<int:second_arg>")
def multiply(first_arg: int, second_arg:int):
    return f"{first_arg * second_arg}" # multiply args


with app.test_request_context():
    print(url_for("index"))
    print(url_for("multiply", first_arg=333, second_arg=3))
    print(url_for("multiply", first_arg=333, second_arg=3, as_complex=True))


if __name__ == "__main__":
    app.run(debug=True)



@app.route("/", methods=["GET", "POST"])
def calculate_bmi():
    if request.method == "POST":
        height = int(request.form.get("height"))
        weight = int(request.form.get("weight"))
        bmi = weight / ((height / 100) ** 2)
        return render_template("index.html", bmi=bmi)
    return render_template("index.html")
