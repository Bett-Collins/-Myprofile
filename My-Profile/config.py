class Config:
    '''
    General configuration parent class
    '''
    pass
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:2020@localhost/profile'



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
