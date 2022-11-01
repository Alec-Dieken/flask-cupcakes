from flask import render_template, jsonify, request
from flask_cupcakes import app, db
from flask_cupcakes.models import Cupcake


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/cupcakes')
def get_cupcakes():

    cc_obj = Cupcake.query.all()
    cupcakes = {'cupcakes': [cupcake.serialize() for cupcake in cc_obj]}

    return jsonify(cupcakes)


@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json.get('image')

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()

    cupcake = new_cupcake.serialize()
    return (jsonify(cupcake), 201)


@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    cc_obj = Cupcake.query.get_or_404(cupcake_id)
    cupcake = {'cupcake': cc_obj.serialize()}

    return jsonify(cupcake)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def edit_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json['flavor']
    cupcake.size = request.json['size']
    cupcake.rating = request.json['rating']
    cupcake.image = request.json['image']

    db.session.commit()
    return jsonify(cupcake.serialize())


@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify({'message': 'Deleted'})
