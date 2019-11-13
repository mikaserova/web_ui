from flask import render_template, request
import  flask_task.form_data as form_data
from flask_task.starter import Starter
from flask_task.hello import app
pol1=3
pred1=5
sc="* * * * *"
print("VIEWS ARE RUNNING")
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/settings', methods=["POST","GET"])   
def settings():
    
    if request.form.get('f2'):
        global sc
        sc=""
        t=request.form.get("minute")
        if t is None: t="*"
        sc+=t+" "
        t=request.form.get("hour")
        if t is None: t="*"
        sc+=t+" "
        t=request.form.get("day")
        if t is None: t="*"
        sc+=t+" "
        t=request.form.get("month")
        if t is None: t="*"
        sc+=t+" "
        t=request.form.get("day_week")
        if t is None: t="*"
        sc+=t
        if sc!="* * * * *":
            Starter.start_scrapper(sc)
    else:
        global pred1,pol1
        pred1 = request.form.get("n1")
        pol1 = request.form.get("n2")
    if pred1 is None: pred1=5
    
    if pol1 is None: pol1=3
 
    #print("GLOBALS ",pol1,pred1)
    
    return render_template("settings.html",pred=int(pred1), pol=int(pol1), schedule=sc)

@app.route('/statistics')   
def statistics():
    global pred1, pol1
    print("GLOBALS1 ",pol1,pred1)
    d=form_data.form_data(pred1, pol1)
    return render_template("statistics.html", res=d)