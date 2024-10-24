from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship

class Feed(Base):
    __tablename__ = 'feed_action'

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    action = Column(String())
    time = Column(TIMESTAMP)

    user = relationship("User", back_populates="feeds")
    post = relationship("Post", back_populates="feeds")

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    feeds = relationship("Feed", back_populates="user")

    gender = Column(Integer)
    age = Column(Integer)
    country = Column(String)
    city = Column(String)
    exp_group = Column(Integer)
    os = Column(String)
    source = Column(String)

class Post(Base):
    __tablename__ = 'post'
    
    id = Column(Integer, primary_key=True)
    feeds = relationship("Feed", back_populates="post")

    text = Column(String)
    topic = Column(String)
