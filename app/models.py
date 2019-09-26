from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
@login_manager.user_loader
def load_user(user_id):
        return User.query.get (user_id)
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    upvotes = db.relationship('Upvote',backref = 'user',lazy = "dynamic")
    pitches= db.relationship('Pitch',backref = 'user',lazy = "dynamic")
    downvotes= db.relationship('Downvote',backref = 'user',lazy = "dynamic")
   
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

class Pitch(db.Model):

    __tablename__ ='pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    description=db.Column(db.Text)
    category=db.Column(db.String(255),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id")) 
    upvotes = db.relationship('Upvote',backref = 'pitch',lazy = "dynamic")
    downvotes=db.relationship('Downvote',backref = 'pitch',lazy = "dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_pitches(cls,id):
        pitches = Pitches.query.filter_by(pitch_id=id).all()
        return pitches
    def __repr__(self):
        return f'pitch {self.description}'

class Comment(db.Model):
    __tablename__='comments'
    
    id = db.Column(db.Integer,primary_key=True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
    description = db.Column(db.Text)

    
    def __repr__(self):
        return f"Comment : id: {self.id} comment: {self.description}"

class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key = True)
    upvote=db.column(db.Integer)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id")) 
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))  
    
    def save_upvote(self):
        db.session.add(self)
        db.session.commit()

    def add_upvotes(cls,id):
        upvote_pitch = Upvote(user=current_user,pitch_id=id)
        upvote_pitch.save_upvote()

    @classmethod
    def get_upvotes(cls,id):
        upvote=Upvote.query.filter_by(pitch_id=id).all()
        return upvote
    @classmethod
    def get_all_upvote(cls,pitch_id):
        upvotes=Upvote.query.order_by('id').all()
        return upvotes
    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
class Downvote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id")) 
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))  
    downvote=db.column(db.Integer)

    def save_downvote(self):
        db.session.add(self)
        db.session.commit()

    def add_downvote(self):
        downvote_pitch = Downvote(user = current_user, pitch_id=id)
        downvote_pitch.save_downvotes()

    @classmethod
    def get_downvotes(cls,id):
        downvote=Downvote.query.filter_by(user=current_user,pitch_id=id)
        downvote_pitch.save_downvote()
    @classmethod
    def get_all_downvotes(cls,pitch_id):
        downvote=Downvote.query.filter_by(pitch_id=id).all()
        return downvote
    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'