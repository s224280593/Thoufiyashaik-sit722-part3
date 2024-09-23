from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://thoufiya_sit722_part3_fgz4_user:gO06rHRjQ3R7TTT1iNrIp0txA6OHUXsq@dpg-crom97q3esus73c3g1h0-a.oregon-postgres.render.com/thoufiya_sit722_part3_fgz4" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
