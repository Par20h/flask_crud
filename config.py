class Config:
    DB_USER = 'root'
    DB_PASSWORD = '1234'
    DB_SERVER = 'localhost'
    DB_DATABASE = 'student_registration'

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True