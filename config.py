import os
from _private_.telegram_key import CFG_TELEGRAM_KEY

class Config:
    TELEGRAM_KEY = CFG_TELEGRAM_KEY
    LOCAL_PATH = '/root/tele_tec_bot'
    HOST = "0.0.0.0"
    PORT     = "443"
    DEBUG = True
    CERT     = f'/{LOCAL_PATH}/bundle.crt' 
    CERT_KEY = f'/{LOCAL_PATH}/certificate.key' 
    CONTEXT = (CERT, CERT_KEY)
    URL = f'https://api.telegram.org/bot{TELEGRAM_KEY}/'
    WH_URL = 'https://eva-bot.ru/'
 
class LocalConfig(Config):
    PORT = 5000
    CONTEXT = None
    WH_URL = "https://127.0.0.1:5000/"


cfg = Config 

print("ENV", os.getenv('ENV'))

if os.getenv('ENV')=='Local':
    cfg = LocalConfig    
