#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    
    bakeries = [bakery.to_dict() for bakery in Bakery.query.all()]
    #! make_response useful for if you want to set actual headers
    return bakeries, 200

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.get(id)
    return bakery.to_dict()

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods = []
    
    for baked_good in BakedGood.query.order_by(BakedGood.price.desc()).all():
        baked_goods.append(baked_good.to_dict())
    
    return baked_goods

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    
    baked_good = BakedGood.query.order_by(BakedGood.price.desc()).first()
    return (baked_good.to_dict())

if __name__ == '__main__':
    app.run(port=5555, debug=True)
