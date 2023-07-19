import os
import logging

class Config:    
    API_ID = 28298577
    API_HASH = "143efc9236a955d630ede2642578b251"
    OWNER_ID = "5163706369"
    SESSION = os.environ.get('SESSION')

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
