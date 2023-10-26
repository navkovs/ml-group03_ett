#!/usr/bin/env python
"""
This will be the main class for the project. It will contain the very basic
parts of the programm that will call other source files and help keep the
organisation of the project more feasible.
"""

import numpy
import sys
import requests
import ett_predictor

from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


def addOne(toAdd):
    """
    Quick demonstration that passing the variable from httpd Server to Flask Server works.
    The toAdd gets castet to int and one gets added.

    :param toAdd: Gets cast to int and one added.
    :type toAdd: int or string
    :return: The number plus one.
    :rtype: int
    """
    return float(toAdd) + 1


@app.route('/getdata/<float:lat>/<float:lon>/<float:length>/<float:breadth>/<int:route>', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def data_get(lat, lon, length, breadth, route):
    """
    Await data from httpd server to call this site with the parameters
    lat, lon and speed. They have to be in float notation and as path vars.

    :return: HTTP Message and Status Code
    :rtype: Tuple (String, Int)
    """
    if request.method == 'GET':
        ########################
        # Do Something with Vars
        ########################

        # ett = 1

        # lat = addOne(lat)
        # lon = addOne(lon)
        # length = addOne(length)
        # breadth = addOne(breadth)

        # print('Latitude:', lat, '\nLongitude:',
        #       lon, '\nLength:', length, '\nBreadth:', breadth)

        ett = ett_predictor.ett_predictor(lat, lon, length, breadth, route)

        #############################
        # Stop doing things with Vars
        #############################

        # Return to Frontend. Should only be a tuple.
        # Return value should be the ETT.
        # Old return:
        # return 'Latitude: {} Longitude: {} Speed: {}'.format(lat, lon, speed), 200
        return 'ETT: {}'.format(ett), 200


if __name__ == '__main__':
    """
    Call the flask app to wait for input.
    This is by all means a server that just waits in the background
    until someone calls /getdata/ with parameters which then tiggers data_get.
    """
    app.run(host='0.0.0.0', threaded=True, debug=True)
