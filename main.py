from flask import Flask
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/loan"
db = SQLAlchemy(application)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    NIC = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.NIC


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Guarantee = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)


db.create_all()
db.session.commit()


@application.route("/")
def index():
    return render_template("index.html")


@application.route("/user/add")
def user_add():
    admin = User(NIC='1234')
    db.session.add(admin)
    db.session.commit()
    return "Item add"


if __name__ == '__main__':
    application.run(debug=True)
