from hub import db

class Physics(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    topics = db.Column(db.String(length=40), nullable=False)
    details = db.Column(db.String(length=1024), nullable=False)
    route = db.Column(db.String(length=20), nullable=False)

    def __repr__(self) -> str:
        return f'Physics {self.topics}'

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)