from flask import Flask, jsonify, request
from flask_cors import CORS
from src.PullData import(
    pullMedianIncome, pullHealthRank, pullGiniCoeffient, pullDeath_Birth, pullInfo
)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.route("/get-info", methods=["post"])
def get_info():
    data = request.json

    if 'calculationType' not in data:
        return jsonify({'Error': "No caclulation provided"})
    
    infoOutput = pullInfo(data['calculationType'])

    if not infoOutput:
        return jsonify({'Error': 'Could not find provided calculation'})
    
    return jsonify(infoOutput)

@app.route("/get-deaths-births", methods=["POST"])
def get_deaths_births():
    data = request.json
    
    if 'region' not in data:
        return jsonify({'Error': 'No region provided'})
    
    deathsBirths_status, deathsBirths_output = pullDeath_Birth(data['region'])
    
    if not deathsBirths_status:
        return jsonify({'Error': deathsBirths_output})
    
    return jsonify(deathsBirths_output)

@app.route("/get-median-income", methods=["POST"]) # AI slop
def get_median_income():
    data = request.json
    
    if 'region' not in data:
        return jsonify({'Error': 'No region provided'})
    
    medianIncome_status, medianIncome_output = pullMedianIncome(data['region'])
    
    if not medianIncome_status:
        return jsonify({'Error': medianIncome_output})

    return jsonify(medianIncome_output)

@app.route("/get-health-rank", methods=["POST"]) # AI slop
def get_health_rank():
    data = request.json
    
    if 'region' not in data:
        return jsonify({'Error': 'No region provided'})
    
    healthRankStatus, healthRankOutcome = pullHealthRank(data['region'])
    
    if not healthRankStatus:
        return jsonify({'Error': healthRankOutcome})
    
    return jsonify(healthRankOutcome)

@app.route("/get-gini-coeffient", methods=["POST"]) # AI slop
def get_gini_coeffient():
    data = request.json
    
    if 'region' not in data:
        return jsonify({'Error': 'No region provided'})
    
    giniCoeffient_status, giniCoeffient_output = pullGiniCoeffient(data['region'])
    
    if not giniCoeffient_status:
        return jsonify({'Error': giniCoeffient_output})

    return jsonify(giniCoeffient_output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)