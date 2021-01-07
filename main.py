import calendar
from flask import Flask, flash, redirect, render_template, request

# c=calendar.TextCalendar(calendar.SUNDAY)
# str=c.formatmonth(2021,1)
# print(str)


app=Flask(__name__)

myCalendar = calendar.Calendar()
dates = list(myCalendar.itermonthdates(2021, 1))
print(dates)

@app.route('/')
def index():
    return render_template('index.html',dates=dates)
    

if __name__=='__main__':
    app.run(debug=True)