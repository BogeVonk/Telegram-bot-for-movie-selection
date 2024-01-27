import random

import telebot

from func.date_time import get_welcome
from init_bot import bot


@bot.message_handler(commands=["start", "help"])
def start_help(message: telebot.types.Message):
    text = (f"{get_welcome()} Я помогу тебе выбрать фильм)\n\n"
            f"Список команд:\n"
            f"/movie_morning - фильм на утро\n"
            f"/daytime_movie - фильм днём\n"
            f"/evening_movie - вечерний фильм\n"
            f"/night_movie - ночной фильм\n"
            f"/movie_couple - фильм для парочки")
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["movie_morning"])
def movie_morning(message: telebot.types.Message):
    with open("movie_morning", "r", encoding="utf-8") as file:
        movies = file.read().split("\n")
    movie = random.choice(movies)
    bot.send_message(message.chat.id, text=f"Утром лучше посмотреть вдохновляющий фильм: \n _*{movie}*_",
                     parse_mode='MarkdownV2')


@bot.message_handler(commands=["daytime_movie"])
def movie_morning(message: telebot.types.Message):
    with open("daytime_movie", "r", encoding="utf-8") as file:
        movies = file.read().split("\n")
    movie = random.choice(movies)
    bot.send_message(message.chat.id, text=f"Днём лучше посмотреть расслабляющий фильм: \n _*{movie}*_",
                     parse_mode='MarkdownV2')


@bot.message_handler(commands=["evening_movie"])
def movie_morning(message: telebot.types.Message):
    with open("evening_movie", "r", encoding="utf-8") as file:
        movies = file.read().split("\n")
    movie = random.choice(movies)
    bot.send_message(message.chat.id, text=f"Вечером лучше посмотреть напряжённый фильм: \n _*{movie}*_",
                     parse_mode='MarkdownV2')


@bot.message_handler(commands=["night_movie"])
def movie_morning(message: telebot.types.Message):
    with open("night_movie", "r", encoding="utf-8") as file:
        movies = file.read().split("\n")
    movie = random.choice(movies)
    bot.send_message(message.chat.id, text=f"Ночью лучше посмотреть завораживающий фильм: \n _*{movie}*_",
                     parse_mode='MarkdownV2')


@bot.message_handler(commands=["movie_couple"])
def movie_morning(message: telebot.types.Message):
    with open("movie_couple", "r", encoding="utf-8") as file:
        movies = file.read().split("\n")
    movie = random.choice(movies)
    bot.send_message(message.chat.id, text=f"Парочке лучше посмотреть романтический фильм: \n _*{movie}*_",
                     parse_mode='MarkdownV2')
