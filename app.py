from flask import Flask, jsonify
from aadhaar.qr import AadhaarSecureQR

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/aadhaar/<int:qr>')
def get_data(qr):
    secure_qr = AadhaarSecureQR(qr)
    data = secure_qr.extract_data()
    return data

if __name__ == "__main__":
    app.run(debug=True)