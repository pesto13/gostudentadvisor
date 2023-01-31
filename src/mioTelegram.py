


from dotenv import load_dotenv

import os
import telebot

def configure():
    load_dotenv()

configure()
bot = telebot.TeleBot(os.getenv('TOKEN'))


def inviaMessaggio(studente, emoji):
    text = ""
    text += f"<b>{emoji} {studente.materia} {emoji}</b>"
    text += "\n"
    text += "• "+studente.anno
    text += "\n"
    text += "• "+studente.info
    text += "\n"
    text += "\n"
    text += "• "+studente.lezioni
    text += "\n"
    text += f"<a  href='{studente.walink}'>Riferimento: {studente.numero}</a>"
    
    bot.send_message(chat_id=os.getenv("chat_id"), text=text, parse_mode="html")

def invio(messaggio):
    bot.send_message(chat_id=os.getenv("chat_id"), text=messaggio)

#bot.infinity_polling()