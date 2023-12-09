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

class ForumQueries(Base):
    __tablename__ = "forumqueries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(String(100), nullable=False)
    QueryTitle = Column(String(50), nullable=False)
    QueryText = Column(String(300), nullable=False)
    QueryDate = Column(DATE, nullable=False, server_default=func.now())
    QueryTime = Column(TIMESTAMP(timezone=True), onupdate=func.now())

class ForumReplies(Base):
    __tablename__ = "forumreplies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    QueryID = Column(Integer, ForeignKey('forumqueries.id'), nullable=False)
    ReplyText = Column(String(300), nullable=False)
    ReplyDate = Column(DATE, nullable=False, server_default=func.now())
    ReplyTime = Column(TIMESTAMP(timezone=True), onupdate=func.now())