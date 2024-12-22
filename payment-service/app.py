from flask import Flask, jsonify, request

app = Flask(__name__)

payments = {}

@app.route('/payments', methods=['POST'])
def create_payment():
    data = request.get_json()
    payment_id = data.get('id')
    payments[payment_id] = data
    return jsonify({'message': 'Payment initiated'}), 201

@app.route('/payments/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    payment = payments.get(payment_id)
    if not payment:
        return jsonify({'message': 'Payment not found'}), 404
    return jsonify(payment)

@app.route('/payments/<int:payment_id>/refund', methods=['POST'])
def refund_payment(payment_id):
    payment = payments.get(payment_id)
    if not payment:
        return jsonify({'message': 'Payment not found'}), 404
    payment['status'] = 'Refunded'
    return jsonify({'message': 'Payment refunded'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
