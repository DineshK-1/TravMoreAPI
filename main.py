from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import SQLAlchemyError

from Database import models
from Database.sql import engine, SessionLocal

import random

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="TravMore API")

origins = [
    "https://travmore.netlify.app",
    "http://localhost:8000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add_rating")
async def add_rating(rating: str, placeID:str,  db: Session = Depends(get_db)):
    userID = "User #"+str(random.randint(1,1000))
    rating_object = models.Ratings(placeID=placeID, RatingScore=rating, UserID = userID)

    try:
        db.add(rating_object)
        db.commit()
    except SQLAlchemyError as e:
        print("Error creating user:", str(e))
        raise HTTPException(status_code=500, detail="Error creating user")

    return rating_object

@app.get("/get_rating")
async def get_rating(placeID:str,  db: Session = Depends(get_db)):
    rating_objects = db.query(models.Ratings).filter(models.Ratings.placeID == placeID).all()
    review_objects = db.query(models.Reviews).filter(models.Ratings.placeID == placeID).all()
    avgRating = 0

    for i in rating_objects:
        avgRating += i.RatingScore
    for i in review_objects:
        avgRating += i.OverallRating
    
    avgRating /= len(rating_objects) + len(review_objects)

    return {"rating": avgRating}

@app.post("/add_review")
async def add_review(placeID:str, OverallRating:str,ParkingRating:str,AmbienceRating:str,TreatmentRating:str,review_text:str,  db: Session = Depends(get_db)):
    userID = "User #"+str(random.randint(1,1000))
    review_object = models.Reviews(placeID=placeID, OverallRating=OverallRating, ParkingRating=ParkingRating,AmbienceRating=AmbienceRating ,TreatmentRating=TreatmentRating, ReviewText=review_text, UserID = userID)

    try:
        db.add(review_object)
        db.commit()
    except SQLAlchemyError as e:
        print("Error creating user:", str(e))
        raise HTTPException(status_code=500, detail="Error creating user")

    return review_object

@app.get("/get_reviews")
async def get_reviews(placeID:str,  db: Session = Depends(get_db)):
    review_objects = db.query(models.Reviews).filter(models.Ratings.placeID == placeID).all()

    return review_objects

@app.post("/add_forum_query")
async def add_forum_query(query_text:str,  db: Session = Depends(get_db)):
    userID = "User #"+str(random.randint(1,1000))
    forum_query_object = models.ForumQueries(QueryText=query_text, UserID = userID)

    try:
        db.add(forum_query_object)
        db.commit()
    except SQLAlchemyError as e:
        print("Error creating user:", str(e))
        raise HTTPException(status_code=500, detail="Error creating user")

    return forum_query_object

@app.get("/get_forum_queries")
async def get_forum_queries(db: Session = Depends(get_db)):
    forum_query_objects = db.query(models.ForumQueries).all()

    return forum_query_objects

@app.post("/add_forum_reply")
async def add_forum_reply(queryID:str, reply_text:str,  db: Session = Depends(get_db)):
    userID = "User #"+str(random.randint(1,1000))
    forum_reply_object = models.ForumReplies(QueryID=queryID, ReplyText=reply_text, UserID = userID)

    try:
        db.add(forum_reply_object)
        db.commit()
    except SQLAlchemyError as e:
        print("Error creating user:", str(e))
        raise HTTPException(status_code=500, detail="Error creating user")

    return forum_reply_object

@app.get("/get_forum_replies")
async def get_forum_replies(queryID:str, db: Session = Depends(get_db)):
    forum_reply_objects = db.query(models.ForumReplies).filter(models.ForumReplies.QueryID == queryID).all()

    return forum_reply_objects