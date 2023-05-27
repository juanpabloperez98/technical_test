from sqlalchemy import create_engine, MetaData
from os import getenv
from dotenv import load_dotenv
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(dir_path, '..', '.env')
load_dotenv(env_path)

user = getenv("USER_DB")
password = getenv("PASSWORD_DB")
db = getenv("DB")
engine = create_engine(f"mysql+pymysql://{user}:{password}@localhost:3306/{db}")
meta_data = MetaData()