import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)


PROJECT_NAME = "ProCharrity bot"

PASSWORD_POLICY = {
    "min_length": 8,
    "uppercase": 1,
    "max_length": 32,

}


class Config:
    # Flask Settings:
    DEBUG = True
    SITE_NAME = 'Test_site'
    SECRET_KEY = 'ASDfasdQW4)(83099498&$^%2ewf'

    # Token settings
    JWT_ACCESS_TOKEN_EXPIRES = 18000  # 30 minutes
    JWT_REFRESH_TOKEN_EXPIRES = 18000  # 30 minutes
    JWT_SECRET_KEY = 'Ad3ewrf#$wqA24&2W24-0)*&)@43'

    # DataBase settings:
    SQL_ALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')
