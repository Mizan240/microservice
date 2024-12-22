from flask import Flask, jsonify, request

app = Flask(__name__)

orders = {}

@app.route('/sales', methods=['POST'])
def create_order():
    data = request.get_json()
    order_id = data.get('id')
    orders[order_id] = data
    return jsonify({'message': 'Order created'}), 201

@app.route('/sales/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    return jsonify(order)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
