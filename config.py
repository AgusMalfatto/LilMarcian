class Config:
    DEBUG = False
    SECRET_KEY='mikey',
    DATABASE_HOST='localhost'
    DATABASE_PASSWORD='password'
    DATABASE_USER='root'
    DATABASE='lilmarcian'


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
