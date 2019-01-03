from flask import Flask, request, jsonify, send_from_directory
# from flask_sslify import SSLify
import requests
# from apiai import ApiAI
import json
# import telegram
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# import vk
import random
from config import cfg
from tele_api  import TeleBot
from commands import CommandsRouter

app = Flask(__name__,  static_url_path='')

session = {}


# @app.route(f'/img/<path:path>')
# def send_js(path):
#     return send_from_directory('img', path)

def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

#-------------------------------- WEBHOOKS ---------------------------------------
@app.route(f'/set_wh', methods=['POST', 'GET'])
def tele_set_wh():
    return TeleBot.setWebhook(cfg.WH_URL)

@app.route(f'/get_wh', methods=['POST', 'GET'])
def tele_get_wh_info():
    return getWebhookInfo()

@app.route(f'/del_wh', methods=['POST', 'GET'])
def tele_del_wh():
    return deleteWebhook()

@app.route('/off', methods=['POST', 'GET'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'

# --------------------------------------------------------- ADMIN ---------------------------------------------
@app.route(f'/', methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        r = request.get_json()
        print(r)

        chat_id = r["message"]["chat"]["id"]
        message = r["message"]["text"]
        sender =  r["message"]["from"]["id"]

        if chat_id < 0 and message:
            CommandsRouter.index(chat_id, message, sender)

            # if chat_id not in session:
            #     session[chat_id] =  {}
            #     print("group chat stored")

            # if sender not in session[chat_id]:
            #     session[chat_id][sender] = {}
            #     print(f"member {sender} added")
            #     TeleBot.sendMessage(sender, 'You have added to the Game')
            



        # admins = TeleBot.getChatAdministrators(chat_id)
        # print("admins:")
        # print(admins)
        # print(type(admins))

        # print("------------------------------------")
        # for a in admins:
            # print(a)


        # chat_id = None
        # message = None
        # callback_data = {}

        # if "callback_query" in r:
        #     chat_id = r["callback_query"]["message"]["chat"]["id"]
        #     callback_data = json.loads(r["callback_query"]["data"])
        #     message = "/callback"

        # if "message" in r:
        #     chat_id = r["message"]["chat"]["id"] # в какой чат
        #     message = r["message"]["text"]       # сообщение пользователя

        # if chat_id not in session or message=="/restart":
        #     session[chat_id] = {"loc": "start", "inv": {}, "room_seen": ""}
        
        # if not session[chat_id]["loc"]:
        #     session[chat_id]["loc"] = "start"

        # if message:
        #     if message == "/callback":
        #         session[chat_id]["loc"] = callback_data["loc"]
            
        #     root(session[chat_id]["loc"], chat_id, message)
    
    return '!',200

if __name__ == "__main__":
    app.run(host=cfg.HOST, port=cfg.PORT, debug=cfg.PORT, ssl_context=cfg.CONTEXT)