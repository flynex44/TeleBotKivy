from kivy.app import App
from kivy.uix.button import Button
import telebot
import pyowm
import datetime
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM('08436b1b32cdca9d4da6b76279c8353e', config_dict)
bot = telebot.TeleBot("1706105429:AAGt3jv2IFfY_kNpuisusZxvEcPo2B7ACX0")
now = datetime.datetime.now()


Button(text='hello world')
print("111")
class TestApp(App):

    @bot.message_handler(func=lambda m: True)

    def echo_all(message):
        if "/w " in message.text:
            message.text = message.text.replace('/w ', '')
            try:
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place(message.text)
                w = observation.weather
                # w.wind()['speed'], w.humidity, w.temperature('celsius')['temp'], w.rain
                weather_info = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
                weather_info += "Темпиратура: " + str(w.temperature('celsius')['temp']) + "\n"
                weather_info += "Скорость ветра: " + str(w.wind()['speed']) + " м.с" + "\n"
                weather_info += "Влажность: " + str(w.humidity) + "%" + "\n"
                weather_info += "Дождь: " + str(w.rain) + "\n"
                bot.reply_to(message, weather_info)
            except:
                bot.reply_to(message, "Неправильное название города!")
        elif message.text == "/help" or message.text == "помощь":
            bot.reply_to(message, "/w 'Название города без ковычек' - Узнать погоду в городе")
        elif message.text == "Время" or message.text == "Время":
            bot.reply_to(message, "Сейчас: " + now.strftime('%Y-%m-%d %H:%M:%S'))
        else:
            bot.reply_to(message, "Напишите /help или помощь")

    bot.polling()




if __name__ == '__main__':
    TestApp().run()