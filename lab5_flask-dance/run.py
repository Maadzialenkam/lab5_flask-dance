from flask import Flask # importujemy bibliotekę Flask, za pomocą której utworzymy naszą pierwszą aplikację app = Flask(__name__)
from flask import request # umożliwia dostęp do żądania otrzymanego przez serwer
from flask import  render_template # pozwala wykorzystywać szablony w plikach HTML
from flask import abort, redirect, url_for, make_response # są użytecznymi modułami do obsługi błędów, przekierowania oraz modyfikowania nagłówka odpowiedzi HTTP

                    

app = Flask(__name__)
                    # tworzymy samą aplikację

#HOME
@app.route('/')
def home():
    return render_template('index.html')


# CONTACT
@app.route("/contact")
def contact():
    return render_template('contact.html')
                    
# GALLERY
@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

# ABOUT ME
@app.route("/aboutme")
def aboutme():
    return render_template('aboutme.html')


if(__name__)=='__main__':
    app.run(host='0.0.0.0')
                    # uruchamiamy aplikację