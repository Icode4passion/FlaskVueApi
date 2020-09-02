


import os
basedir = os.path.abspath(os.path.dirname(__file__))
db_file_prod = 'sqlite:///'+os.path.join(basedir,'database_prod.db')
db_file_test = 'sqlite:///'+os.path.join(basedir,'database_test.db')
db_file_dev = 'sqlite:///'+os.path.join(basedir,'database_dev.db')




class Config(object):
    DEBUG=False
    TESTING=False
    SQLALCHEMY_TRACK_MODIFICATION = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = db_file_prod    
    

class TestConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI = db_file_test
    SQLALCHEMY_ECHO = False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = db_file_dev
    SQLALCHEMY_ECHO = False
