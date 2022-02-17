from webbrowser import get
import telebot;


bot = telebot.TeleBot('5111904045:AAEDPZLqKaacz7BFQV9Aohjj-5gmjEmoUCA');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    helpStr="Привет, это проект MedBot - Многофункциональный сервис для медицинской диагностики заболеваний. Внимание: при любом диагнозе необходима консультация врача! \n Для информации введите /help."
    splitted_text = str(message.text).lower().split()
    if str(message.text).lower() == "привет":
        bot.send_message(message.from_user.id, helpStr)
    elif str(message.text).lower() == "/help":
        bot.send_message(message.from_user.id, "MedBot - Многофункциональный сервис для медицинской диагностики заболеваний. Внимание: при любом диагнозе необходима консультация врача! \n Список команд: \n /q - Начать опрос\n")
    elif str(message.text).lower() == "/q":
        bot.send_message(message.from_user.id, "dds")
    else:
        bot.send_message(message.from_user.id, helpStr)

bot.polling(none_stop=True, interval=0)