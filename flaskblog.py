from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, RegistrationForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'e4f49b0f7a880f50cdda741e13a3e203'


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

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == "password":
            flash('You have been logged in !', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title="Login", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title="Register", form=form)





if __name__ == "__main__":
    app.run(debug=True)
