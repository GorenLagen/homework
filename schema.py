from pydantic import BaseModel, Field
from datetime import datetime

class FeedGet(BaseModel):
	user_id: int
	post_id: int
	action: str
	time: datetime

	class Config:
		orm_mode = True

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