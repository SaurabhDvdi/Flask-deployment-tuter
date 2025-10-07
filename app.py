from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = "Welcome to Flask!"
    description = "This is a simple Flask application running on Replit."
    features = [
        {
            'title': 'Easy to Learn',
            'description': 'Flask is a lightweight web framework that\'s perfect for beginners.'
        },
        {
            'title': 'Flexible',
            'description': 'Build everything from simple websites to complex web applications.'
        },
        {
            'title': 'Well Documented',
            'description': 'Extensive documentation and a large community to help you.'
        }
    ]
    return render_template('index.html', title=title, description=description, features=features)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
  