from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import flask.ext.restless
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'dawefihaw09efha0wihefaw'
db = SQLAlchemy(app)

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    completed = db.Column(db.Boolean)
    task = db.Column(db.String(200))
    username = db.Column(db.String(100))

manager.create_api(Task, methods=['GET', 'POST', 'DELETE'])

admin = Admin(app)
admin.add_view(ModelView(Task, db.session))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()