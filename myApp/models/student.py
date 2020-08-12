from myApp.exts import db
from myApp.models.dbHelp import DBHelp


class Student(db.Model, DBHelp):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    gender = db.Column(db.Boolean)
    age = db.Column(db.Integer)
    content = db.Column(db.String(40))
    isDelete = db.Column(db.Boolean, default=False)
    grade = db.Column(db.Integer,db.ForeignKey("grades.id"))
    def __init__(self,name,gender,age,content,grade):
        self.name = name
        self.gender = gender
        self.age = age
        self.content = content
        self.grade = grade
    def __str__(self):
        return self.name