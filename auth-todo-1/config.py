class Config(object):
	Debug = True

class ProductionConfig(Config):
	Debug = False

class DevelopmentConfig(Config):
	Debug = True

app_config = {
	'development' : DevelopmentConfig,
	'production' : ProductionConfig
}