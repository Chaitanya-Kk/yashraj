import os
import sys
from flask import Flask, render_template, request, jsonify
from modules.bmi_calculator import calculate_bmi
from modules.recommendations import get_recommendation

# Ensure the modules directory is recognized
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/recommend", methods=["POST"])
def api_recommend():
    try:
        data = request.get_json()
        if not all(k in data for k in ["weight", "height", "age", "gender"]):
            return jsonify({"error": "Missing required fields"}), 400
        
        bmi = calculate_bmi(data["weight"], data["height"])
        details = get_recommendation(bmi, data["age"], data["gender"])
        return jsonify({"bmi": bmi, "recommendations": details})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
