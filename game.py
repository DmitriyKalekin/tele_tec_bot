from config import *
import requests
from random import choice
import sys

session = {
}

def tele_send_message(chat_id, **kwargs):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, **kwargs}
    r = requests.post(url, json=answer)
    return r.json()

def tele_send_photo(chat_id, **kwargs):
    url = URL + 'sendPhoto'
    answer = {'chat_id': chat_id, **kwargs}
    r = requests.post(url, json=answer)
    return r.json()    


def root(name, chat_id, message):
    print("INDEX: processing ", name)
    method_to_call = getattr(__import__(__name__), name)
    res =  method_to_call(name, chat_id, message)
#     if session[chat_id]["room_seen"] != name:
#         session[chat_id]["room_seen"] = name
    return res



def start(name, chat_id, message):
    pp = tele_send_photo(chat_id, photo="http://www.aisystems.ru/temp/hor/img/logo.png", caption="<b>Возвращение квантового кота</b>", parse_mode="html")
#     print(pp)
    tele_send_message(chat_id, text="""
За окном моей хижины снова белеет снег, а в камине так же, как и тогда, потрескивают дрова... Третья зима. Прошло уже две зимы, но те события, о которых я хочу рассказать, встают перед моими глазами так, словно это было вчера...

Я работал лесником уже больше десяти лет. Больше десяти лет я жил в своей хижине, окруженной лесом, собирая капканы браконьеров и выезжая раз в одну или две недели в близлежащий поселок... После воскресной службы в местной церкви я заходил в магазинчик и покупал необходимые мне вещи: патроны к дробовику, крупу, хлеб, лекарства... 

Когда-то я был неплохим компьютерным специалистом... Впрочем, это уже не важно... Десять лет я не видел экрана монитора, и не жалею об этом.

Теперь я понимаю, что корни того, что тогда произошло, лежат давно — во второй половине 30-х... Хотя лучше начать все по-порядку...

В тот холодный февральский день я, как всегда, собрался ехать в поселок...
    """,  
    reply_markup={
        "inline_keyboard": [
                [{
                        "text": "[ Дальше ]",
                        "callback_data": "{ \"loc\": \"home\" }"
                }]
        ]
    },
    parse_mode="markdown")


def have(chat_id, name):
    return name in session[chat_id]["inv"]

def take(chat_id, val):
    

    if "tak" in val:
        session[chat_id]["inv"][val["id"]] = val
        print("INV", session[chat_id]["inv"])
        if val["id"]  in session[chat_id]["obj"]:
                del session[chat_id]["obj"][val["id"]]
        return val["tak"]

    return "Боюсь, я не смогу этого сделать."


def act_table(chat_id):
    if not have(chat_id, "money"):
        take(chat_id, {
                "id": "money",
                "nam" : 'деньги',
                "inv" : 'Большие деньги — большое зло... Хорошо что у меня немного денег...',
                "tak": 'Порывшись в ящиках я достал деньги.'
        })
        return 'Порывшись в ящиках я достал деньги.'
    return 'Стол... Этот стол я сделал своими руками.';

                
def find_object(message, obj_list):
        words = message.split()
        for w in words:
                for k, v in obj_list.items():
                        if "nam" in v and v["nam"][:-1].lower() in w[:-1].lower():
                                return v
        return None

def find_command(message):
        words = message.split()
        for w in words:
                if "надет" in w.lower() or "одет" in w.lower() or "взят" in w.lower():
                        return "take"
        return "act"

def act(chat_id, obj):
    if "act" not in obj:
            return ""
    
    if callable(obj["act"]):
            return obj["act"](chat_id)
    
    return obj["act"]
        




