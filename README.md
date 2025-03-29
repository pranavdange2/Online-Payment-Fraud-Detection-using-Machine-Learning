# Online Payment Fraud Detection System

A web-based application that uses machine learning to detect fraudulent online payment transactions in real-time.

## Features

- Real-time fraud detection for online payments
- Support for multiple transaction types (Transfer, Cash Out, Debit, Payment)
- Modern, responsive UI built with TailwindCSS
- RESTful API endpoints for prediction
- Interactive feedback with SweetAlert2 notifications

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML, TailwindCSS, JavaScript
- **Machine Learning**: 
  - NumPy
  - Pandas
  - Scikit-learn
  - XGBoost
  - Joblib (for model serialization)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd R Project
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

3. Fill in the transaction details in the form:
   - Transaction Type (Transfer, Cash Out, Debit, Payment)
   - Amount
   - Step (Hour of transaction)
   - Old Balance
   - New Balance
   - Destination Old Balance
   - Destination New Balance

4. Submit the form to get the fraud prediction result

## API Endpoints

### POST /predict
Endpoint for fraud detection predictions

**Request Body:**
```json
{
    "type": "TRANSFER",
    "amount": 1000,
    "step": 1,
    "oldbalanceOrg": 1000,
    "newbalanceOrig": 0,
    "oldbalanceDest": 0,
    "newbalanceDest": 1000
}
```

**Response:**
```json
{
    "success": true,
    "fraud_probability": 0.15,
    "is_fraud": false
}
```

## Development

The application runs in debug mode by default, which enables:
- Auto-reload on code changes
- Detailed error messages
- Interactive debugger

## Security Notes

- This is a development server and should not be used in production
- For production deployment, use a proper WSGI server (e.g., Gunicorn)
- Implement proper input validation and rate limiting for production use

## License

[MIT License](LICENSE)
