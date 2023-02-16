from fastapi import APIRouter, Depends
from fullstack_challenge_api.utils.db import get_db
from sqlalchemy.orm import Session
import sqlalchemy
from sqlalchemy import create_engine
import config
# from databases import Database

router = APIRouter()
DATABASE_URL = "mysql+mysqldb://root:PASSWORD@localhosthost/app"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = Session(autocommit=False, autoflush=False, bind=engine)
# database = Database(DATABASE_URL)
Base = declarative_base()
Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Company(Base):
    __tablename__ = "challenge_companies"

    key = Column(Integer, primary_key=True, index=True)
    properties_name = Column(String)
    properties_country = Column(String)
    properties_founding_date = Column(Date)
    properties_description = Column(String)
    properties_company_id = Column(Integer)

@router.get("/companies")
async def get_companies(db: Session = Depends(get_db)):
      query = db.query(Company).all()
      return query



