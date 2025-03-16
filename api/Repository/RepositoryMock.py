from Repository.IRepository import IRepository

class RepositoryMock(IRepository):
    data = {
        'a': 'https://www.youtube.com/',
        'b': 'https://music.youtube.com/',
        'c': 'https://itch.io/',
        'd': 'https://drive.google.com/',
        'e': 'https://excalidraw.com/',
        'f': 'https://www.youtube.com/@Cogumelando'
    }

    def __init__(self) -> None:
        pass

    def get_all_links(self):
        return self.data

    def get_link(self, short_code: str) -> str:
        if short_code in self.data:
            return self.data[short_code]
        return 'http://localhost:8000'

    def save_link(self, short_code: str, original_url: str) -> str:
        for key, val in self.data.items():
            if val == original_url:
                return key
        
        self.data[short_code] = original_url
        return short_code
    
    def verify_link(self, short_code: str):
        return short_code in self.data.keys()