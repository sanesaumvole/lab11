from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Post(BaseModel):
    id: int
    title: str
    content: str

posts_db = {
    1: Post(id=1, title="First Post", content="Content of the first post"),
    2: Post(id=2, title="Second Post", content="Content of the second post")
}

@router.get("/", response_model=List[Post])
async def get_posts():
    return list(posts_db.values())

@router.post("/", response_model=Post)
async def create_post(post: Post):
    if post.id in posts_db:
        raise HTTPException(status_code=400, detail="Post with this ID already exists")
    posts_db[post.id] = post
    return post

@router.put("/{post_id}", response_model=Post)
async def update_post(post_id: int, updated_post: Post):
    if post_id not in posts_db:
        raise HTTPException(status_code=404, detail="Post not found")
    posts_db[post_id] = updated_post
    return updated_post

@router.delete("/{post_id}", response_model=Post)
async def delete_post(post_id: int):
    if post_id not in posts_db:
        raise HTTPException(status_code=404, detail="Post not found")
    return posts_db.pop(post_id)
