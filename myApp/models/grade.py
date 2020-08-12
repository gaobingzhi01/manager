from myApp.exts import db
from myApp.models.dbHelp import DBHelp


class Grade(db.Model, DBHelp):
    __tablename__ = "grades"

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(20))
    boyNum = db.Column(db.Integer)
    girlNum = db.Column(db.Integer)
    isDelete = db.Column(db.Boolean,default=False)
    def __init__(self,name,boyNum,girlNum):
        self.name = name
        self.boyNum = boyNum
        self.girlNum = girlNum