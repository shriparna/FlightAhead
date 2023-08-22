# FlightAhead
Project 4: FlightAhead

# Project 4 : Group 4. Flight Ahead

### Details of the Project 
###### Name: Flight Ahead
###### Submission Date: 8/21/2023
###### Presentation Date: 8/21/2023

### Team
###### [Vidya Gadave](https://github.com/VidyaGadave), [Shridhar Kamat](https://github.com/shriparna), [Ajay Gopalkrishna](https://github.com/ajoyg), [Brandon Reed](https://github.com/B-the-Reed), [Raymond Darrough](https://github.com/raymonddarrough), [Alejandro Gutierrez](https://github.com/alejfxguti), [JP Fortunato](https://github.com/joaopedrofortunato)
<hr>

## Project Specification:
#### Tech Stack
- ML Models: Gradient Boosted Trees, Neural Net Model, Logistic Regression, Random Forest Classifier, Random Forest Regressor, Decision Trees, Keras Tuner
- API: Python Flask
- Front-end: HTML, CSS, JavaScript
- Visuals: Tableau

#### Package Contents:
- [Code](https://github.com/shriparna/FlightAhead/tree/main/code) - Directory to store all the code
   - [FlightAheadShridhar.ipynb](https://github.com/shriparna/FlightAhead/blob/main/code/FlightAheadShridhar.ipynb) - Spark Google Collab notebook for Logistic Regression and Random Forest Classifier models
   - [FlightAhead_RF_Vidya.ipynb](https://github.com/shriparna/FlightAhead/blob/main/code/FlightAhead_RF_Vidya.ipynb) - Jupyter notebook for Random Forest Regressor model
   - [FlightDataPCAAjay.ipynb](https://github.com/shriparna/FlightAhead/blob/main/code/FlightDataPCAAjay.ipynb) - Jupyter notebook for Neural Network model with PCA
   - [FlightDataPrepAjay.ipynb](https://github.com/shriparna/FlightAhead/blob/main/code/FlightDataPrepAjay.ipynb) - Jupyter notebook for Neural Network model combiled with weather data
   - [Flights_JP_3D_ok.ipynb](https://github.com/shriparna/FlightAhead/blob/main/code/Flights_JP_3D_ok.ipynb) - Jupyter notebook for Keras Tuner for Canceled, Departed and Delayed filght
   - [Flights_JP_Delays.ipynb](https://github.com/shriparna/FlightAhead/blob/main/code/Flights_JP_Delays.ipynb) - Jupyter notebook for Keras Tuner for Delays
   - [Flights_JP_Diversions.ipynb](https://github.com/shriparna/FlightAhead/blob/main/code/Flights_JP_Diversions.ipynb) - Jupyter notebook for Keras Tuner for Diversions
   - [REV3_FlightData_preprocessing_delays.ipynb](https://github.com/shriparna/FlightAhead/blob/main/code/REV3_FlightData_preprocessing_delays.ipynb) - Jupyter Notebook for cleaning and pre-processing and scaling the data for reusability
   - [REV3_gbt_tuning_brandon.ipynb](https://github.com/shriparna/FlightAhead/blob/main/code/REV3_gbt_tuning_brandon.ipynb) - Jupyter Notebook for the Gradient Boosted Trees model with weather data
   - [app.py](https://github.com/shriparna/FlightAhead/blob/main/code/app.py) - Python file to define different API routes using Flask for the Random Forest Classifier model
   - [app_gbt.py](https://github.com/shriparna/FlightAhead/blob/main/code/app_gbt.py) - Python file to define different API routes using Flask for the Gradient Boosted Trees model
   - [flightahead_prep_AG.ipynb](https://github.com/shriparna/FlightAhead/blob/main/code/flightahead_prep_AG.ipynb) - Jupyter Notebook for the Decision Trees Model
   - [static](https://github.com/shriparna/FlightAhead/tree/main/code/static) - This folder contains the css stylesheet and JavaScript code
        - [css](https://github.com/shriparna/FlightAhead/tree/main/code/static/css) - Directory to store stylesheet files
            - [style.css](https://github.com/shriparna/FlightAhead/blob/main/code/static/css/style.css) - Main Stylesheet file 
        - [js](https://github.com/shriparna/FlightAhead/tree/main/code/static/js) -  Directory to store the JavaScript files
            - [maplogic.js](https://github.com/shriparna/FlightAhead/blob/main/code/static/js/maplogic.js) - Main JavaScript file to predict the GBT model and render the visual
   - [templates](https://github.com/shriparna/FlightAhead/tree/main/code/templates) - Directory to store the html files
        - [FlightDashboard.html](https://github.com/shriparna/FlightAhead/blob/main/code/templates/FlightDashboard.html) - Main html file to display the dashboard
- [Data_files](https://github.com/shriparna/FlightAhead/tree/main/Data_files) - Direcotry to store all data files
    - [Master Data Flights_2018.csv](https://github.com/shriparna/FlightAhead/blob/main/Data_files/Master%20Data%20Flights_2018.csv) - 2018 filght data merged with origin and destination latitude and longitude
    - [REV3_2018_cleaned_delays.csv](https://github.com/shriparna/FlightAhead/blob/main/Data_files/REV3_2018_cleaned_delays.csv) - 2018 flight data for top 5 airline and origin and destination cleaned and scaled
    - [Weather_data_top_5_stations.csv](https://github.com/shriparna/FlightAhead/blob/main/Data_files/Weather_data_top_5_stations.csv) - Weather data for origin and destination airports
    - [2018.csv](https://www.kaggle.com/datasets/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018?select=2018.csv) The data file is of 1GB+ size so giving here the Kaggle link from where we used the data
- [model](https://github.com/shriparna/FlightAhead/tree/main/model) - Directory to store ML models
    - [Flights18.sav](https://github.com/shriparna/FlightAhead/blob/main/model/Flights18.sav) Random Forest Classifier model pickle file
    - [Flights18_gbt_tuned.sav](https://github.com/shriparna/FlightAhead/blob/main/model/Flights18_gbt_tuned.sav) Gradient Boosted Trees model pickle file
    - Note: Flights18_RFC.sav file could not be uploaded as the size of the file was above 500MB
- [presentation](https://github.com/shriparna/FlightAhead/tree/main/presentation) - Directory to store presentation
    - [FlightAhead_ Predicting Flight Delays _ Project 04, Group 04.pptx](https://docs.google.com/presentation/d/1y7MM_9d3cm2tdMSaE-rkktSqniE2or8BjQnFMtFlTuI/edit?pli=1#slide=id.g275a37de113_0_344) Group Presentation Slides

<hr>

## Visuals (Tableau):

1. [Project4 (Flight Ahead) - Average Arrival and Departure Delays](https://public.tableau.com/app/profile/shridhar.kamat6308/viz/Project4FlightAhead-AverageArrivalandDepartureDelays/AvgDelay?publish=yes)
![Screenshot 2023-08-21 at 3 56 54 PM](https://github.com/shriparna/FlightAhead/assets/71340748/911a0c9e-a02c-416c-b2be-4c49a8ea5f7b)


2. [2018 Top 5 Busiest Airport Flight Delays Analysis](https://public.tableau.com/app/profile/alejandro.gutierrez4671/viz/2018Top5BusiestAirportFlightDelaysAnalysis/2018Top5BusiestAirportsFlightDelayAnalysis?publish=yes)
![Screenshot 2023-08-21 at 4 04 16 PM](https://github.com/shriparna/FlightAhead/assets/71340748/e69d726e-a5ad-4cae-8d48-cf9ced70269e)

<hr>

## Instructions:
- Our Dashboard is deployed on the route http://127.0.0.1:5000
- Use drop downs to select Origin, Destination, Airline, Day of the Week, Time of the Day and, Season 
- Click the Predict button to check the probalibility of the flight being delay or on-time
- The plot shows the routes with average arrival and departure delays from the top 5 origin to different destinations for the top 5 airlines
<hr>
