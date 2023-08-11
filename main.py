import os
from dotenv import load_dotenv
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, InlineQueryResultArticle, InputTextMessageContent
from api import invitation_templates
from image import test_image
import time
import logging

logging.basicConfig(filename='info.log', filemode='a', level=logging.INFO, format=f"%(asctime)s - %(filename)s - %(message)s - %(lineno)d - %(thread)d")

load_dotenv()
token = os.getenv('API_TOKEN')
bot = telebot.TeleBot(token)
print('The Bot Is Online...')

def start_check(msg):
    text = msg.text
    text = text.split()
    if text[0] =='start':
        my_message = 'سلام به نظر آماده ای ماجراجویی هامون رو باهم شروع کنیم start'
        bot.send_message(msg.chat.id, my_message)


@bot.message_handler(func=start_check)
@bot.message_handler(commands=['start'])
def start(msg):
    logging.info(f"{msg.chat.first_name}")
    my_message = 'سلام به نظر آماده ای ماجراجویی هامون رو باهم شروع کنیم'
    my_message = my_message + "  "+ str(msg.chat.first_name)
    print(msg.chat)
    # bot.reply_to(msg, my_message)
    bot.send_message(msg.chat.id, my_message)

@bot.message_handler(commands=['image'])
def image(msg):
    test_image(invitation_templates())
    # print(my_message)
    time.sleep(1)
    photo = 'https://cdn.gencraft.com/prod/user/bf053dd8-59d8-46c6-8134-97f6f28d782f/f1a236c4-358d-46e5-bbc8-f29003eb0a6c/images/image1_1024_1024.jpg?Expires=1690220573&Signature=j2Lgn1n9YxAxaBKDgebROYvBBBKx28PCjMWCfyRZZZD3BemInNYes3t03s2dYdo1BIjDjhGK4a~NN9ZS~gqOw8pgsBnRHIkTI1y3tkvxfPWUyhXY7oCE3Ai7EmkjIpt-4oEZG3-ntTLFBDff3wb0EtzEZVJti-Ja4neWO3UDFFgp6jLzP9UtM~pFT8Q90qJHpTsEq4qwz5NYsuS5oTS4YlTaIRWinnRbsScoA5rs75jegl2M4QavysLuDTZP9u--BVi8lLW7XkwXxWyycV1iASPFwdF1-DjxF5pwXOUZLofvJzS6FtAfzM-CAamzn~C1KSvMzftxNbWsMlIWoOBgtA__&Key-Pair-Id=K3RDDB1TZ8BHT8'
    bot.send_photo(msg.chat.id, photo, 'it is caption and its optional')
    # i can send another photo with send_photo
    video = open('test2.mp4', 'rb')
    bot.send_message(msg.chat.id, 'hello')
    bot.send_video(msg.chat.id, video, 'it is caption and its optional')
    # bot.reply_to(msg, f"{my_message}")

@bot.message_handler(commands=['hello'])
def hello(msg):
    test_image(invitation_templates())
    # print(my_message)
    time.sleep(1)
    photo = open('image.png', 'rb')
    bot.send_photo(msg.chat.id, photo)
    # bot.reply_to(msg, f"{my_message}")


def check(msg):
    text = msg.text
    text = text.split()
    if text[0] == 'test':
        bot.send_message(msg.chat.id, 'hi')
@bot.message_handler(func=check)
def test(msg):
    pass

# بررسی اینکه یک فایل دریافت کردیم
@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def doc(msg):
    bot.send_message(msg.chat.id, 'thanks')


@bot.message_handler(func=lambda message: True, content_types=['audio', 'video', 'location', 'contact', 'sticker'])
def default_command(msg):
    bot.reply_to(msg, "this is the default command")




