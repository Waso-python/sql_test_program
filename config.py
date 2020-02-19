import os


basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "waso-the-best"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    KSDB ='localhost:c:/db/ks2.fdb'
    BPDB ='localhost:c:/db/ks2.fdb'
    TDTDB = 'localhost:c:/db/ks2.fdb'