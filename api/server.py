from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from Repository.RepositoryMock import RepositoryMock
from Services.UrlShortenerService import UrlShortenerService
from Data.URLRequest import URLRequest

app = FastAPI()

origins = [
    "https://encurta-ai.vercel.app",
    "http://localhost:8080",
    "http://localhost:5173"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

link_repository = RepositoryMock()
url_shortener_service = UrlShortenerService(link_repository)


###################################################################################
@app.get("/")
async def root():
    return url_shortener_service.handle_root()

@app.get("/links")
async def get_all_links():
    return url_shortener_service.handle_get_all_links()

@app.get("/{short_code}")
async def redirect_url(short_code: str):
    """
    Redirect to the original URL based on the short code.
    """
    return RedirectResponse(url=url_shortener_service.handle_get_link(short_code), status_code=307)

@app.post('/shorten')
async def shorten(request: URLRequest):
    """
    Shorten a given URL and return the short version.
    """
    short_code = url_shortener_service.handle_shorten_link(request)
    return {"short_url": f"{short_code}"}