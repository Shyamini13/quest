from flask import *

app= Flask(__name__)

@app.route('/js')
def myjs():
    return render_template('day2.html')













if __name__=="__main__":
    app.run(debug=True)