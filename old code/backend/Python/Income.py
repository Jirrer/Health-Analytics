from flask import Flask, request, jsonify
import os
import csv

Income = Flask(__name__)

def get_data(input):
    county_data = {}
    file_name = f"./BackEnd/Data/CountyData/{input}.csv"

    if os.path.isfile(file_name):
        with open(file_name) as county_file:
            county = csv.reader(county_file)
            for row in county:
                county_data[row[0]] = line_chart_format(int(row[1]))
        return county_data
    else:
        return {"error": "File not found"}

def line_chart_format(value):
    if 10000 < value < 200000:
        return (value / 1000) + 50
    elif value <= 50000:
        return (value / 100) / 2
    elif value >= 200000:
        return (value / 2000) + 150
    else:
        return None  # Handle errors accordingly

@Income.route('/data', methods=['GET'])
def data():
    county_name = request.args.get('county')
    if not county_name:
        return jsonify({"error": "No county specified"}), 400
    result = get_data(county_name)
    return jsonify(result)

if __name__ == '__main__':
    Income.run(debug=True)
