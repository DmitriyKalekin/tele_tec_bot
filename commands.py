from tele_api import TeleBot

class CommandsRouter:
    """
    """
    
    def index(chat_id, message, sender, **kwargs):
        """
        """
        if message.lower() == "/start_game":
            start_game(chat_id, message)
            return

    def start_game(chat_id, message, sender, **kwargs):
        """
        """
        TeleBot.sendMessage(
            chat_id, 
            f"{sender} желает начать новую игру. У вас 1 минута. Чтобы присоединиться нажмите [Join]",
            reply_markup={
                "inline_keyboard": [
                        [{
                            "callback_data": "{ \"game_id\": \"detective\" }"
                        }]
                ]
            },
            parse_mode="markdown"
        )




