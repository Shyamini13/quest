from flask import *
import sqlite3
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///anu.sqlite3'
app.config['SECRET_KEY']='abc'
db=SQLAlchemy(app)

class Employees(db.Model):
    id=db.Column('employee_id',db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    address=db.Column(db.String(20))

    def __init__(self,name,address):
        self.name=name
        self.address=address

@app.route('/add',methods=['GET','POST'])
def add_emp():
    if request.method=='POST':
        # return 'success'
        em =Employees(request.form['name'],request.form['address'])
        db.session.add(em)
        db.session.commit()
        return redirect(url_for ('display'))

    else:
        return render_template('add.html')

@app.route('/')
def display():
    return render_template('list.html',emp=Employees.query.all())




@app.route('/dele/<int:id>')
def list_del(id):
    emp=Employees.query.get(id)
    db.session.delete(emp)
    db.session.commit()
    return redirect(url_for ('display'))


@app.route('/edit/<int:id>')
def list_update(id):
    u=update(Employees)
    u=u.values({'employee_id':'id'})
    u=u.where(Employees.c.employee_id==id)
    return redirect(url_for ('display'))







if __name__=="__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True) 