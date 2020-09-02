
from api.utils.database import db  
# from flask_marshmallow import Marshmallow ,Schema ,fields 
from marshmallow_sqlalchemy import ModelSchema 
from marshmallow import fields
  


class Movie(db.Model):
    __tablename__ = 'movie'

    movie_id = db.Column(db.Integer,primary_key=True)
    movie_name = db.Column(db.String(30))
    movie_director = db.Column(db.String(30))
    movie_url = db.Column(db.String(100))
    movie_image = db.Column(db.String(500))

    def __init__(self,movie_name,movie_director,movie_url,movie_image):
        self.movie_name = movie_name
        self.movie_director= movie_director
        self.movie_url= movie_url
        self.movie_image= movie_image


    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class MovieSchema(ModelSchema):
    class Meta:
        model = Movie
        sqla_session = db.session
        #fields = ("movie_name","movie_director","movie_url")

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

# class Movie(db.Model):
    


#     movie_id        =           db.Column(db.Integer , primary_key = True)
#     movie_name      =           db.Column(db.String(20))
#     directed_by     =           db.Column(db.String(50))
#     staring         =           db.Column(db.String(200))
#     produced_by     =           db.Column(db.String(50))
#     release_date    =           db.Column(db.String(20))
#     language        =           db.Column(db.String(20))
#     boxoffice_hit   =           db.Column(db.Integer)
#     movie_url       =           db.Column(db.String(100))


#     def __init__(self ,movie_name ,directed_by ,staring,produced_by,release_date,language,boxoffice_hit,movie_url ) :
#         self.movie_name = movie_name,
#         self.directed_by = directed_by,
#         self.staring  = staring, 
#         self.produced_by = produced_by ,
#         self.release_date = release_date,
#         self.language = language,
#         self.boxoffice_hit = boxoffice_hit, 
#         self.movie_url = movie_url


#     def create(self):
#         db.session.add(self)
#         db.session.commit()
#         #return self

# class MovieSchema(Schema):
#     class Meta:
#         # model = Movie
#         #sqla_session = db.session
#         fields = ("movie_name","directed_by", "staring" ,
#                      "produced_by","release_date", "language",
#                      "boxoffice_hit", "movie_url")
# movie_schema = MovieSchema()
# movies_schema = MovieSchema(many=True)

#     # id = fields.Number(dump_only=True)
#     # movie_name = fields.String(required=True)
#     # directed_by = fields.String(required=True)
#     # staring = fields.String(required=True)
#     # produced_by = fields.String(required=True)
#     # release_date = fields.String(required=True)
#     # language = fields.String(required=True)
#     # boxoffice_hit = fields.String(required=True)
#     # movie_url = fields.String(required=True)



    







    