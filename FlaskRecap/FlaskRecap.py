'''
pip uninstall aniso8601==6.0.0 --y
pip uninstall appdirs==1.4.3 --y
pip uninstall colorama==0.4.3 --y
pip uninstall curl==0.0.1 --y
pip uninstall distlib==0.3.0 --y
pip uninstall filelock==3.0.12 --y
pip uninstall Flask-RESTful==0.3.7 --y
pip uninstall Flask-SQLAlchemy==2.4.0 --y
pip uninstall importlib-metadata==1.6.0 --y
pip uninstall psycopg2-binary==2.8.2 --y
pip uninstall pytz==2019.1 --y
pip uninstall SQLAlchemy==1.3.4 --y
pip uninstall virtualenv==20.0.17 --y
pip uninstall zipp==3.1.0 --y
'''
'''
pip install virtualenv
pip install curl
'''



#cd "C:\scripts\GH - complete\FSND-auth-example\FlaskRecap"
#virtualenv env
#pip uninstall -r requirements.txt -y
#pip install -r requirements.txt
#$env:FLASK_APP="C:\scripts\GH - complete\FSND-auth-example\FlaskRecap\FlaskRecap.py"
#$env:FLASK_ENV = "development"
#flask run

#pip3 install -r requirements.txt --ignore-installed
#pip freeze | xargs pip uninstall -y


#Alternative to FLASK_ENV is flask run --reload
#to delete envirmoents (env is name)
#    rm -r env 

from flask import Flask, request, jsonify, abort

app = Flask(__name__)

greetings = {
            'en': 'hello', 
            'es': 'Hola', 
            'ar': 'مرحبا',
            'ru': 'Привет',
            'fi': 'Hei',
            'he': 'שלום',
            'ja': 'こんにちは'
            }


@app.route('/greeting', methods=['GET'])
def greeting_all():
    return jsonify({'greetings': greetings})

@app.route('/greeting/<lang>', methods=['GET'])
def greeting_one(lang):
    print(lang)
    if(lang not in greetings):
        abort(404)
    return jsonify({'greeting': greetings[lang
    ]})

@app.route('/greeting', methods=['POST'])
def greeting_add():
    info = request.get_json()
    if('lang' not in info or 'greeting' not in info):
        abort(422)
    greetings[info['lang']] = info['greeting']
    return jsonify({'greetings':greetings})


@app.route('/')  #/ is home
def index():
    return('Hello!')

