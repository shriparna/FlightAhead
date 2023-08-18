# Import the dependencies.

import numpy as np
import pandas as pd
import pickle as pl
from datetime import datetime
from sklearn.preprocessing import StandardScaler

from flask import Flask, jsonify, render_template

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
@app.route('/')
def welcome():
    """List all available api routes."""
    return(f"Available Routes")

@app.route("/api/v1.0/flightPredict/<date>/<airline>/<origin>/<dest>")
def flightPredict(date, airline, origin, dest):
    date_format = datetime.strptime(date, '%Y-%m-%d')
    weekday = date_format.weekday()
    if weekday < 6:
        weekday = weekday + 1
    else:
        weekday = 0

    month = date_format.month
    day = date_format.day
    filename='../model/Flights18.sav'
    flight_model = pl.load(open(filename,'rb'))

    #print(weekday,month,day)
    TAXI_OUT = 12.0
    WHEELS_OFF = 921.0
    WHEELS_ON = 1216.0
    TAXI_IN = 19.0
    CANCELLED = 0.0
    DIVERTED = 0.0
    CRS_ELAPSED_TIME = 147.0
    ACTUAL_ELAPSED_TIME = 146.0
    AIR_TIME = 115.0
    DISTANCE = 888.0
    Month = month
    Day = day
    Weekday = weekday
    OP_CARRIER_AA = 0
    OP_CARRIER_DL = 0
    OP_CARRIER_OO = 0
    OP_CARRIER_UA = 0
    OP_CARRIER_WN = 0
    if airline == "AA":
        OP_CARRIER_AA = 1
    if airline == 'UA':
        OP_CARRIER_UA =1
    if airline == 'WN':
        OP_CARRIER_WN=1
    if airline == 'OO':
        OP_CARRIER_OO=1
    if airline == 'DL':
        OP_CARRIER_DL =1
    
    ORIGIN_ATL =0
    ORIGIN_CLT = 0
    ORIGIN_DEN = 0
    ORIGIN_DFW = 0 
    ORIGIN_ORD = 0
    if origin == 'ATL':
        ORIGIN_ATL =1
    if origin == 'CLT':
        ORIGIN_CLT = 1
    if origin == 'DEN':
        ORIGIN_DEN = 1
    if origin == 'DFW':
        ORIGIN_DFW = 1
    if origin == 'ORD':
        ORIGIN_ORD = 1
    
    DEST_ATL =0
    DEST_CLT = 0
    DEST_DEN = 0
    DEST_DFW = 0 
    DEST_ORD = 0
    if dest == 'ATL':
        DEST_ATL =1
    if dest == 'CLT':
        DEST_CLT = 1
    if dest == 'DEN':
        DEST_DEN = 1
    if dest == 'DFW':
        DEST_DFW = 1
    if dest == 'ORD':
        DEST_ORD = 1
    
    
    features_list = [TAXI_OUT, WHEELS_OFF, WHEELS_ON, TAXI_IN, CANCELLED,
       DIVERTED, CRS_ELAPSED_TIME, ACTUAL_ELAPSED_TIME, AIR_TIME,
       DISTANCE, Month, Day, Weekday, OP_CARRIER_AA, OP_CARRIER_DL,
       OP_CARRIER_OO, OP_CARRIER_UA, OP_CARRIER_WN, ORIGIN_ATL,
       ORIGIN_CLT, ORIGIN_DEN, ORIGIN_DFW, ORIGIN_ORD, DEST_ATL,
       DEST_CLT, DEST_DEN, DEST_DFW, DEST_ORD]
    
    features_df = pd.DataFrame(features_list)
    #Scaling
    scaler = StandardScaler()
    feature_scaled = scaler.fit_transform(features_df)
    
    feature_reshaped = feature_scaled.reshape(1,-1)
    print(feature_reshaped) 
    #features_list = features.reshape(-1,1)
    #print(features)

    delay =  flight_model.predict(feature_reshaped)[0]
    if delay == 0:
        outcome = "Your flight is predicted to be on time"
    else:
        outcome = "Your flight is predicted to be delayed"
    return outcome




    
if __name__ == '__main__':
    app.run(debug=True)