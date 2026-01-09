from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os;
from dotenv import load_dotenv
load_dotenv()
env=os.getenv(".env")
base=declarative_base()

db_url = os.getenv("DB_URL")
if db_url is None:
    raise ValueError("DB_URL is not set in the environment variables")
print(db_url)

eng=create_engine(db_url)
Session=sessionmaker(
    autoflush=False,
    bind=eng
)
def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close()