import calendar, datetime
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_cors import CORS
from forum import create_forum, get_reservedList
import time

app=Flask(__name__,  template_folder='Templates')

myCalendar = calendar.TextCalendar(calendar.SUNDAY)
months={1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December'}


@app.route('/', methods=['GET','POST'])
def index():
    # initial
    yy = datetime.datetime.now().year
    mm = datetime.datetime.now().month
    dates=list(myCalendar.itermonthdates(yy,mm))
    return render_template('index.html',dates=dates, mm=mm,months=months, yy=yy)


@app.route('/new_calendar/<int:mm>/<int:yy>', methods=['GET','POST'])
def new_calendar(mm, yy):
    dates=list(myCalendar.itermonthdates(yy,mm))
    return render_template('index.html',dates=dates, mm=mm,months=months, yy=yy)


@app.route('/nextMonth/<int:mm>/<int:yy>', methods={'GET','POST'})
def next(mm, yy):
    new_mm = mm + 1
    new_yy = yy
    if new_mm > 12:
        new_yy = yy + 1
        new_mm = 1
    return redirect (url_for('new_calendar', mm=new_mm, yy=new_yy))


@app.route('/prevMonth/<int:mm>/<int:yy>', methods={'GET','POST'})
def previous(mm, yy):
    new_mm = mm - 1
    new_yy = yy
    if new_mm <= 0:
        new_yy = yy - 1
        new_mm = 12
    return redirect (url_for('new_calendar', mm=new_mm, yy=new_yy))


@app.route('/postForum',methods=['GET','POST'])
def forum():
    if request.method=='GET':
        pass

    if request.method=='POST':
        
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        phonenum=request.form.get('phonenum')
        email=request.form .get('email')
        dd=request.form.get('dd')
        create_forum(fname,lname,phonenum,email,dd)
        
    return redirect (url_for('index'))


@app.route('/forum',methods=['GET','POST'])
def gotoforum():
    if request.method=='GET':
        pass
    if request.method=='POST':
        dd=request.form.get('dd')
    reserved_list = get_reservedList(dd)
    return render_template('forum.html', dd=dd, reserved_list=reserved_list)


if __name__=='__main__':
    app.run(debug=True)