import google.generativeai as genai
import requests
import time
import telebot
TOKEN = "7012455970:AAEXFgsU2G7RndFdorK8U7IU_VHVWrnCUFo"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['ask'])
def gpt(message):
  
  chat_id = message.chat.id
  genai.configure(api_key="AIzaSyAAS4CmjtLudX3fRdip4f6SxTMAzNQmrag")

  generation_config = {
    "temperature": 1,
    "top_p": 1,
    "top_k": 64,
    "max_output_tokens": 8024,
  }

  safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
  ]

  model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                            generation_config=generation_config,
                              safety_settings=safety_settings)
  start_time = time.time()
  prompt_parts = message.text.split()[1:]
  prompt_parts = ' '.join(prompt_parts)

  response = model.generate_content(prompt_parts)
  end_time = time.time()
  response_time = end_time - start_time
  bot.reply_to(message, f"{response.text}\n\n{response_time}", parse_mode="Markdown")
bot.infinity_polling()
