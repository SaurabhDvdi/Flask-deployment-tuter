from flask import Flask, render_template
import urllib.request
import json

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

@app.route('/learn')
def learn():
    try:
        url = "https://en.wikipedia.org/api/rest_v1/page/summary/Flask_(web_framework)"
        
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'FlaskTutorialApp/1.0')
        
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
        
        content = f"""
        <h3>{data.get('title', 'Flask')}</h3>
        <p>{data.get('extract', 'Flask is a micro web framework written in Python.')}</p>
        
        <h3>Key Information</h3>
        <p><strong>Description:</strong> {data.get('description', 'Python web framework')}</p>
        
        <h3>Learn More</h3>
        <p>Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.</p>
        
        <p><a href="{data.get('content_urls', {}).get('desktop', {}).get('page', 'https://flask.palletsprojects.com/')}" target="_blank" style="color: #3498db;">Read more on Wikipedia</a></p>
        
        <p><a href="https://flask.palletsprojects.com/" target="_blank" style="color: #3498db;">Official Flask Documentation</a></p>
        """
        
        return render_template('learn.html', content=content, error=None)
    
    except Exception as e:
        error_message = f"Unable to fetch content from API: {str(e)}"
        return render_template('learn.html', content=None, error=error_message)

if __name__ == '__main__':
    app.run(host='74.220.48.0/24', debug=True)
  