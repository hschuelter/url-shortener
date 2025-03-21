from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings, SettingsConfigDict


import config
from Repository.RepositoryMock import RepositoryMock
from Repository.RepositoryPsql import RepositoryPsql
from Services.UrlShortenerService import UrlShortenerService
from Data.URLRequest import URLRequest

app = FastAPI()
settings = config.Settings()

origins = [
    settings.frontend_url,
    settings.alternate_url1,
    settings.alternate_url2

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

link_repository = RepositoryPsql(settings)
url_shortener_service = UrlShortenerService(link_repository, settings)


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