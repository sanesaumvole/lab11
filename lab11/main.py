from fastapi import FastAPI, Request
from routers import version, posts, stats

app = FastAPI()

app.include_router(version.router, prefix="/version", tags=["version"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(stats.router, prefix="/stats", tags=["stats"])

request_count = {
    "GET": {"version": 0, "posts": 0},
    "POST": {"posts": 0},
    "PUT": {"posts": 0},
    "DELETE": {"posts": 0}
}

@app.middleware("http")
async def count_requests(request: Request, call_next):
    response = await call_next(request)
    endpoint = request.url.path.split('/')[1]
    method = request.method
    if endpoint in request_count.get(method, {}):
        request_count[method][endpoint] += 1
    return response

@app.get("/stats/")
async def get_stats():
    return request_count
