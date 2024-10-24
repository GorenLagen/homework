from pydantic import BaseModel, Field 
from typing import Optional 
from datetime import datetime


class GetUsers(BaseModel):
	id: int
	gender: int
	age: int
	city: str
	country: str
	os: str
	source: str
	exp_group: int

	class Config:
		orm_mode = True

class GetPosts(BaseModel):
	id: int
	text: str
	topic: str

	class Config:
		orm_mode = True

class FeedGet(BaseModel):
	user_id: int
	post_id: int
	action: str
	time: datetime

	user: Optional[GetUsers] = None
	post: Optional[GetPosts] = None

	class Config:
		orm_mode = True