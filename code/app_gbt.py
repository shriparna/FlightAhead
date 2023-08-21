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

@app.route("/api/v1.0/flightPredict/<timeofday>/<weekday>/<season>/<airline>/<origin>/<dest>")
def flightPredict(timeofday,weekday,season,airline, origin, dest):
#    date_format = datetime.strptime(date, '%Y-%m-%d')
#     weekday = date_format.weekday()
#     if weekday < 6:
#         weekday = weekday + 1
#     else:
#         weekday = 0

    # month = date_format.month
    # day = date_format.day
    filename='../model/Flights18_gbt_tuned.sav'
    flight_model = pl.load(open(filename,'rb'))

    #print(weekday,month,day)
    CRS_ELAPSED_TIME = 147.0
    DISTANCE = 888.0
    
    sched_dep_time_Morning = 0
    sched_dep_time_Afternoon = 0
    sched_dep_time_Evening = 0
    sched_dep_time_Night = 0
    if timeofday == "Morning":
        sched_dep_time_Morning = 1
    if timeofday == "Afternoon":
        sched_dep_time_Afternoon = 1
    if timeofday == "Evening":
        sched_dep_time_Evening = 1
    if timeofday == "Night":
        sched_dep_time_Night = 1


    sched_arr_time_Morning = 0
    sched_arr_time_Afternoon = 0
    sched_arr_time_Evening = 0
    sched_arr_time_Night = 0
    if timeofday == "Morning":
        sched_arr_time_Morning = 1
    if timeofday == "Afternoon":
        sched_arr_time_Afternoon = 1
    if timeofday == "Evening":
        sched_arr_time_Evening = 1
    if timeofday == "Night":
        sched_arr_time_Night = 1


    WEEKDAY_Friday = 0
    WEEKDAY_Monday = 0
    WEEKDAY_Saturday = 0
    WEEKDAY_Sunday = 0
    WEEKDAY_Thursday = 0
    WEEKDAY_Tuesday = 0
    WEEKDAY_Wednesday = 0
    if weekday == "Friday":
        WEEKDAY_Friday = 1
    if weekday == "Monday":
        WEEKDAY_Monday = 1
    if weekday == "Saturday":
        WEEKDAY_Saturday = 1
    if weekday == "Sunday":
        WEEKDAY_Sunday = 1
    if weekday == "Thursday":
        WEEKDAY_Thursday = 1
    if weekday == "Tuesday":
        WEEKDAY_Tuesday = 1
    if weekday == "Wednesday":
        WEEKDAY_Wednesday = 1

    season_Autumn = 0
    season_Spring = 0
    season_Summer = 0
    season_Winter = 0
    if season == "Autumn":
        season_Autumn = 1
    if season == "Spring":
        season_Spring = 1
    if season == "Summer":
        season_Summer = 1
    if season == "Winter":
        season_Winter = 1

    #Weather forecast
    ORIGIN_PRCP = 0.5
    ORIGIN_SNOW = 0
    ORIGIN_SNWD = 0
    DEST_PRCP = 0.3
    DEST_SNOW = 4
    DEST_SNWD = 1

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
    
    
    # features_list = [TAXI_OUT, WHEELS_OFF, WHEELS_ON, TAXI_IN, CANCELLED,
    #    DIVERTED, CRS_ELAPSED_TIME, ACTUAL_ELAPSED_TIME, AIR_TIME,
    #     DISTANCE, Month, Day, Weekday, OP_CARRIER_AA, OP_CARRIER_DL,
    #    OP_CARRIER_OO, OP_CARRIER_UA, OP_CARRIER_WN, ORIGIN_ATL,
    #    ORIGIN_CLT, ORIGIN_DEN, ORIGIN_DFW, ORIGIN_ORD, DEST_ATL,
    #    DEST_CLT, DEST_DEN, DEST_DFW, DEST_ORD]
    
    features_list = [[CRS_ELAPSED_TIME,\
    DISTANCE,\
    ORIGIN_PRCP,\
    ORIGIN_SNOW,\
    ORIGIN_SNWD,\
    DEST_PRCP,\
    DEST_SNOW,\
    DEST_SNWD,\
    OP_CARRIER_AA,\
    OP_CARRIER_DL,\
    OP_CARRIER_OO,\
    OP_CARRIER_UA,\
    OP_CARRIER_WN,\
    ORIGIN_ATL,\
    ORIGIN_CLT,\
    ORIGIN_DEN,\
    ORIGIN_DFW,\
    ORIGIN_ORD,\
    DEST_ATL,\
    DEST_CLT,\
    DEST_DEN,\
     DEST_DFW,\
    DEST_ORD,\
    WEEKDAY_Friday,\
    WEEKDAY_Monday,\
    WEEKDAY_Saturday,\
    WEEKDAY_Sunday,\
    WEEKDAY_Thursday,\
    WEEKDAY_Tuesday,\
    WEEKDAY_Wednesday,\
    sched_dep_time_Afternoon,\
    sched_dep_time_Evening,\
    sched_dep_time_Morning,\
    sched_dep_time_Night,\
    sched_arr_time_Afternoon,\
    sched_arr_time_Evening,\
    sched_arr_time_Morning,\
    sched_arr_time_Night,\
    season_Autumn,\
    season_Spring,\
    season_Summer,\
    season_Winter]]

    features_df = pd.DataFrame(features_list)
    print(features_df.shape)
    #Scaling
   # scaler = StandardScaler()
    #feature_scaled = scaler.fit_transform(features_df)
    
    #feature_reshaped = feature_scaled.reshape(1,-1)
    #print(feature_scaled) 
    #features_list = features.reshape(-1,1)
    #print(features)

    delay =  flight_model.predict(features_df)
    delay_probabilities = flight_model.predict_proba(features_df)
    if delay_probabilities[0][0] > 0.65:
        outcome = {'flt_delay': "on time", 'probability': delay_probabilities[0][0]}
    else:
        outcome = {'flt_delay': "delayed", 'probability': delay_probabilities[0][1]}
    # print("Delay:", delay)
    # if delay == 0:
    #      outcome = "Your flight is predicted to be on time"
    # else:
    #      outcome = "Your flight is predicted to be delayed"
    return jsonify(outcome)

@app.route("/FlightDashboard")
def showDashboard():
    outcome = "click the Predict button"
    return render_template('FlightDashboard.html', flt_outcome = outcome)



    
if __name__ == '__main__':
    app.run(debug=True)