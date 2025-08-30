from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api/prices', methods=['GET'])
def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'ids': 'bitcoin,ethereum,binancecoin',  # Add more coins as needed
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': False
    }
    response = requests.get(url, params=params)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

