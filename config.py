import os


class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	MONGO_URI = os.environ.get('MONGO_URL') or 'mongodb://localhost:27017/tradesdb'

