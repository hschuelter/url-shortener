from Repository.IRepository import IRepository

from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class RepositoryPsql(IRepository):
    data = {}
    settings = {}
    engine = {}
    db = {}

    def __init__(self, settings) -> None:
        self.settings = settings
        self.engine = create_engine(settings.database_psql)

        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        Base = declarative_base()
        self.db = SessionLocal()
        return

    def get_all_links(self):
        return self.data

    def get_link(self, short_code: str) -> str:
        connection = self.engine.connect()
        sql = text(f'''
                SELECT long_url 
                FROM links l 
                WHERE l.short_code = '{short_code}' 
                LIMIT 1''')
        result = connection.execute(sql).fetchall()

        for row in result:
            r = row._mapping
            return r['long_url']
        return 'https://encurta-ai.vercel.app/'

    def save_link(self, short_code: str, original_url: str) -> str:
        key = self.verify_long_url(original_url)
        if key != '':
            return key
        
        
        connection = self.engine.connect()
        sql = text(f'''
                INSERT INTO links (short_code, long_url)
                VALUES ('{short_code}', '{original_url}') ''')
        connection.execute(sql)
        connection.commit()
        
        self.data[short_code] = original_url
        return short_code
    
    def verify_link(self, short_code: str):
        connection = self.engine.connect()
        sql = text(f'''
                SELECT * 
                FROM links l 
                WHERE l.short_code = '{short_code}' 
                LIMIT 1''')
        result = connection.execute(sql).fetchall()

        for _ in result:
            return True
 
        return False
    
    def verify_long_url(self, original_url: str) -> str:
        connection = self.engine.connect()
        sql = text(f'''
                SELECT short_code 
                FROM links l 
                WHERE l.long_url = '{original_url}' 
                LIMIT 1''')
        result = connection.execute(sql).fetchall()
        for row in result:
            r = row._mapping
            return r['short_code']

        return ''
        