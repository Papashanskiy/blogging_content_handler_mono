import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '')
    INSTAGRAM_CLIENT_ID = os.getenv('INSTAGRAM_CLIENT_ID', '')
    INSTAGRAM_CLIENT_SECRET = os.getenv('INSTAGRAM_CLIENT_SECRET', '')
    
    def __init__(self) -> None:
        self.debug = False      
    
    
config = Config()
    