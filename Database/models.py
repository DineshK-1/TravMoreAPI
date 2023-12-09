from .sql import Base
from sqlalchemy import DATE, TIMESTAMP, Column, Integer, String, ForeignKey, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Ratings(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    placeID = Column(String(200), nullable=False)
    RatingScore = Column(Integer, nullable=False)
    UserID = Column(String(100), nullable=False)

class Reviews(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, autoincrement=True)
    placeID = Column(String(200), nullable=False)
    OverallRating = Column(Integer, nullable=False)
    AmbienceRating = Column(Integer, nullable=False)
    ParkingRating = Column(Integer, nullable=False)
    TreatmentRating = Column(Integer, nullable=False)
    UserID = Column(String(100), nullable=False)
    ReviewText = Column(String(300), nullable=False)