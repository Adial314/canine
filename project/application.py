# APPLICATION
#   A. Seaborn
#   Dec 29 2020


import json
import flask
from flask import request, jsonify, render_template, send_from_directory
from flask_api import status

from lib.query_ncbi import query_ncbi
from lib.conversion.seqrecord_to_dict import *


# Instantiate the app
app = flask.Flask(__name__);


@app.route('/')
def Home():
    return render_template('home.html')


@app.route('/api')
def api():
    
    # Parse API arguments
    if "version" in request.args:
        version = request.args['version']
    else:
        return "API version not specified", status.HTTP_400_BAD_REQUEST

    if "user" in request.args:
        user = request.args['user']
    else:
        return "User not specified", status.HTTP_400_BAD_REQUEST

    if "resource" in request.args:
        resource = request.args['resource']
    else:
        return "Target resource not specified", status.HTTP_400_BAD_REQUEST

    if "database" in request.args:
        database = request.args['database']
    else:
        return "Target database not specified", status.HTTP_400_BAD_REQUEST

    if "term" in request.args:
        term = request.args['term']
    else:
        return "Search term not specified", status.HTTP_400_BAD_REQUEST

    if "format" in request.args:
        format = request.args['format']
    else:
        return "File format not specified", status.HTTP_400_BAD_REQUEST
    
    # Pass on request to resource
    if version == "0.0.0":
        if resource == "ncbi" or resource == "NCBI":
            result = query_ncbi(user, database, term, format)
        else:
            return f"Resource '{resource}' not recognized", status.HTTP_400_BAD_REQUEST
    else:
        return f"Version '{version}' not recognized", status.HTTP_400_BAD_REQUEST
    
    # Process records
    records = list()
    for record in result['records']:
        records.append(seqrecord_to_dict(record))
    
    # Append status code
    response = dict()
    response['status'] = 200
    response['count'] = result['count']
    response['records'] = records
    
    # Return response
    return jsonify(response)


# ------------------------- MAIN ------------------------- #
# localhost:5050/api?version=0.0.0&user=skynet@world.domination&resource=ncbi&database=nucleotide&term=CRT[Gene Name] AND "Plasmodium falciparum"[Organism]&format=gb

if __name__ == '__main__':
    app.run(debug=True, port=5050)
