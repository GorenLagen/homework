import fastapi
from typing import List
from database import SessionLocal
from schema import GetPosts, GetUsers, FeedGet
from tableUser import User, Post, Feed
from sqlalchemy.orm import Session

app = fastapi.FastAPI()

def get_db():
	with SessionLocal() as db:
		return db

@app.get("/users/{user_id}", response_model=List[GetUsers])
def get_user(user_id: int, Session: Session = fastapi.Depends(get_db)):
	res = Session.query(User).filter(User.id == user_id).limit(10).all()
	return res 

@app.get("/posts/{post_id}", response_model=List[GetPosts])
def get_post(post_id: int, Session: Session = fastapi.Depends(get_db)):
	res = Session.query(Post).filter(Post.id == post_id).limit(10).all()
	return res 

@app.get('/users/{user_id}/feed', response_model=List[GetUsers])
def get_user_feed(user_id: int, limit: int = 10, Session: Session = fastapi.Depends(get_db)):
    res = Session.query(User).filter(User.id == id).order_by(User.time.desc()).limit(limit).all()
    return res

@app.get('/post/{post_id}/feed', response_model=List[GetPosts])
def get_post_feed(post_id: int, limit: int = 10, Session: Session = fastapi.Depends(get_db)):
    res = Session.query(Post).filter(Post.id == id).order_by(Post.time.desc()).limit(limit).all()
    return res

@app.get('/post/recommend/{user_id}', response_model=List[GetPosts])
def get_post_recommend(user_id: int, limit: int = 10, Session: Session = fastapi.Depends(get_db)):
	res = Session.query(Post).limit(limit).all()
	return res