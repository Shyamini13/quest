from flask import Flask

app= Flask(__name__)  #creating a flask class obj

@app.route('/aa')  #url mapping associated with function syntax app.route(rule,option)

def home():
    return "<h1>welcome to flask</h1>"

@app.route('/hai/<myname>')
def details(myname):
    return 'hai my name is '+myname

@app.route('/hai/<int:num>')
def mynum(num):
    return 'my num is %d'%num

@app.route('/hai/<int:num>')
def myhome():
    return "my home page"

app.add_url_rule("/myhome1","myhome2",myhome)
if __name__=="__main__":
    app.run(debug=True)  #app.run(host,port.debug,options)
    