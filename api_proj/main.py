import os ,logging ,sys
from flask import Flask , jsonify 
from api.utils.database import db
from api.utils.responses import response_with
import api.utils.responses as resp  
from api.routes.movies import movie_routes
from api.routes.users import user_routes
from api.config.config import DevelopmentConfig
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from api.routes.movies import limiter
from flask_cors import CORS, cross_origin
import flask_monitoringdashboard as dashboard


app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string' # user missed in code example book


if os.environ.get('WORK_ENV') == "PROD":
    app_config = ProductionConfig

elif os.environ.get('WORK_ENV') == "TEST":
    app_config = TestConfig

else :
    app_config = DevelopmentConfig


app.config.from_object(app_config)

jwt = JWTManager(app)
CORS(app,headers='Content-Type')
# limiter = Limiter(app,
# key_func=get_remote_address,
#     default_limits=["200 per day", "50 per hour"])
limiter.init_app(app)
dashboard.bind(app)
db.init_app(app)
with app.app_context():
    db.create_all()

#logging.basicConfig(stream=sys.stdout,format='%(asctime)s|%(levelname)|%(filename)s:%(lineno)s|%(message)', level=logging.DEBUG)


app.register_blueprint(movie_routes, url_prefix='/api/movies/')
app.register_blueprint(user_routes,url_prefix='/api/users')

 
@app.after_request
def add_header(response):
    return response
@app.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return response_with(resp.BAD_REQUEST_400)
@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_500)
@app.errorhandler(404)
def not_found(e):
    logging.error(e)
    return response_with(resp. SERVER_ERROR_404)



if __name__ == '--main__':
    app.run(host = "0.0.0.0" ,  port = 5000 , use_reload = False)