from flask import Flask , request, url_for, render_template
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

app = Flask(__name__)
Bootstrap(app)

app.config.from_pyfile('config.cfg')

#mail = Mail(app)

s = URLSafeTimedSerializer('Thisissecret!')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    email = request.form['email']
    token = s.dumps(email, salt='email-confirm')
    
    #msg = Message('Confirm Email', sender='bilalahoor@gmail.com', recipients=[email])
    #link = url_for('confirm_email', token=token, _external=True) 
    #msg.body = 'Your link is {}'.format(link)
    
    #mail.send(msg)
    
    return '''
    <br>
    <h1>The email you entered is {}.
    <br>
    </h1> <h1>The token is: {}</h1>
    <br>
    
    <h2>your link to login:</h2>
    <a href= "http://127.0.0.1:5000/confirm_email/{}"> http://127.0.0.1:5000/confirm_email/{}</a>
    '''.format(email, token, token, token)


@app.route('/confirm_email/<token>')
def confirm_email(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=20)
    except SignatureExpired:
        return '<h1>The token is expired!</h1>'
    return '<h1>The token works!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
















 




















# app.config['MAIL_SERVER']
# app.config['MAIL_PORT']
# app.config['MAIL_USE_TLS']
# app.config['MAIL_USE_SSL']
# app.config['MAIL_DEBUG']
# app.config['MAIL_USERNAME']


