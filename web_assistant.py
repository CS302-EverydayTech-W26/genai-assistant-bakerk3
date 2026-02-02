from gemini_client import *
from flask import Flask
from flask import render_template

def main():
    app = Flask(__name__)

    client = GeminiClient()

    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html', title='Home')
        # return 'The Web App with Python Flask!'
    
    @app.route('/prompt/<prompt>')
    def prompt(prompt):
        return client.generate_response(prompt)
    
    app.run(host='0.0.0.0', port=81)

if __name__ == "__main__":
  main()