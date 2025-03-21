import string
import random

from Repository.IRepository import IRepository
from Data.URLRequest import URLRequest

class UrlShortenerService:
    repository = ''
    settings = {}

    def __init__(self, repository: IRepository, settings) -> None:
        self.repository = repository
        self.settings = settings

    def handle_root(self) -> str:
        return {"message": "healthcheck successful!"}

    def handle_get_all_links(self) -> str:
        return self.repository.get_all_links()

    def handle_get_link(self, short_code: str) -> str:
        return self.repository.get_link(short_code)

    def handle_shorten_link(self, request: URLRequest) -> None:
        short_code = self.generate_short_code()
        print(short_code)
        while self.repository.verify_link(short_code):
            short_code = self.generate_short_code()
        
        short_code = self.repository.save_link(short_code, request.url)
        return short_code
    

    def generate_short_code(self, length: int = 6) -> str:
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=length))