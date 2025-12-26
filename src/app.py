from flask import Flask, jsonify, request
from flask_cors import CORS
from PullData import pullMedianIncome

app = Flask(__name__)
CORS(
    app,
    resources={r"/*": {"origins": "http://localhost:5173"}},
    supports_credentials=True,
    methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"]
)

@app.route("/get-median-income", methods=["POST"]) # AI slop
def get_median_income():
    data = request.json
    
    if 'region' not in data:
        return jsonify({'Error': 'No region provided'})
    
    medianIncome_status, medianIncome_output = pullMedianIncome(data['region'])
    
    if not medianIncome_status:
        return jsonify({'Error': medianIncome_output})

    return jsonify(medianIncome_output)

if __name__ == "__main__":
    app.run(debug=True)