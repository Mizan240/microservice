from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/shipping/calculate', methods=['POST'])
def calculate_shipping():
    data = request.get_json()
    weight = data.get('weight')
    destination = data.get('destination')
    # Simulate shipping cost calculation
    shipping_cost = 10 + (weight * 2)
    return jsonify({'shipping_cost': shipping_cost})

@app.route('/shipping/status/<string:tracking_number>', methods=['GET'])
def track_shipment(tracking_number):
    # Simulate tracking information
    return jsonify({'tracking_number': tracking_number, 'status': 'In Transit'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)
