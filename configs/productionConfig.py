from configs.defaultConfig import DefaultConfig


class ProductionConfig(DefaultConfig):
    DEBUG = False
    TESTING = False