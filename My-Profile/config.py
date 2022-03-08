class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:2020@localhost/profile'
    SECRET_KEY = 'Flask WTF Secret Key'
    UPLOADED_PHOTOS_DEST ='app/static/photos'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
    
config_options = {
    'development':DevConfig,
    'production' : ProdConfig
}
