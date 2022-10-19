from flask import render_template, url_for, flash, redirect, request
from website import app, db
#from website import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.urls import url_parse
from sqlalchemy import desc, asc, text
from website.forms import RegistrationForm, LoginForm #
from website.models import User
import numpy as np # 
import json #
import dateutil.parser #
from datetime import datetime #

@app.route("/")
@app.route("/index")
def index():
    if current_user.is_authenticated:
        flagstotal = find_totalflagstotal()
        return render_template('index.html', title='Home', flagstotal=flagstotal)
    else:  
        return redirect(url_for('login'))

@app.route("/flags")
def flags():
    flagsrt,flagsrtlist = find_totalflags('REPORTED_TEMP')
    flagsot,flagsotlist = find_totalflags('OUTSIDE_TEMP')
    flagsrh,flagsrhlist = find_totalflags('REPORTED_HUMIDITY')
    flagsoh,flagsohlist = find_totalflags('OUTSIDE_HUMIDITY')
    flagsap,flagsaplist = find_totalflags('AIR_PRESSURE')
    flagsop,flagsoplist = find_totalflags('OUTSIDE_AIRPRESSURE')
    return render_template('flags.html', title='Flags', flagsrt=flagsrt, flagsot=flagsot, flagsrh=flagsrh, flagsoh=flagsoh, flagsap=flagsap, flagsop=flagsop, flagsrtlist=flagsrtlist, flagsotlist=flagsotlist, flagsrhlist=flagsrhlist, flagsohlist=flagsohlist, flagsaplist=flagsaplist, flagsoplist=flagsoplist) 

@app.route("/graphs")
def graphs():
    return render_template('graphs.html', title='Graphs')

@app.route("/profile/<username>")
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('profile.html', title='Profile', user=user)

@app.route("/emergencycontacts")
def emergencycontacts():
    return render_template('emergencycontacts.html', title='Emergency Contacts')

@app.route("/settings")
def settings():
    return render_template('settings.html', title='Settings')

def loadJSON(name,key):
    input_file = open(name)
    json_array = json.load(input_file)
    factor = []
    data_time = []
    anomalies = []
    for item in json_array:
        time= item['DATA_ENTRY_TIME']
        time = datetime.fromisoformat(time)
        time = time.strftime('%d-%m-%Y-%H:%M')
        if (item[key]) == "null":
            temp = float("0")
            anomalies.append(time)
        else:
            temp = float(item[key])

        factor.append(temp)
        data_time.append(time)
    return factor,data_time,anomalies

def find_flags(list,avg):
    a = np.array(list)
    threshold = np.percentile(a, 98)
    flags=[]
    for i in a:
        if i > threshold:
            flags.append(i)
    return flags
    
def loadJSONSimple(name,key):
    input_file = open(name)
    json_array = json.load(input_file)
    factor = []
    for item in json_array:
        if (item[key]) == "null":
            temp = float("0")
        else:
            temp = float(item[key])
        factor.append(temp)
    return factor

def find_totalflags(factor):
    json = loadJSONSimple('website/sensor_data/prop_2_kitchen.json',factor)
    average = (sum(json)/len(json))
    flagstotal = len(find_flags(json,average))
    flags = find_flags(json,average)
    return flagstotal, flags

def find_totalflagstotal():

    flagsrt, flags = find_totalflags('REPORTED_TEMP')
    flagsot, flags = find_totalflags('OUTSIDE_TEMP')
    flagsrh, flags = find_totalflags('REPORTED_HUMIDITY')
    flagsoh, flags = find_totalflags('OUTSIDE_HUMIDITY')
    flagsap, flags = find_totalflags('AIR_PRESSURE')
    flagsop, flags = find_totalflags('OUTSIDE_AIRPRESSURE')

    totalflagstotal = flagsrt+flagsot+flagsrh+flagsoh+flagsap+flagsop

    return totalflagstotal


##################    GRAPHS #############################

