import telebot
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
bot = telebot.TeleBot('Put here your Telegram token')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello")


@bot.message_handler(commands=['search_videos'])
def search_videos(message):
    msg = bot.send_message(message.chat.id, "Enter text, what are you gonna find in YouTube: ")
    bot.register_next_step_handler(msg, search)


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, "Do you want something? ")


def search(message):
    bot.send_message(message.chat.id, "Start searching...")
    video_href = "https://www.youtube.com/results?search_query=" + message.text
    driver.get(video_href)
    sleep(2)
    videos = driver.find_elements_by_id("video-title")
    for i in range(len(videos)):
        bot.send_message(message.chat.id, videos[i].get_attribute('href'))
        if i == 10:
            break


bot.polling()
