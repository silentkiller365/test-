import os
import telebot
bot =telebot .TeleBote("5117499847:AAHr9by8LAI2m15TWZrBSEnn8WpwEe9-EWs")
@bot.massage_handler(commands=["start"])
def send_wellcome(massage):
    bot.reply_to(massage,"HELLO I'M TEST# BOT")

@bot.massage_handler(commands=["ssh"])
def send_massage(massage):
    bot.send_massage(massage,"connecting the sever☁️")

bot.polling()