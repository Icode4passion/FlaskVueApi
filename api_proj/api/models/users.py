from api.utils.database import db 
from passlib.hash import pbkdf2_sha256 as sha256
from marshmallow_sqlalchemy import ModelSchema 
from marshmallow import fields



class User(db.Model):
    uid = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(200),nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()
    
    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)


    @staticmethod 
    def verify_hash(password,hash):
        return sha256.verify(password,hash)


class UserSchema(ModelSchema):
    class Meta:
        model = User 
        sqla_session = db.session


user_schema = UserSchema()
users_schema = UserSchema(many=True)