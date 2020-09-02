from flask import Flask ,request,jsonify , Blueprint ,session ,current_app
from api.utils.responses import response_with 
import api.utils.responses as resp 
from api.models.movies import Movie , MovieSchema ,movie_schema , movies_schema  
from api.utils.database import db   
from flask_jwt_extended import jwt_required
from flask_limiter import Limiter 
from flask_limiter.util import get_remote_address
from flask_cors import cross_origin

limiter = Limiter(
    current_app ,
    key_func=get_remote_address,
    # default_limits=["200 per day", "50 per hour"]
    )

movie_routes = Blueprint("movie_routes", __name__)


# @movie_routes.route('/',methods=['POST'])

# def create_movie():
#     # try :
#     data = request.get_json()
#     #print(data))
#     #print(movie_schema.load(data))
#     result = movie_schema.load(data)  
#     db.session.add(result)
#     db.session.commit()    
#     return response_with(resp.SUCCESS_201, value={"movie": result})
#     # except Exception as e:
#     #     print (e)
#     #     return response_with(resp.INVALID_INPUT_422)

# @movie_routes.route('/',methods=['POST'])
# def create_movie():

#     try :

#         data = request.get_json()
#         if data['movie_name']:
#             existing_movie = Movie.query.filter_by(movie_name  = movie_name ).first_or_404()
#             if existing_movie is not None:
#                 response = {
#                   'message': 'user already exists'
#                     }
#             return response_with(resp.SUCCESS_201 , response)
#             new_user = Movie(movie_name = data['movie_name'],
#                         movie_director = data['movie_director'],
#                         movie_url = data['movie_url'])       
                
#             db.session.add(my_movies)
#             db.session.commit()
#             response = {
#                   'message': 'user already exists'
#                     }
#             return movie_schema.jsonify(resp.SUCCESS_201,response)

#     except Exception as e:
#         print (e)
#         return response_with(resp.INVALID_INPUT_422)

# @movie_routes.route('/',methods=['POST'])
# def create_movie():
#     try:
#         movie_name = request.json['movie_name']
#         movie_director= request.json['movie_director']
#         movie_url= request.json['movie_url']

#         result = Movie(movie_name,movie_director,movie_url)

#         db.session.add(result)
#         db.session.commit()      

#         result = movie_schema.jsonify(result)  

#         return result

#     except Exception as e:
#          print (e)
#          return response_with(resp.INVALID_INPUT_422)


    
@movie_routes.route('/',methods=['GET'])

# @jwt_required
# @limiter.limit("3 per day")
def get_movies_all():
    fetched = Movie.query.all()     
    movie  = movies_schema.dump(fetched)
    # return response_with(resp.SUCCESS_201,{"movie":movie})
    return jsonify(movie)

@movie_routes.route('/<int:movie_id>',methods=['GET'])

def get_movies_details(movie_id):
    fetched = Movie.query.get_or_404(movie_id)
    movie  = movie_schema.dump(fetched)
    return response_with(resp.SUCCESS_201,{"movie":movie})
     


@movie_routes.route('/',methods=['POST'])
@jwt_required
def create_movie():    
    try:    
        json_data = request.get_json()        
        movie = movie_schema.load(json_data)
        result = movie_schema.dump(movie.create())  
        return response_with(resp.SUCCESS_201, value={"movie": result})
    except Exception as e:
        print (e)
        return response_with(resp.INVALID_INPUT_422)

@movie_routes.route('/<int:movie_id>',methods=['PUT'])
@jwt_required
def update_movie(movie_id):
    try :
        data = request.get_json()
        get_movie = Movie.query.get_or_404(movie_id)
        get_movie.movie_name = data['movie_name']
        get_movie.movie_director = data['movie_director']
        get_movie.movie_url = data['movie_url']
        get_movie.movie_url = data['movie_image']
        db.session.add(get_movie)
        db.session.commit()
        result = movie_schema.dump(get_movie)
        return response_with(resp.SUCCESS_201, value={"movie": result})
    except Exception as e:
        print (e)
        return response_with(resp.INVALID_INPUT_422)


@movie_routes.route('/<int:movie_id>',methods=['PATCH'])
@jwt_required
def update_movie_by_patch(movie_id):
    try :
        data = request.get_json()
        get_movie = Movie.query.get_or_404(movie_id)
        if data.get('movie_name'):
            get_movie.movie_name = data['movie_name']
        if data.get('movie_director') :
            get_movie.movie_director = data['movie_director']
        if data.get('movie_url'):
            get_movie.movie_url = data['movie_url']
        if data.get('movie_image'):
            get_movie.movie_image = data['movie_image']
        db.session.add(get_movie)
        db.session.commit()
        result = movie_schema.dump(get_movie)
        return response_with(resp.SUCCESS_201, value={"movie": result})
    except Exception as e:
        print (e)
        return response_with(resp.INVALID_INPUT_422)
    

@movie_routes.route('/<int:movie_id>', methods=['DELETE'])
@jwt_required
def delete_movie(movie_id):
    get_movie = Movie.query.get_or_404(movie_id)
    db.session.delete(get_movie)
    db.session.commit()
    return response_with(resp.SUCCESS_204)

 