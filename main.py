from init_bot import bot
from handlers import register_handlers

if __name__ == "__main__":
    register_handlers()
    print("Бот запущен")
    bot.infinity_polling()
