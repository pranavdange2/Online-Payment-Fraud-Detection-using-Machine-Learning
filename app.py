from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Convert values to appropriate types
        amount = float(data['amount'])
        old_balance_orig = float(data['oldbalanceOrg'])
        new_balance_orig = float(data['newbalanceOrig'])
        old_balance_dest = float(data['oldbalanceDest'])
        new_balance_dest = float(data['newbalanceDest'])
        
        # Initialize fraud probability
        fraud_probability = 0.0
        reasons = []
        
        # Rule 1: Check if sender has sufficient balance
        if amount > old_balance_orig:
            fraud_probability += 0.4
            reasons.append("Transaction amount exceeds available balance")
        
        # Rule 2: Check if balances after transaction make sense
        expected_new_balance_orig = old_balance_orig - amount
        expected_new_balance_dest = old_balance_dest + amount
        
        balance_mismatch_orig = abs(expected_new_balance_orig - new_balance_orig)
        balance_mismatch_dest = abs(expected_new_balance_dest - new_balance_dest)
        
        if balance_mismatch_orig > 0.01:  # Allow for small rounding differences
            fraud_probability += 0.3
            reasons.append("Sender's final balance doesn't match the transaction")
            
        if balance_mismatch_dest > 0.01:  # Allow for small rounding differences
            fraud_probability += 0.3
            reasons.append("Receiver's final balance doesn't match the transaction")
        
        # Rule 3: Check for negative balances
        if new_balance_orig < 0 or new_balance_dest < 0:
            fraud_probability += 0.4
            reasons.append("Transaction results in negative balance")
        
        # Rule 4: Check for unusually large amounts (example threshold: 1M)
        if amount > 1000000:
            fraud_probability += 0.2
            reasons.append("Unusually large transaction amount")
        
        # Cap probability at 1.0
        fraud_probability = min(fraud_probability, 1.0)
        
        # Consider it fraud if probability is over 30%
        is_fraud = fraud_probability > 0.3
        
        return jsonify({
            'success': True,
            'fraud_probability': fraud_probability,
            'is_fraud': is_fraud,
            'reasons': reasons if is_fraud else []
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)
