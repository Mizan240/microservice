from flask import Flask, jsonify, request

app = Flask(__name__)

products = {}

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product_id = data.get('id')
    products[product_id] = data
    return jsonify({'message': 'Product created'}), 201

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify(product)

@app.route('/products', methods=['GET'])
def get_all_products():
    return jsonify(list(products.values()))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
