from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(1000))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch = db.Column(db.Integer,db.ForeignKey("pitches.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch):
        comments = Comment.query.filter_by(pitch_id=pitch).all()
        return comments

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_title = db.Column(db.String)
    pitch_content = db.Column(db.String(1000))
    category = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)

    comments = db.relationship('Comment',backref =  'pitch_id',lazy = "dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,category):
        pitches = Pitch.query.filter_by(category=category).all()
        return pitches

    @classmethod
    def get_pitch(cls,id):
        pitch = Pitch.query.filter_by(id=id).first()

        return pitch

    @classmethod
    def count_pitches(cls,uname):
        user = User.query.filter_by(username=uname).first()
        pitches = Pitch.query.filter_by(user_id=user.id).all()

        pitches_count = 0
        for pitch in pitches:
            pitches_count += 1

        return pitches_count