@bot.message_handler(func=start_check)
@bot.message_handler(commands=['kelid'])
def start(msg):
    logging.info(f"{msg.chat.first_name}")
    my_message = 'نمایش کلید ها'
    my_message = my_message + "  "+ str(msg.chat.first_name)
    print(msg.chat)
    # bot.reply_to(msg, my_message)
    keyboard = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("درباره ما", callback_data='about')
    btn2 = InlineKeyboardButton("عکس ها", callback_data='image')
    btn3 = InlineKeyboardButton('سلام', callback_data='a')
    keyboard.add(btn1, btn2, btn3)
    # keyboard.add(btn2)

    bot.send_message(msg.chat.id, my_message, reply_markup=keyboard)

@bot.callback_query_handler(func= lambda call: call.data == 'about')
def about(call):
    keyboard = InlineKeyboardMarkup()
    btn2 = InlineKeyboardButton('بازگشت', callback_data='back')
    keyboard.add(btn2)
    text = 'سلام تست'
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard)

@bot.callback_query_handler(func= lambda call: call.data == 'back')
def back(call):
    keyboard = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("درباره ما", callback_data='about')
    keyboard.add(btn1)
    text = 'سلام تست2'
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call:call.data == 'image')
def image_btn(call):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton('تولد')
    btn2 = KeyboardButton('جنگل')
    btn3 = KeyboardButton('بیابان')
    keyboard.add(btn1, btn2, btn3)
    text = 'لیست عکس ها'
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def image_btn_b(msg):
    if msg.chat.type == 'private':
        if msg.text == "تولد":
            # photo = 'https://cdn.gencraft.com/prod/user/89b19de1-d394-445f-b9ec-0ffddf9cd610/c8126b37-12eb-4f15-ab37-c5177d2ad279/images/image0_1024_1024_watermark.jpg?Expires=1690302406&Signature=W2Z0wYyVlohgRmZnLJ52MzBHVPTD76ZBKJlGbvWzmnYcQnExytJXxElpblcHkzUU~LoIG9ZUM9o0~r0CrNpekknLS6V7a3jyCQOSlXyJ6VYnvDb~UkmEFKr7NmJ4jjN5l4~fVyRod22I0Jszk-UXTsFJhW2i6at1a88b3uINYxa8xoKfBpgwgc0iCVr3IxYmXaAzpeaE3UmVZ-9ZuHIhBEhg9cSJwRSmKdeWbNQCxADHEjV0OD0JeRCiLp-BquXgKAlV8hX97Dlim46HN8tl2MuguG0h54X8b9eWcG3pZw-xy1Yl3IW2AMc08fN6sIc01kkKspw5l23Ls8fjxTrnhw__&Key-Pair-Id=K3RDDB1TZ8BHT8'
            # bot.send_photo(msg.chat.id, photo=photo)
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = KeyboardButton('سلام ، سلامتی صاب تول')
            btn2 = KeyboardButton('دست جیغ ماچ بغل')
            btn3 = KeyboardButton('جوغیدم یک گل ناب کرم')
            keyboard.add(btn1)
            keyboard.add(btn2)
            keyboard.add(btn3)
            text = 'لیست عکس های تولد'
            bot.send_message(msg.chat.id, 'birthday', reply_markup=keyboard)

    if msg.text == 'سلام ، سلامتی صاب تول':
        text = """
            [میدونم فکر کردی عکسه ولی این ویدیوعه]

            
            
            
            https://www.youtube.com/watch?v=SclL-9av9GQ&list=PLQNHe26WJklD32a90YHtLwv5kQ8zbvjYN&index=7
            """
        bot.send_message(msg.chat.id, text=text, parse_mode='markdown')
    
    if msg.text == 'دست جیغ ماچ بغل':
        text = """
            [دست جیغ ماچ بغل](https://www.youtube.com/watch?v=SclL-9av9GQ&list=PLQNHe26WJklD32a90YHtLwv5kQ8zbvjYN&index=7)
            """
        bot.send_message(msg.chat.id, text=text, parse_mode='markdown')


#*******************inline command*****************
@bot.inline_handler(lambda query: query.query=='shad')
def test(inline_query):
    result = InlineQueryResultArticle(
        id='1',
        title='shad',
        input_message_content=InputTextMessageContent('سلام این بات در حال تست است.')
    )
    bot.answer_inline_query(inline_query.id, [result])




bot.polling()