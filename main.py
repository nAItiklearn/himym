from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app =FastAPI()

#dummy data
posts: list[dict] = [
    {
        "id":1 ,
        "author": "Naitik",
        "title": "this is the coolest website for himym",
        "content": "so cool",
        "date_created": "july 15 , 2009",
    },
    {
            "id":2 ,
            "author": "shrusti",
            "title": "this is the coolest website for himym",
            "content": "so peak",
            "date_created": "june 30th , 2008",
        },
]

@app.get("/", response_class= HTMLResponse, include_in_schema= False)
##Its lwk good to hide the html responses because they are for human interactions and not for api docs , so we can hide from /docs using inc_in_schema=False
def home():
    return f"<h2>{posts[0]['title']}</h2>"

@app.get("/api/posts")
def get_posts():
    return posts