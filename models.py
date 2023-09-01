from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    active = db.Column(db.Boolean, default=True)
    
    portfolios = db.relationship('Portfolio', backref='user', lazy=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "active": self.active
        }
        
    def serialize_with_portfolio(self):
        return {
            "id": self.id,
            "username": self.username,
            "active": self.active,
            "portfolios": self.get_portfolios()
        }
        
    def get_portfolios(self):
        return [portfolio.serialize() for portfolio in self.portfolios]
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
        
class Portfolio(db.Model):
    __tablename__ = 'portfolios'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False, unique=True)
    active = db.Column(db.Boolean, default=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    photos = db.relationship('Photo', backref="portfolio")
    
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "active": self.active,
            "users_id": self.users_id
        }
        
    def serialize_with_photos(self):
        return {
            "id": self.id,
            "title": self.title,
            "active": self.active,
            "user": self.user.username,
            "photos": self.get_photos()
        }
        
    def get_photos(self):
        return [photo.serialize() for photo in self.photos]
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
        
class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), nullable=False)
    media = db.Column(db.String(20), default="image")
    active = db.Column(db.Boolean, default=True)
    portfolios_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "filename": self.filename,
            "portfolios_id": self.portfolios_id,
            "active": self.active
        }
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()