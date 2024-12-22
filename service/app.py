from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

PRODUCT_SERVICE = 'http://product-service:5001'
SALES_SERVICE = 'http://sales-service:5002'
PAYMENT_SERVICE = 'http://payment-service:5003'
SHIPPING_SERVICE = 'http://shipping-service:5004'
AUTH_SERVICE = 'http://auth-service:5005'
INVENTORY_SERVICE = 'http://inventory-service:5006'

@app.route('/products', methods=['GET'])
def get_products():
    response = requests.get(f"{PRODUCT_SERVICE}/products")
    return jsonify(response.json())

@app.route('/sales', methods=['POST'])
def create_order():
    data = request.get_json()
    response = requests.post(f"{SALES_SERVICE}/sales", json=data)
    return jsonify(response.json())

@app.route('/payments', methods=['POST'])
def create_payment():
    data = request.get_json()
    response = requests.post(f"{PAYMENT_SERVICE}/payments", json=data)
    return jsonify(response.json())

@app.route('/shipping/calculate', methods=['POST'])
def calculate_shipping():
    data = request.get_json()
    response = requests.post(f"{SHIPPING_SERVICE}/shipping/calculate", json=data)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