@app.route('/reported_temp')
def reported_temp():
    reported_temp,data_time,anomalies= loadJSON('website/sensor_data/prop_2_kitchen.json','REPORTED_TEMP')
    maximum = max(reported_temp)
    minimum = min(reported_temp)
    average = (sum(reported_temp)/len(reported_temp))
    flags = find_flags(reported_temp,average)
    rt_flag_count = len(flags)
    return render_template('reported_temp.html',reported_temp=reported_temp,outside_temp=outside_temp,rt_flag_count=rt_flag_count,data_time = data_time,maximum=maximum,average=average,minimum=minimum, anomalies=anomalies,flags=flags)

@app.route('/outside_temp')
def outside_temp():
    outside_temp,data_time,anomalies = loadJSON('website/sensor_data/prop_2_kitchen.json','OUTSIDE_TEMP')
    maximum = max(outside_temp)
    minimum = min(outside_temp)
    average = (sum(outside_temp)/len(outside_temp))
    flags = find_flags(outside_temp,average)
    ot_flag_count = len(flags)
    return render_template('outside_temp.html', outside_temp= outside_temp,data_time=data_time,maximum=maximum,minimum=minimum,average=average, anomalies=anomalies,flags=flags,ot_flag_count=ot_flag_count)

@app.route('/reported_hum')
def reported_hum():
    reported_hum,data_time,anomalies = loadJSON('website/sensor_data/prop_2_kitchen.json','REPORTED_HUMIDITY')
    maximum = max(reported_hum)
    minimum = min(reported_hum)
    average = (sum(reported_hum)/len(reported_hum))
    flags = find_flags(reported_hum,average)
    rh_flag_count = len(flags)
    return render_template('reported_hum.html',reported_hum=reported_hum,data_time=data_time,maximum=maximum,minimum=minimum,average=average,rh_flag_count=rh_flag_count, anomalies=anomalies,flags=flags)

@app.route('/outside_hum')
def outside_hum():
    outside_hum,data_time,anomalies = loadJSON('website/sensor_data/prop_2_kitchen.json','OUTSIDE_HUMIDITY')
    maximum = max(outside_hum)
    minimum = min(outside_hum)
    average = (sum(outside_hum)/len(outside_hum))
    flags = find_flags(outside_hum,average)
    oh_flag_count = len(flags)
    return render_template('outside_hum.html',outside_hum=outside_hum,data_time=data_time,maximum=maximum,minimum=minimum,average=average, oh_flag_count=oh_flag_count,anomalies=anomalies,flags=flags)
 
@app.route('/outside_press')
def outside_press():
    outside_press,data_time,anomalies = loadJSON('website/sensor_data/prop_2_kitchen.json','OUTSIDE_AIRPRESSURE')
    maximum = max(outside_press)
    minimum = min(outside_press)
    average = (sum(outside_press)/len(outside_press))
    flags = find_flags(outside_press,average)
    op_flag_count = len(flags)
    return render_template('outside_press.html',outside_press=outside_press,data_time=data_time,maximum=maximum,minimum=minimum,average=average,op_flag_count=op_flag_count, anomalies=anomalies,flags=flags) 

@app.route('/air')
def air():
    air,data_time,anomalies = loadJSON('website/sensor_data/prop_2_living.json','AIR_PRESSURE')
    maximum = max(air)
    minimum = min(air)
    average = (sum(air)/len(air))
    flags = find_flags(air,average)
    air_flag_count = len(flags)
    return render_template('pressure.html',air=air,data_time=data_time,maximum=maximum,minimum=minimum,average=average,air_flag_count=air_flag_count, anomalies=anomalies,flags=flags)

################## LOGIN/REGISTER #############################

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Incorrect username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, phone=form.phone.data, dob=form.dob.data, ecname=form.ecname.data, ecphone=form.ecphone.data, ecemail=form.ecemail.data, multi=form.multi.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered !')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
