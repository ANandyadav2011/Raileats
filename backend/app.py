from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to RailEats Backend API"

@app.route('/order', methods=['POST'])
def order():
    data = request.get_json()
    train = data.get('train')
    station = data.get('station')
    return jsonify({
        "message": f"Food order request received for Train {train} at {station}"
    })

if __name__ == '__main__':
    app.run(debug=True)
