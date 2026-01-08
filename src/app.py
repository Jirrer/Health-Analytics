from flask import Flask, jsonify, request
from flask_cors import CORS
from src.PullData import pullMedianIncome, pullHealthRank, pullGiniCoeffient

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

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