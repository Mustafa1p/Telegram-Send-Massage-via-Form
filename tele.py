import tkinter as tk
from tkinter import scrolledtext
import telebot
import threading

# Replace "YOUR_TELEGRAM_BOT_TOKEN" with your actual Telegram bot token
bot_token = "YOU_API_TOEKN" #FROM BOTFATHER 
bot = telebot.TeleBot(bot_token)

def start_bot():
    print("ACTIVE")
    bot.infinity_polling()

@bot.message_handler(commands=["start"])
def welcome(message):
    bot.reply_to(message, "Welcome to the bot! How can I assist you today?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

def send_message():
    chat_id = input_box_chat_id.get("1.0", tk.END).strip()
    msg = input_box_message.get("1.0", tk.END).strip()
    input_box_chat_id.delete("1.0", tk.END)
    input_box_message.delete("1.0", tk.END)
    bot.send_message(chat_id, msg)

root = tk.Tk()
root.title("Telegram Bot Send massages")

frame = tk.Frame(root)
frame.pack()

label_chat_id = tk.Label(frame, text="Chat ID:")
label_chat_id.pack()
input_box_chat_id = tk.Text(frame, height=1)
input_box_chat_id.pack()

label_message = tk.Label(frame, text="Message:")
label_message.pack()
input_box_message = tk.Text(frame, height=4)
input_box_message.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

threading.Thread(target=start_bot).start()

root.mainloop()
