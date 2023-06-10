import pickle
from flask import Flask,request,jsonify,render_template
from flask import Flask
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
application = app

pickle.load(open('/config/workspace/notebook/model/ridge.pkl','rb'))
pickle.load(open('/config/workspace/notebook/model/scaler.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['get','post'])
def predict_datapoint():
    if request.method=='post':
        Temperature=float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        WS = float(request.form.get('WS'))
        Rain = float(request.form.get('Rain'))
        FFMC  = float(request.form.get('FFMC'))
        DMC  = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data_scaled=standred_scaler.transform([[Temperature,RH,ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result = ridge_model.predict(new_data_scaled)

        return render_template('home.html',result=result[0])
    else:
        return render_template('home.html')

        



if __name__=="__main__":
    application.run(host="0.0.0.0")
