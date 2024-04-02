from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Define models
class User(BaseModel):
    username: str
    email: str

class Post(BaseModel):
    title: str
    content: str
    author: str
    comments: List[str] = []

# Simulated database
db_users = {}
db_posts = {}

# Endpoint to create a new user
@app.post("/users/", response_model=User)
async def create_user(user: User):
    if user.username in db_users:
        raise HTTPException(status_code=400, detail="Username already registered")
    db_users[user.username] = user
    return user

# Endpoint to retrieve all users
@app.get("/users/", response_model=List[User])
async def read_users():
    return list(db_users.values())

# Endpoint to create a new post
@app.post("/posts/", response_model=Post)
async def create_post(post: Post, current_user: User = Depends()):
    if post.author != current_user.username:
        raise HTTPException(status_code=403, detail="User is not authorized to create this post")
    db_posts[post.title] = post
    return post

# Endpoint to retrieve all posts
@app.get("/posts/", response_model=List[Post])
async def read_posts():
    return list(db_posts.values())

# Endpoint to retrieve a specific post
@app.get("/posts/{title}", response_model=Post)
async def read_post(title: str):
    if title not in db_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_posts[title]

# Endpoint to add a comment to a post
@app.post("/posts/{title}/comments/", response_model=Post)
async def add_comment(title: str, comment: str, current_user: User = Depends()):
    if title not in db_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    if title in db_posts and current_user.username not in db_posts[title].author:
        raise HTTPException(status_code=403, detail="User is not authorized to comment on this post")
    db_posts[title].comments.append(comment)
    return db_posts[title]
