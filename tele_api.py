import requests

from config import cfg


class TeleBot:

    def sendMessage(chat_id, text, **kwargs):
        url = cfg.URL + 'sendMessage'
        answer = {'chat_id': chat_id, 'text': text,  **kwargs}
        r = requests.post(url, json=answer)
        return r.json()

    def sendPhoto(chat_id, **kwargs):
        url = cfg.URL + 'sendPhoto'
        answer = {'chat_id': chat_id, **kwargs}
        r = requests.post(url, json=answer)
        return r.json()


    def setWebhook(wh_url):
        print("Setting: wh")
        url = cfg.URL + "setWebhook?url=" + wh_url
        print(url)
        r = requests.get(url)
        return str(r.json())
    

    def getWebhookInfo():
        print("Getting: wh")
        url = cfg.URL + "getWebhookInfo"
        print(url)
        r = requests.get(url)
        return str(r.json())

    def del_wh():
        r = requests.get(cfg.URL + "deleteWebhook")
        return str(r.json())


    def getChatAdministrators(chat_id, **kwargs):
        url = cfg.URL + 'getChatAdministrators'
        answer = {'chat_id': chat_id, **kwargs}
        print(answer)
        r = requests.post(url, json=answer)
        print(r)
        return r.json()


