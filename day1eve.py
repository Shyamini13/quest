from flask import *
app=Flask(__name__)


@app.route('/login',methods=['post'])
def reg():
    # get 
    # uname=request.args.get('fname')
    # place=request.args.get('pla')

    # post
    uname=request.form['fname']
    place=request.form['pla']
    return 'success'+uname

