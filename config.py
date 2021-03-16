import os
class Config:
    '''
    General configuration parent class
    '''

    SOURCE_API_BASE_URL ='https://newsapi.org/v2/sources?category={}&apiKey={}'                  
    ARTICLE_API_NEWS_URL ='https://newsapi.org/v2/everything?sources={}&apiKey=c0ad7cfd16f849a9b0d5a6d213b3eac7'
    NEWS_API_KEY = 'c0ad7cfd16f849a9b0d5a6d213b3eac7'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    



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
'production':ProdConfig
}