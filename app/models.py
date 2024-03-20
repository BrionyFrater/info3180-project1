from . import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(400))
    num_rooms = db.Column(db.Integer)
    num_baths = db.Column(db.Integer)
    price = db.Column(db.String(40))
    property_type = db.Column(db.String(10))
    location = db.Column(db.String(150))
    image_name = db.Column(db.String(200))

    def __init__(self, title, description, num_rooms, num_baths, price, property_type, location, image_name):
        self.title = title
        self.description = description
        self.num_rooms = num_rooms
        self.num_baths = num_baths
        self.price = price
        self.property_type = property_type
        self.location = location
        self.image_name = image_name
    
    def __repr__(self):
        return f'Property {self.title}'