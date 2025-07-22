from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'orders.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    train = db.Column(db.String(50))
    station = db.Column(db.String(50))

    def __repr__(self):
        return f'<Order {self.train} at {self.station}>'

# Create DB tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "RailEats API with DB"

@app.route('/order', methods=['POST'])
def order():
    data = request.get_json()
    train = data.get('train')
    station = data.get('station')

    new_order = Order(train=train, station=station)
    db.session.add(new_order)
    db.session.commit()

    return jsonify({
        "message": f"Order saved: Train {train} at {station}"
    })

if __name__ == '__main__':
    app.run(debug=True)
