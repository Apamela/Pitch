from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class Pitch:
    '''
    Pitch class to define Pitch Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))
    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)
    def __repr__(self):
        return f'User {self.username}'
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    uses = db.relationship('User',backref='role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'
class Pitch(db.Model):

    __tablename__ = 'pitch'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    image_path = db.Column(db.String)
    description=db.column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))        
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

class Upvote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id")) 
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))  
    upvote=db.column(db.Integer)

    def save_upvote(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvote(cls,id):
        upvote=Upvote.query.filter_by(user=current_user,pitch_id=id)
        upvote_pitch.save_upvote()
    @classmethod
    def get_upvote(cls,id):
        upvote=Upvote.query.filter_by(pitch_id=id).all()
        return upvotes
    def __repr__(self):
        return self.user.username
