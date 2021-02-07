import calendar, datetime
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_cors import CORS
from forum import create_forum, get_reservedList


# c=calendar.TextCalendar(calendar.SUNDAY)
# str=c.formatmonth(2021,1)
# print(str)


app=Flask(__name__)

myCalendar = calendar.TextCalendar(calendar.SUNDAY)
yy = datetime.datetime.now().year
mm = datetime.datetime.now().month
dates=list(myCalendar.itermonthdates(yy,mm))
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
    return render_template('index.html',dates=dates, mm=mm,months=months, yy=yy)

@app.route('/nextMonth', methods={'GET','POST'})
def next():
    global mm, yy, dates
    mm = mm + 1
    if mm > 12:
        yy = yy + 1
        mm = 1
    dates = list(myCalendar.itermonthdates(yy,mm))
    return redirect (url_for('index'))

@app.route('/previousMonth', methods={'GET','POST'})
def previous():
    global mm, yy, dates
    mm = mm - 1
    if mm <= 0:
        yy = yy - 1
        mm = 12
    dates = list(myCalendar.itermonthdates(yy,mm))
    return redirect (url_for('index'))

@app.route('/postForum',methods=['GET','POST'])
def forum():
    if request.method=='GET':
        pass

    if request.method=='POST':
        
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        phonenum=request.form.get('phonenum')
        email=request.form .get('email')
        #date=request.form.get('dates')
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