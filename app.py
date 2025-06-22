from fastapi import FastAPI, Request, Response
import requests
from fastapi.responses import StreamingResponse

app = FastAPI()

# Target m3u8 URL
TARGET_M3U8_URL = "https://azonew.newkso.ru/azo/nevena1/mono.m3u8"

# Headers to bypass 403
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://top2.newkso.ru"
}

@app.get("/")
def root():
    return {"status": "proxy online"}

@app.get("/stream.m3u8")
def stream():
    r = requests.get(TARGET_M3U8_URL, headers=HEADERS)
    return Response(content=r.content, media_type="application/vnd.apple.mpegurl")

@app.get("/segment")
def segment(url: str):
    r = requests.get(url, headers=HEADERS, stream=True)
    return StreamingResponse(r.iter_content(chunk_size=1024), media_type=r.headers.get("Content-Type", "video/mp2t"))
