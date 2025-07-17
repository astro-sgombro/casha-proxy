
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ZENROWS_API_KEY = "c4dff8b5ac9b52f74551eb7e073b1f4078693e88"
ZENROWS_BASE_URL = "https://realestate.api.zenrows.com/v1/targets/idealista/properties/"

@app.route("/api/idealista", methods=["GET"])
def proxy_idealista():
    property_id = request.args.get("propertyId")
    if not property_id:
        return jsonify({"error": "Missing propertyId parameter"}), 400

    target_url = f"{ZENROWS_BASE_URL}{property_id}"
    params = {"apikey": ZENROWS_API_KEY}

    try:
        res = requests.get(target_url, params=params, timeout=15)
        res.raise_for_status()
        return jsonify(res.json())
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "✅ DomusCheck proxy is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
