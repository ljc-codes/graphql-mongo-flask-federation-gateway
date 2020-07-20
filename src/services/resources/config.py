class BaseConfig:
    TESTING = False
    DEBUG = False

    MONGO_USER = '******'
    MONGO_PWD = '*****'

    MONGO_HOST = '*******'


class DevConfig(BaseConfig):
    DEBUG = True