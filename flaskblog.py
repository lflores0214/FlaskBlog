from flask import Flask, render_template, url_for

app = Flask(__name__)


posts = [
    {
        'author': 'luis flores',
        'title': 'Blog Post 1',
        'content': 'First blog post',
        'date_posted': 'April 2, 2021'
    },
    {
        'author': 'Abigail Fischer',
        'title': 'Blog Post 2',
        'content': 'Second blog content',
        'date_posted': 'April 4, 2021'
    }
]


@app.route("/")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="about")


if __name__ == "__main__":
    app.run(debug=True)
