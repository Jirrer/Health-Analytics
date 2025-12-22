from flask import Flask, jsonify
from src.PullData import pullMedianIncome

app = Flask(__name__)

@app.get("/get-median-income")
def get_median_income():
    medianIncome_status, medianIncome_output = pullMedianIncome()
    
    if not medianIncome_status:
        return jsonify({'Error': medianIncome_output})

    return jsonify(medianIncome_output)


if __name__ == "__main__":
    app.run(debug=True)