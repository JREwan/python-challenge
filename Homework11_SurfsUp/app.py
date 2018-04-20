# Climate App
# Now that you have completed your initial analysis, design a Flask api based on the queries that you have just developed.
#  - Use FLASK to create your routes.
#################################################
# Import Flask & jsonify & the kitchen sink...
#################################################
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save reference to the tables
Station = Base.classes.station
Measurement = Base.classes.measurement
# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        "<h1>HW 11 Surf Is Up!<h1/>"
        "<br/>"
        "<h2>Available APIs<h2/>"
        "<li><a href ='/api/v1.0/precipitation'>Precipitation</a></li>"
        "<li><a href ='/api/v1.0/stations'>Stations</a></li>"
        "<li><a href ='/api/v1.0/tobs'>Temps observed</a></li>"
        "<li><a href = '/api/v1.0/start_end'>Calculated Temps</a></li>"
    )

#################################################
# /api/v1.0/precipitation
#################################################
@app.route("/api/v1.0/precipitation")
def precipitation():
    yearago_date = dt.date(2016, 8 , 22)
    # select(station, date, prcp) frome measurement
    # where date >= yearago_date
    prcp_in_last_year = session.query(Measurement.date, func.sum(Measurement.prcp)).\
        filter(Measurement.date > yearago_date).group_by(Measurement.date).all()
    
    prcp_list = [prcp_in_last_year]

    return jsonify(prcp_list)

#################################################
# /api/v1.0/stations
#################################################
@app.route("/api/v1.0/stations")
def stations():
    all_stations = session.query(Station.name, Station.station, Station.elevation).all()
    
    station_list = []
    for a_station in all_stations:
        row = {}
        row['elevation'] = a_station[2]
        row['station'] = a_station[1]
        row['name'] = a_station[0]
        station_list.append(row)
    return jsonify(station_list)
    
#################################################
# /api/v1.0/tobs
#   - Return a json list of Temperature Observations (tobs) for the previous year
#################################################
@app.route("/api/v1.0/tobs")
def temp_obs():
    yearago_date = dt.date(2016, 8 , 22)
    temps = session.query(Station.name, Measurement.date, Measurement.tobs).\
    filter(Measurement.date > yearago_date).all()
        
    tobs_list = []
    for temp in temps:
        t = {}
        t["Station"] = temp[0]
        t["Date"] = temp[1]
        t["Temperature"] = int(temp[2])
        tobs_list.append(t)
    return jsonify(tobs_list)

#################################################
#
# - /api/v1.0/<start> and /api/v1.0/<start>/<end>
#   - Return a json list of the minimum temperature, the average temperature, and the max temperature 
#      for a given start or start-end range.
#   - When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal 
#      to the start date.
#   - When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the 
#      start and end date inclusive.
#
# Hints
# - You will need to join the station and measurement tables for some of the analysis queries.
# - Use Flask jsonify to convert your api data into a valid json response object.
#################################################
@app.route("/api/v1.0/start_end")
def calc_temps():
    sy = 2017 # start year
    sm = 7    # start month
    sd = 1    # start day
    ey = 2017 # end year
    em = 7    # end month
    ed = 11   # end day
    # Convert dates to "year - 1" dates
    start_date = dt.date(sy, sm, sd)
    end_date = dt.date(ey, em, ed)

    temp_info = session.query(Measurement.tobs).filter(Measurement.date >= start_date, Measurement.date <= end_date).all()
    temperatures = [temperature[0] for temperature in temp_info]
    # Get the minimum temp
    temp_min = min(temperatures)
    # Get the maximum temp
    temp_max = max(temperatures)
    # Get the average temp
    temp_avg = np.mean(temperatures)
    date_results = 'Start date:  ' + str(start_date) + '</br>' + 'End date:  ' + str(end_date) + '</br>' 
    minmax_results = 'Min temp: ' + str(temp_min) + '</br>' + 'Avg temp: ' + str(temp_avg) +'</br>' + 'Max temp: ' + str(temp_max)
    temp_results = date_results + minmax_results 
    return(temp_results)   
    

#################################################
# Define Main behavior
#################################################
if __name__ == '__main__':
    app.run(debug=True)
