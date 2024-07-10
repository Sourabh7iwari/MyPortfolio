from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/experiences')
def experiences():
    return render_template('experiences.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')


if __name__== '__main__':
    app.run(debug=True)