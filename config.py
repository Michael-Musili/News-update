import os

class Config:

    SOURCES_API_BASE_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    ARTICLES_API_BASE_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = 'f4c86580284a4e12bd792c731cfe34c4'
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
