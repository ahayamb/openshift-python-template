import os

# PATH_NAME = 'OPENSHIFT_PYTHON_DIR'
# virtenv = os.environ.get(PATH_NAME, '') + 'virtenv/venv/'
# virtualenv = os.path.join(virtenv, 'bin/activate_this.py')

# try:
# 	exec(compile(open(virtualenv, 'rb').read(), virtualenv, 'exec'), dict(__file__=virtualenv))
# except:
# 	pass

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug = True)