from _private_.telegram_key import CFG_TELEGRAM_KEY
CFG_LOCAL = False
CFG_LOCAL_PATH = '/root/tele_tec_bot'
PORT     = "443"
CERT     = f'/{CFG_LOCAL_PATH}/bundle.crt' 
CERT_KEY = f'/{CFG_LOCAL_PATH}/certificate.key' 
CONTEXT = (CERT, CERT_KEY)
URL = f'https://api.telegram.org/bot{CFG_TELEGRAM_KEY}/'
WH_URL = 'https://eva-bot.ru/'