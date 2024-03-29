from dotenv import load_dotenv
import os
import telebot
from telebot.util import quick_markup
import telebot.types as t
from dataclasses import dataclass

#TODO
"""
1. salvo gli id su file/ram
2. mando i messaggi in privato
3. configurazione delle materie
"""



@dataclass
class Contatto:
    id: str
    materie: list



def loadContatti():
    with open('contatti.txt', 'r', encoding="utf-8") as f:
        return f.read()

def writeContatti():
    with open('contatti.txt', 'w', encoding="utf-8") as f:
        for c in contatti:
            f.write(c)

def configure():
    load_dotenv()
    loadContatti()


contatti = []
configure()    
bot = telebot.TeleBot(os.getenv('TOKEN'))

@bot.message_handler(commands=['setup'])
def setup(m):
    cid = m.chat.id
    print(cid)
    print("eccomi")
    if(cid not in [c.id for c in contatti]):
        bot.send_message(cid, "ti sei registrato!")
        contatti.append(Contatto(cid, [1,2]))
    else:
        bot.send_message(cid, "sei già registrato!")

""" 
@bot.callback_query_handler(func=lambda c:True)
def menu(c):
    print("eccomi")
    if c.data == 'whatever':
        qm = quick_markup({
                'hah': {'url': 'https://twitter.com'},
                'cambia': {'callback_data': 'hihi'}
            })
        
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=qm)
    elif c.data == 'hihi':
        qm = quick_markup({
                'Twitter': {'url': 'https://twitter.com'},
                'Facebook': {'url': 'https://facebook.com'},
                'Back': {'callback_data': 'whatever'}
            })
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=qm)


@bot.message_handler(commands=['kb'])
def kb(m):
    cid = m.chat.id
    qm = quick_markup({
        'Twitter': {'url': 'https://twitter.com'},
        'Facebook': {'url': 'https://facebook.com'},
        'Back': {'callback_data': 'whatever'}
    })
    #t.InlineKeyboardButton("hihi")
    bot.send_message(cid, "suvvia", reply_markup=qm)


 """

def inviaMessaggio(studente, emoji):
    print("stampoooo")
    text = ""
    text += f"<b>{emoji} {studente.materia} {emoji}</b>"
    text += "\n"
    text += "• "+studente.anno if studente.anno != None else "non specificato"
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




#TODO questo non mi lascia lanciare il main, fare in parallelo?
# bot.infinity_polling()