# main.py
from fastapi import FastAPI
from face_swap_utils import swap_faces_from_urls
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/swap")
def swap_faces(source_url: str, target_url: str):
    image_bytes = swap_faces_from_urls(source_url, target_url)
    return StreamingResponse(image_bytes, media_type="image/jpeg")
