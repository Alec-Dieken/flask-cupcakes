from flask_cupcakes import db, app

class Cupcake(db.Model):
    '''cupcakes table'''

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, default='https://tinyurl.com/demo-cupcake')

    def serialize(self):
        return {'id': self.id, 'flavor': self.flavor, 'size': self.size,
                'rating': self.rating, 'image': self.image}