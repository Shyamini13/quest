from flask import *
from flask_mail import *
app=Flask(__name__)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='dhabu944@gmail.com'
app.config['MAIL_PASSWORD']='gvas yigl iklt tyhx'
app.config['MAIL_USE-TLS']=False
app.config['MAIL_USE_SSL']=True

mail=Mail(app)

@app.route('/m')
def send_myemail():
    msg=Message('subject',sender="dhabu944@gmail.com",recipients=["shyamilikrishna85@gmail.com"])
    msg.body="my flask msg"
    mail.send(msg)
    return 'success'


if __name__=="__main__":
    app.run(debug=True)