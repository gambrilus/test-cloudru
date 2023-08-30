# import main Flask class and request object
from flask import Flask, request
import os

# create the Flask app
app = Flask(__name__)
app.config.from_pyfile('settings.py')

@app.route('/hostname')
def hostname():
    return f'{ app.config.get("HOSTNAME") }'


@app.route('/author')
def author():
    return f'{ app.config.get("AUTHOR") }'

@app.route('/id')
def id():
    return 'JSON Object Example'

if __name__ == '__main__':
    # run app in debug mode on port 8000
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)