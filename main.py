import telebot
import webbrowser
from telebot import types
import random

bot = telebot.TeleBot('6988336366:AAFXEQ8hEh1ntHbKCdRPnRJnPGUPeaUY2sI')

#FOR FUTURE!!! Make 8ball for Bot
#################################

responses = [
    "Այո",
    "Համաձայն չեմ",
    "Հնարավոր է",
    "Այո, միայն ժամանակի համար",
    "Դատարկ մնա",
    "Ապական արդյունքներն են",
    "Կարող եք հասկանալ կատարվածի շաբաթում",
    "Վստահ եմ",
    "Հնարավոր չէ",
    "Անհանգստացնելի է",
]

@bot.message_handler(commands=['8ball'])
def eight_ball(message):
    if len(message.text.split()) == 1:
        bot.reply_to(message, "Խնդրում եմ գրեք ձեր հարցը։ ")
        return
    question = " ".join(message.text.split()[1:])
    response = random.choice(responses)
    bot.reply_to(message, f"🎱 Պատասխան: {response} 🔮")


#Help information
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Ահա բոլոր հրամանները\n/start\n/dasacucak\n/help' , parse_mode='html')


#Response On Hello
hello_arr =  ['Բարև Անժելա բոտ', 'Barev Anjela Bot']
@bot.message_handler(func=lambda message: any(word.lower() in message.text.lower() for word in hello_arr))
def respond_to_hello(message):
    bot.send_message(message.chat.id, f'Բարև, {message.from_user.first_name}')
#########################################
    
    
# #Replying Your ID
# @bot.message_handler(func=lambda message: message.text.lower() == 'id')
# def send_user_id(message):
#     bot.reply_to(message, f'<b>ID: </b> {message.from_user.id}', parse_mode='html')

#Sending Image ***!!!SECRET!!!***
# pic_arr = ['Give Me A Beautiful Image From All The World', 'Give me pic']
# @bot.message_handler(func=lambda message: any(word.lower() in message.text.lower() for word in pic_arr))
# def send_pic(message):
#     file = open('image.png', 'rb')
#     bot.send_photo(message.chat.id, file)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    #Sending button with URL
    btn1 = types.KeyboardButton('Ուղարկիր ինձ դասացուցակը')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Help')
    markup.row(btn2)
    bot.send_message(message.chat.id, f'Բարև, {message.from_user.first_name}: Ինչո՞վ կարող եմ օգտակար լինել։', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

dasacucak = open('Dasacucak.jpg', 'rb')

def on_click(message):
    if message.text == 'Ուղարկիր ինձ դասացուցակը':
        bot.send_photo(message.chat.id, dasacucak)
    elif message.text == 'Help':
        help(message)

@bot.message_handler(commands=['dasacucak'])
def give_dasacucak(message):
    bot.send_photo(message.chat.id,  open('Dasacucak.jpg', 'rb'), caption='Ահա քո դասացուցակը')

#Replying To Photo
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message, '😍😍😍')


#Func For Delete and Edit Message
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#     elif callback.data == 'edit':
#         bot.edit_message_text('Edit Text', callback.message.chat.id, callback.message.message_id)



bot.infinity_polling()





#DAY 3
#Cuurent Time(Date,Week , etc.)
#