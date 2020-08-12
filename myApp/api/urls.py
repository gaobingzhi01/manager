from flask import Blueprint, render_template

from myApp.models import Grade, Student

urls = Blueprint("myApp","urls",template_folder="templates")


# create your urls and views here
@urls.route('/grades/')
def gradesList():
    # 获取所有班级对象
    grades = Grade.query.all()
    # print(grades)
    # return "班级列表"
    return render_template("gradesList.html",grades=grades)


@urls.route('/students/')
def studentsList():
    stus = Student.query.all()
    # print(stus)
    # return "学生列表"
    return render_template("studentsList.html", stus=stus)


# 查看某个 id 值得学生的信息
@urls.route('/detail/<sid>/')
def studentDetail(sid):
    stu = Student.query.get(sid)
    print(stu)
    return "某个 id 值得学生信息"


@urls.route('/')
def hello_world():
    return 'Hello World!'