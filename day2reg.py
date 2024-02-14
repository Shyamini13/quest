from flask import *

app=Flask(__name__)
app.secret_key='wwww'


@app.route('/')
def emp_reg():
    return render_template('regday2.html')

@app.route('/su',methods=['GET','POST'])
def emp_details():
    # return success

    if request.method=="POST":
        res=request.form
        return render_template('mydetails.html',data=res)

@app.route('/cs')
def cook_set():
    res=make_response("<h1>cookie set </h1>")
    res.set_cookie('place','eklm')
    return res

@app.route('/cg')
def cook_get():
    res=request.cookies.get('place')
    return res


@app.route('/ss')
def sess_set():
    res=make_response("<h1>session is set <a href='sg'>view details</a></h1>")
    session['phone']=7778888
    return res


@app.route('/sg')
def sess_get():
    if 'phone' in session:
        c=session['phone']
        return 'my session value is %d <a href ="/sd">logout</a> '%c
    else:
        return 'no session values found'


@app.route('/sd')
def sess_del():
    if 'phone' in session:
        session.pop('phone',None)
        return 'logouted'
    else:
        return 'no session values found'


@app.route('/upld')
def emp_upload():
    return render_template('myimg.html')

@app.route('/upldsave',methods=['POST'])
def emp_upld_save():
    if request.method=="POST":
        f=request.files['img']
        f.save(f.filename)
        return 'success'















if __name__=="__main__":
    app.run(debug=True) 