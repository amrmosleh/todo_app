from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# importing the necessary libarires, compnents, etc, to make the code run
# - flask
# -SQLALchemy

'''
__authors__ = ['Amr Mohamad - amrmosleh]
__date__ = 2022026
__description__ = "TO-DO application for CICD"

'''

app = Flask(__name__)
#  it refers to a class

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class Todo(db.Model):
    """A dummy docstring."""
    id = db.Column(db.Integer, primary_key=True)
    # creating a variable "id". In this variable I eant to  initiate my database. Specifically, I want to initailize a column of my table /database. the function db.column() takes agrmants or parameters. more to read on https//fflask-sqlalchemy.paletprojects/com/en/2.x/.api


    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route("/")
def list1():
    """A dummy docstring."""
    todo_list = Todo.query.all()
    return render_template("list.html", todo_list=todo_list)


@app.route("/edit")
def home():
    """A dummy docstring."""
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    """A dummy docstring."""
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    """A dummy docstring."""
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    """A dummy docstring."""
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))



if "__name__ == __main__":
    db.create_all()
    app.run()












