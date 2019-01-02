# CONFIG
CFG_LOCAL = False
CFG_LOCAL_PATH = '/root/teletec-bot'
TELEGRAM_KEY    = ''
 # Same FQDN used when generating SSL Cert
PORT     = "443"
CERT     = f'{CFG_LOCAL_PATH}/bundle.crt' 
CERT_KEY = f'{CFG_LOCAL_PATH}/certificate.key' 
CONTEXT = (CERT, CERT_KEY)
URL = 'https://api.telegram.org/bot'+TELEGRAM_KEY+'/'
WH_URL = 'https://eva-bot.ru/'