def home(name, chat_id, message):
    obj_list = { 
            'fireplace' : {
                "id":     "fireplace", 
                "nam" : 'камин',	
                "dsc" : 'У стены стоит {*камин*}. Огоньки пламени неравномерно освещают хижину.',
                "act" : 'Мне нравится сидеть у камина долгими зимними вечерами.',
             },
             'mytable': {
                        "id":     "mytable", 
                        "nam" : 'стол',
                        "dsc" : 'В левом углу стоит дубовый {*стол*} с ящиками.',
                        "act" : act_table

              }, 
             'foto': {
                        "id":     "foto", 
                        "nam" : 'фото',
                        "dsc" : 'На столе стоит {*фотокарточка*} в рамке.',
                        "act":  'Я смотрю на изображение моего кота у меня на руках.',
                        "tak" : 'Я взял фотографию.',
                        "inv" : 'На этой фотографии изображены я и мой Барсик.',
              }, 
             'mycat': {
                        "id":     "mycat", 
                     "nam": "Барсик",
                     "dsc": "Возле камина уютно свернувшись в клубок спит мой кот {*Барсик*}.",
                     "act": "Я чешу Барсику за ушком."
             }, 
             'gun': {
                "id":     "gun", 
                "nam" : 'дробовик',
                "dsc" : 'В правом углу хижины стоит {*дробовик*}.',
                "tak" : 'Я взял дробовик и повесил его за спину.',
                "act":  "Я верчу в руках дробовик. С ним я выгляжу серьезно."
             }, 
             'mywindow': {
                "id":     "mywindow", 
                "nam": 'окно', 
                "dsc": 'В хижине есть единственное {*окно*}.',
                "act":  "Я смотрю в окно. За окном белым-бело..."
             }, 
             'mybed': {
                "id":     "mybed", 
                "nam" : 'кровать',
                "dsc" : 'У окна стоит {*кровать*}.',
                "act" : 'Сейчас не время спать.',
              }, 
              'mywear': {
                        "id":     "mywear", 
                      "nam" : 'ватник',
                      "dsc" : 'На гвоздике, вбитом в сосновую дверь, висит {*ватник*}.',
                      "act":  "Я разглядываю ватник. Он старый, но тёплый.",
                      "tak": "Я надеваю ватник. Мне в нём будет тепло."
              } 
              
    }


    if session[chat_id]["room_seen"] !=name:
        session[chat_id]["room_seen"] = name
        session[chat_id]["obj"] = obj_list
        pp = tele_send_photo(chat_id, photo="http://www.aisystems.ru/temp/hor/img/room_cat.png", caption="<b>Хижина</b>", parse_mode="html")

        descr = " ".join([ str(v["dsc"]) for k,v in obj_list.items() if "dsc" in v ])


        tele_send_message(chat_id, text=f"""
        В этой хижине я провел 10 лет. 10 лет назад я своими руками построил ее. Довольно тесно, но уютно.

{descr}

```
Чтобы взаимодействовать с объектами - опишите это действие в чате текстом.
Чтобы начать заново - напишите `/restart`
```
        """,  
        reply_markup={
                "inline_keyboard": [
                        [{
                                "text": "[ Идти: Перед хижиной ]",
                                "callback_data": "{ \"loc\": \"forest\" }"
                        }]
                ]
        },
        parse_mode="markdown")
    else:
        cur_obj = find_object(message, obj_list)    
        action = ""
        if cur_obj:
                command = find_command(message)
                print(command)
                print(cur_obj)

                if command=="take":
                        action = take(chat_id, cur_obj)
                else:
                        action = act(chat_id, cur_obj)
        
        if action == "":
                action = "Ничего не происходит"
                

        tele_send_message(chat_id, text=f"""{action}""",  
        parse_mode="markdown")          


def forest(name, chat_id, message):
#     pp = tele_send_photo(chat_id, photo="http://www.aisystems.ru/temp/hor/img/room_cat.png", caption="<b>Хижина</b>", parse_mode="html")


#     obj = { 'fireplace', 'mytable', 'foto', 'mycat', 'gun', 'mywindow', 'mybed', 'mywear' }
    if not have(chat_id, "money"):    
        session[chat_id]["loc"] = "home"
        session[chat_id]["room_seen"] = "home"
        tele_send_message(chat_id, text="""
        Мне кажется, я что-то забыл. Надо поискать в хижине.
        """,
        parse_mode="markdown")
        return
    
    if not have(chat_id, "mywear"):    
        session[chat_id]["loc"] = "home"
        session[chat_id]["room_seen"] = "home"
        tele_send_message(chat_id, text="""
        На улице холодно... Я не пойду туда без моего ватника.
        """,
        parse_mode="markdown")
        return    

    pp = tele_send_photo(chat_id, photo="http://www.aisystems.ru/temp/hor/img/forest.png", caption="<b>Перед хижиной</b>", parse_mode="html")


    tele_send_message(chat_id, text=f"""
        Когда я выходил из хижины, Барсик внезапно проснулся и бросился мне под ноги. Я погладил его за ушами — Значит едем вместе?

        На улице перед хижиной все занесено снегом. Дикий лес окружает хижину со всех сторон. Дорога, ведущая в поселок, занесена снегом.



```
Поздравляем! Вы прошли первую комнату! Больше комнат в этой тестовой игре нет.
Вы можете поиграть в полную версию игры тут:
http://instead-games.ru/instead-em/?/games/instead-cat-1.6.zip
http://instead-games.ru/instead-js/#zip:/games/instead-cat-1.6.zip
Чтобы начать заново - напишите `/restart`

```
        """,  
        reply_markup={
                "inline_keyboard": [
                        [{
                                "text": "[ Хижина ]",
                                "callback_data": "{ \"loc\": \"home\" }"
                        }, {
                                "text": "[ Чаща ]",
                                "callback_data": "{ \"loc\": \"deep_forest\" }"
                        }, {
                                "text": "[ Дорога ]",
                                "callback_data": "{ \"loc\": \"road\" }"
                        }]
                ]
        },
        parse_mode="markdown")



def deep_forest(name, chat_id, message):


    pp = tele_send_photo(chat_id, photo="http://www.aisystems.ru/temp/hor/img/deep_forest.png", caption="<b>Чаща</b>", parse_mode="html")


    tele_send_message(chat_id, text=f"""
В чаще страшно, холодно и легко заблудиться. Кажется, я слышу, как неподалёку воют волки...
        """,  
        reply_markup={
                "inline_keyboard": [
                        [{
                                "text": "[ Перед хижиной ]",
                                "callback_data": "{ \"loc\": \"forest\" }"
                        }]
                ]
        },
        parse_mode="markdown")       

def road(name, chat_id, message):

    tele_send_message(chat_id, text=f"""
        Дороги пока нет. 
        """,  
        reply_markup={
                "inline_keyboard": [
                        [{
                                "text": "[ Перед хижиной ]",
                                "callback_data": "{ \"loc\": \"forest\" }"
                        }]
                ]
        },
        parse_mode="markdown")           