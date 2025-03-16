class IRepository:
    def __init__(self) -> None:
        pass

    def get_all_links(self):
        pass

    def get_link(self, url: str) -> str:
        pass

    def save_link(self, short_code: str, original_url: str) -> None:
        pass

    def verify_link(self, short_code: str):
        pass