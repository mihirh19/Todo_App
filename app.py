
from datetime import datetime
from distutils.log import debug
#hello
from email.policy import default
import mailbox
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
# from matplotlib.pyplot import title

# from sqlalchemy import desc
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///form.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class todo(db.Model): # type: ignore
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    Date = db.Column(db.DateTime, default = datetime.utcnow())

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route("/", methods = ['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        # print(request.form['title'])
        title = request.form['title']
        desc = request.form['desc']
        to = todo(title=title, desc=desc)
        db.session.add(to)
        db.session.commit()

    all = todo.query.all()
    return render_template('index.html', alltodo = all)

@app.route('/update/<int:sno>', methods = ['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        to = todo.query.filter_by(sno=sno).first()
        to.title = title
        to.desc = desc
        db.session.add(to)
        db.session.commit()
        return redirect("/")

    alltodo = todo.query.filter_by(sno=sno).first()
    return render_template('update.html', alltodo=alltodo)
    

@app.route('/delete/<int:sno>')
def delete(sno):
    alltodo = todo.query.filter_by(sno=sno).first()
    db.session.delete(alltodo)
    db.session.commit()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
