from flask import Flask, jsonify, request

app = Flask(__name__)

inventory = {}

@app.route('/inventory/<int:product_id>', methods=['GET'])
def get_inventory(product_id):
    stock = inventory.get(product_id, 0)
    return jsonify({'product_id': product_id, 'stock': stock})

@app.route('/inventory/<int:product_id>/update', methods=['POST'])
def update_inventory(product_id):
    data = request.get_json()
    stock = data.get('stock')
    inventory[product_id] = stock
    return jsonify({'message': 'Stock updated'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5006)
