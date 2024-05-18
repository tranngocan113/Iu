from telebot import types
#code này để chạy bot thêm tính năng là chạy phà phà
import datetime
import io
import random
import telebot
import time
import os
os.system('clear')
print("♥️♥️♥️BOT ĐANG HOẠT ĐỘNG♥️♥️♥️")
import subprocess
import string
import sqlite3
import hashlib
import requests
import datetime
import google.generativeai as genai
import sys
import threading
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
import subprocess
import requests
from bs4 import BeautifulSoup
import requests
import re
import telebot
from pytube import YouTube
from urllib.parse import quote
import datetime
import os
import ssl
from googleapiclient.discovery import build
import random
from urllib.parse import urlencode
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
import hashlib
import uuid
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import time
import sys
import requests
import re
import telebot


YOUTUBE_API_KEY = "AIzaSyAIHM6HyTJ516JsgLG6IcHiHyY2-lMEXBI"
TOKEN = "6968514461:AAGsMuuNxpVpSOK3LCLqi1L_bfDBRynxBmc"
bot = telebot.TeleBot(TOKEN)
processes = []
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
video_info = {}
admin_huy = "andzvcl"
ADMIN_ID1 = 6216148625
GROUP_ID = -1001906536250
cooldown_dict = {}
allowed_users = []
processes = []
proxy_update_count = 0
last_proxy_update_time = time.time()
admin_vip = 'admin.txt'
def get_click_to_copy_link(video_url):
    try:
        yt = YouTube(video_url)
        video_title = yt.title
        count = 'Ngọc An'
        click_to_copy_link = f'<a href="{video_url}">{count}. {video_title}</a>'
        ###########byNgocAn
        return click_to_copy_link
    except Exception as e:
        print("Error:", e)
        return None

# ######
def generate_random(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
    
def get_random_lastname():
    with open("lastname.txt", "r") as file:
        lastnames = file.readlines()
        return random.choice(lastnames).strip()

def get_random_firstname():
    with open("firstname.txt", "r") as file:
        firstname = file.readlines()
        return random.choice(firstname).strip()
def load_allowed_users():
    try:
        with open(admin_vip, 'r') as file:
            allowed_users = [int(line.strip()) for line in file]
        return set(allowed_users)
    except FileNotFoundError:
        return set()
cooldown_dict = {}
is_bot_active = True
delay_delete = int(180)
# Hàm tính thời gian hoạt động của bot
start_time = time.time()
proxy_update_count = 0
proxy_update_interval = 600 
def TimeStamp():
    now = str(datetime.date.today())
    return now
is_bot_active = True
@bot.message_handler(commands=['ask'])
def gpt(message):
  chat_id = message.chat.id
  genai.configure(api_key="AIzaSyAAS4CmjtLudX3fRdip4f6SxTMAzNQmrag")

# Set up the model
  generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
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

  model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

  prompt_parts = message.text.split()[1:]
  prompt_parts = ' '.join(prompt_parts)

  response = model.generate_content(prompt_parts)
  bot.send_message(chat_id, f"{response}")
print(response.text)
@bot.message_handler(commands=['facebook'])
def create_facebook_account(message):
    
    sent_message = bot.send_message(message.chat.id, "Đang tạo tài khoản...")
    password = "Mrcs122007€£"
    success = False
    
    while not success:
        random_chars = generate_random(6)
        lastname = get_random_lastname()
        firstname = get_random_firstname()
        domain = random.choice(["@villastream.xyz", "@villastream.xyz", "@villastream.xyz", "@villastream.xyz"])
        mail = f"{firstname.lower()}{lastname.lower()}{random_chars}{domain}"
        sex = random.randint(1, 2)
        birthday_day = str(random.randint(10, 30))
        birthday_month = str(random.randint(1, 12))
        birthday_year = str(random.randint(1970, 2005))

        if sex == 1:
            gender = "👧 Nữ"
        elif sex == 2:
            gender = "🧑 Nam"
        else:
            gender = "Không xác định"

        cookies = {
            'datr': 'thk-ZqmsVOopQu0GZ-DgnrHf',
            'sb': 'thk-ZiSZQ0FpUUdkLdIsxuKi',
            'm_pixel_ratio': '1.5625',
            'wd': '461x939',
            'fr': '0FTZVuy6ZTMZbQqRW..BmPhm5..AAA.0.0.BmPhnD.AWVRgvzpEzg',
            'rs': '%7C%7C%7C2%7Cgghdhg%40gmail.com%7CGad%7CAnhd%7CGad+Anhd',
            'ps_n': '1',
            'ps_l': '1',
        }

        headers = {
            'authority': 'mbasic.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=thk-ZqmsVOopQu0GZ-DgnrHf; sb=thk-ZiSZQ0FpUUdkLdIsxuKi; m_pixel_ratio=1.5625; wd=461x939; fr=0FTZVuy6ZTMZbQqRW..BmPhm5..AAA.0.0.BmPhnD.AWVRgvzpEzg; rs=%7C%7C%7C2%7Cgghdhg%40gmail.com%7CGad%7CAnhd%7CGad+Anhd; ps_n=1; ps_l=1',
            'dpr': '1.5625',
            'origin': 'https://mbasic.facebook.com',
            'referer': 'https://mbasic.facebook.com/reg',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"SM-A125F"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"12.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'viewport-width': '980',
        }

        data = {
            'lsd': 'AVqI4IzBamc',
            'jazoest': '2955',
            'ccp': '2',
            'reg_instance': 'thk-ZqmsVOopQu0GZ-DgnrHf',
            'submission_request': 'true',
            'helper': '',
            'reg_impression_id': '44cae64f-eeb1-44fd-b395-596e34909bff',
            'ns': '0',
            'zero_header_af_client': '',
            'app_id': '',
            'logger_id': '',
            'field_names[]': [
                'firstname',
                'reg_email__',
                'sex',
                'birthday_wrapper',
                'reg_passwd__',
            ],
            'lastname': lastname,
            'firstname': firstname,
            'reg_email__': mail,
            'sex': sex, 
            'custom_gender': '',
            'did_use_age': 'false',
            'birthday_day': birthday_day, 
            'birthday_month': birthday_month,
            'birthday_year': birthday_year,
            'age_step_input': '',
            'reg_passwd__': password,
            'submit': 'Đăng ký',
        }

        response = requests.post('https://mbasic.facebook.com/reg/submit/', cookies=cookies, headers=headers, data=data)

        if 'Chúng tôi sẽ hướng dẫn một số bước để bạn có thể xác nhận tài khoản trên Facebook.</div><div class="be bh bi">Hoàn tất các bước này trong 180 ngày tới để chắc chắn là bạn có thể dùng tài khoản này' in response.text:
            success = True
            response_data = f"┌─────⭓Create Account FB | test\n│»  🔔 Xin Chào: @{message.from_user.username}\n│»  👤Tên: {firstname} {lastname}\n│»  📧Email: {mail}\n│»  🔑Mật khẩu: Mrcs122007€£\n│»  👶Giới tính: {gender}\n│»  🍰Sinh nhật: {birthday_day}/{birthday_month}/{birthday_year}\n│»  📃Mail|Pass: {mail}|Mrcs122007€£\n│»  🌐 Trạng thái: ✅️ Success !\n└────────────────────────"
            bot.send_message(message.chat.id, response_data)
            bot.delete_message(message.chat.id, sent_message.message_id)
        else:
            continue
    
        
@bot.message_handler(commands=['random_face'])
def send_random_face(message):
    sent_message = bot.send_message(message.chat.id, "Vui lòng đợi lấy ảnh...")
    response = requests.get("https://thispersondoesnotexist.com/")
    
    if response.status_code == 200:
        bot.send_photo(message.chat.id, response.content)
        bot.delete_message(message.chat.id, sent_message.message_id)
    else:
        bot.reply_to(message, "Không thể lấy ảnh vào lúc này.")
        bot.delete_message(message.chat.id, sent_message.message_id)

@bot.message_handler(commands=['rad'])
def delete_admin(message):
    admin_id = message.from_user.id
    if admin_id != ADMIN_ID1:
        bot.reply_to(message, 'Lệnh Này Chỉ Dành Cho Admin Tạo Ra Bot.')
        return
    if message.text.split()[1] == 'all':
        admin_list = [int(line.strip()) for line in open(admin_vip, 'r').readlines()]
        admin_count = len(admin_list)
        sent_message = bot.reply_to(message, f'Đã xoá {admin_count} admin trong group')
        with open(admin_vip, 'w') as file:
            file.write('\n'.join(map(str, load_allowed_users())))
    if message.reply_to_message is None:
        sent_message = bot.reply_to(message, 'Hoặc cũng có thể sử dụng lệnh này bằng cách trả lời tin nhắn của người dùng mà bạn muốn xoá admin')
        time.sleep(delay_delete)
        bot.delete_message(chat_id=message.chat.id, message_id=sent_message.message_id)
        return
    admin_can_xoa = int(message.reply_to_message.from_user.id)
    allowed_users = load_allowed_users()
    if admin_can_xoa not in load_allowed_users():
        sent_message = bot.reply_to(message, f'ID {admin_can_xoa} không có trong danh sách admin.')
        time.sleep(delay_delete)
        bot.delete_message(chat_id=message.chat.id, message_id=sent_message.message_id)
        return
    allowed_users.remove(admin_can_xoa)
    with open(admin_vip, 'w') as file:
        file.write('\n'.join(map(str, allowed_users)))
    bot.reply_to(message, f'Đã xoá admin có ID: {admin_can_xoa}')
@bot.message_handler(commands=['admin'])
def show_admin(message):
    admin_list = [int(line.strip()) for line in open(admin_vip, 'r').readlines()]
    admin_count = len(admin_list)
    bot.reply_to(message, f'Danh sách admin: {admin_list}\n+ Có tổng: {admin_count} admin.')
@bot.message_handler(commands=['add'])
def add_user(message):
    admin_id = message.from_user.id
    if admin_id != ADMIN_ID1:
        bot.reply_to(message, 'bot tạo ra là để admin sài.')
        return
    if message.reply_to_message is None:
        sent_message = bot.reply_to(message, 'Vui lòng sử dụng lệnh này bằng cách trả lời tin nhắn của người dùng mà bạn muốn thêm admin')
        time.sleep(delay_delete)
        bot.delete_message(chat_id=message.chat.id, message_id=sent_message.message_id)
        return
    add_adminid = message.reply_to_message.from_user.id
    if add_adminid in load_allowed_users():
        sent_message = bot.reply_to(message, f'Người dùng có ID {add_adminid} đã có trong danh sách admin.')
        time.sleep(delay_delete)
        bot.delete_message(chat_id=message.chat.id, message_id=sent_message.message_id)
        return
    with open(admin_vip, 'a') as file:
        file.write(str(add_adminid) + '\n')
        bot.reply_to(message, f'Đã thêm người dùng có id: {add_adminid}\n+ Cấp quyền làm ADMIN.')
        return
@bot.message_handler(commands=['id'])
def check_user_id(message):
    if message.reply_to_message is None:
        bot.reply_to(message, 'Vui lòng sử dụng lệnh này bằng cách trả lời tin nhắn của người dùng mà bạn muốn kiểm tra ID.')
        return

    user_id = message.reply_to_message.from_user.id
    username = message.reply_to_message.from_user.username
    bot.reply_to(message, f'ĐÂY LÀ TÊN : \n+ {username}. \n+ có ID là: {user_id}.')
@bot.message_handler(commands=['search'])
def youtube_search(message):
    if len(message.text.split()) == 1:
        sent_message = bot.reply_to(message, 'VUI LÒNG NHẬP TỪ KHÓA /search {Từ Khóa}.')
        return
    search_query = message.text.split(' ', 1)[1] 
    youtube = build('youtube', 'v3', developerKey='AIzaSyAIHM6HyTJ516JsgLG6IcHiHyY2-lMEXBI') # Thay bằng khóa API YouTube của bạn
    request = youtube.search().list(q=search_query, part='snippet', type='video', maxResults=5) # Thực hiện tìm kiếm
    response = request.execute()
    results = []
    count = 1
    for item in response['items']:
        video_id = item['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        click_to_copy_link = get_click_to_copy_link(video_url)
        if click_to_copy_link:
            results.append(click_to_copy_link)
        count += 1
    markup = types.InlineKeyboardMarkup(row_width=1)
    delete_button = types.InlineKeyboardButton("Xóa tin nhắn", callback_data='delete_message')
    markup.add(delete_button)
    bot.send_message(message.chat.id, "\n\n".join(results), reply_markup=markup, parse_mode='HTML')
@bot.message_handler(commands=['ytb'])
def download_video(message):
    try:
        chat_id = message.chat.id
        video_url = message.text
        youtube_video = YouTube(video_url)
        video_title = youtube_video.title
        bot.send_message(chat_id, f"Tiêu đề: {video_title}", reply_markup=generate_config_button())
        video_info[chat_id] = {'video_url': video_url, 'video_title': video_title}
    except Exception as e:
        bot.reply_to(message, str(e))
@bot.callback_query_handler(func=lambda call: 'config' in call.data)
def configure_video(call):
    chat_id = call.message.chat.id
    video_url = video_info[chat_id]['video_url']
    video_title = video_info[chat_id]['video_title']
    youtube_video = YouTube(video_url)
    downloaded_video = youtube_video.streams.get_highest_resolution().download()
    with open(downloaded_video, 'rb') as video_file:
        bot.send_video(chat_id, video_file, supports_streaming=True)
    bot.edit_message_text(f"Tiêu đề: {video_title}\n\nVideo đã tải về",
                          chat_id=chat_id, message_id=call.message.message_id)
def generate_config_button():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton("Tải Về", callback_data='config'))
    return keyboard
@bot.message_handler(commands=['admin'])
def diggory(message):
    username = message.from_user.username
    diggory_chat = f'''
┌─────⭓ Buff DEV | BOT
│»  🔔 Xin Chào: @{username}
│»  🌐 Zalo: ...
│»  🌐 Facebook: ...
│»  🌐 Telegram : @anvipvcl
└────────────────────────
    '''
    sent_message = bot.send_message(message.chat.id, diggory_chat)

    time.sleep(20)

    bot.delete_message(chat_id=message.chat.id, message_id=sent_message.message_id)
@bot.message_handler(commands=['andzvcl'])
def anhwed(message):
    try:
        url = message.text.split()[1]
        ngocan = Options()
        ngocan.add_argument("--headless")
        ngocan.add_argument("--start-maximized")  
        ngocan.add_argument("--window-size=1050,655") 
        anvip = webdriver.Chrome(options=ngocan)
        anvip.get(url)
        annvip = '/sdcard/screenshot.png'
        anvip.save_screenshot(annvip)
        message_text = ' '.join(message.text.split()[2:])
        anvip.quit()
        with open(annvip, 'rb') as photo:
            bot.send_photo(chat_id='-1001802793115', photo=photo, caption=message_text)
    except Exception as e:
        bot.reply_to(message, f"Có lỗi xảy ra: {str(e)}")
@bot.message_handler(commands=['tt'])
def luuvideo_tiktok(message):
  if len(message.text.split()) == 1:
    sent_message = bot.reply_to(message, 'VUI LÒNG NHẬP LINK VIDEO /tiktok {link video}.')
    return
  linktt = message.text.split()[1]
  data = f'url={linktt}'
  head = {
    "Host":"www.tikwm.com",
    "accept":"application/json, text/javascript, */*; q=0.01",
    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    "user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
  }
  response = requests.post("https://www.tikwm.com/api/",data=data,headers=head).json()
  linkz = response['data']['play']
  rq = response['data']
  tieude = rq['title']
  view = rq['play_count']
  response_api = requests.get("https://www.tiktok.com/oembed?url=" + linktt)
  data = response_api.json()
  title = data.get("title")
  thumbnail_url = data.get("thumbnail_url")
  author_unique_id = data.get("author_unique_id")
  author_name = data.get("author_name")
  sent_message = bot.reply_to(message, f'Tên Tác giả: {author_name}\nID Tác giả: {author_unique_id}\n\nTiêu đề: {title}\n+ Số view: {view}')
  try:
   bot.send_video(message.chat.id, video=linkz, caption=f'Tên Tác giả: {author_name}\nID Tác giả: {author_unique_id}\n\nTiêu đề: {title}\n+ Số view: {view}',  reply_to_message_id=message.message_id, supports_streaming=True)
  except Exception as e:
   bot.reply_to(message, f'Bot hơi lag đợi t')
  bot.delete_message(chat_id=message.chat.id, message_id=sent_message.message_id)
  markup = types.InlineKeyboardMarkup()
  text = 'Video ở đây'
  button = types.InlineKeyboardButton(text='Ấn vào để xem', url=linkz)
  markup.add(button)
  bot.send_message(message.chat.id, text=text, parse_mode='Markdown', reply_markup=markup)
@bot.message_handler(commands=['sms'])
def spam_sms(message):
	if len(message.text.split()) == 1:
		sent_message = bot.reply_to(message, 'VUI LÒNG NHẬP SỐ ĐIỆN THOẠI /sms {số điện thoại}')
		time.sleep(10)
		bot.delete_message(chat_id=message.chat.id, message_id=sent_message.message_id)
		return
	user = message.from_user
	username = user.username
	username = message.from_user.username
	phone = message.text.split()[1]
	if not phone.isnumeric():
		sent_message = bot.reply_to(message, 'SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ !')
		time.sleep(5)
		bot.delete_message(chat_id=message.chat.id, message_id=sent_message.message_id)
		return
	if phone in ['113','911','114','115']:
		sent_message = bot.reply_to(message,"Ê, Bậy số này không được") 
		time.sleep(20)
		bot.delete_message(chat_id=message.chat.id, message_id=sent_message.message_id)
		return
	file_path2 = os.path.join(os.getcwd(), "sms.py")
	file_path = os.path.join(os.getcwd(), "tunglo.py")
	process = subprocess.Popen(["python", file_path2, phone])
	process = subprocess.Popen(["python", file_path, phone])
	
	processes.append(process)
	markup = types.InlineKeyboardMarkup(row_width=1)
	delete_button = types.InlineKeyboardButton("Xóa tin nhắn", callback_data='delete_message')
	markup.add(delete_button)
	bot.reply_to(message, f' 🚀 Tấn công thành công 🚀 \nBot👾:@ngocan\nSố tấn công 📱: [ {phone} ] \nNgười yêu cầu: [ @{username} ]\nLập lại ⚔️: [ 10000 ]\nGói 💸:  [ VIP ]\nThời gian chờ ⏱: [ 120000 ]\n🤖 BOT DÙNG RIÊNG: ...\nChủ sở hữu 👑: Ngọc An', reply_markup=markup)

@bot.message_handler(commands=['start'])
def account(message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
    else:
        user = message.from_user
    user_id = user.id
    profile_photos = bot.get_user_profile_photos(user_id)

    if profile_photos.photos:
        last_photo = profile_photos.photos[0][-1]
        avatar = last_photo.file_id
        username = message.from_user.username
        name = message.from_user.first_name
        user_id = message.from_user.id
        username = user.username
        name = user.first_name
        video_links = [
"https://v16m-default.akamaized.net/b746a6e481507acc0d4c6df8dcf43081/6594a1e8/video/tos/alisg/tos-alisg-pve-0037/oMCRWVFikQKiQEsI7AiyAhiBwQovBAEBfMyBD8/?a=0&ch=0&cr=0&dr=0&lr=all&cd=0%7C0%7C0%7C0&cv=1&br=1690&bt=845&bti=OHYpOTY0Zik3OjlmOm01MzE6ZDQ0MDo%3D&cs=0&ds=6&ft=XE5bCqT0mI2PD12jhYxR3wUYO-HyMeF~O5&mime_type=video_mp4&qs=0&rc=NWRoOjQ3ZjNkNzQ5OzVmOUBpMzU7bnY5cmVycDMzODgzNEA0LmM1LzJfX2MxYTFfNDMuYSM1MzFeMmRjMjVgLS1kLy1zcw%3D%3D&l=2024010217525431557C063206FCC4CEAB&btag=e00088000",
  
"https://v16m-default.akamaized.net/674838ec6173fbccd16467eb238307c6/6594a6a2/video/tos/alisg/tos-alisg-pve-0037c001/oQERjQlAtUUP6ggmnBI6fJeU5CQBggbTD2E56S/?a=0&ch=0&cr=0&dr=0&lr=all&cd=0%7C0%7C0%7C0&cv=1&br=3784&bt=1892&bti=OHYpOTY0Zik3OjlmOm01MzE6ZDQ0MDo%3D&cs=0&ds=6&ft=XE5bCqT0mmjPD12hbcxR3wU2nIZFaeF~O5&mime_type=video_mp4&qs=0&rc=Z2k2NzU3NTM3ZzM2PDpnZUBpM3k0eTw6ZnJnbjMzODczNEAuMDA2NjUvNjQxYS1hNWMwYSNkbl5ncjQwZWdgLS1kMS1zcw%3D%3D&l=20240102181308D85C77B31F545E4CCC77&btag=e00088000",

"https://v16m-default.akamaized.net/2941b747e2f53052cce84430574d5077/6594a50a/video/tos/alisg/tos-alisg-pve-0037c001/owFsqIfEBAEqAAFdwiPbASQPXiY2ByACo6WI4g/?a=0&ch=0&cr=0&dr=0&lr=all&cd=0%7C0%7C0%7C0&cv=1&br=640&bt=320&bti=OHYpOTY0Zik3OjlmOm01MzE6ZDQ0MDo%3D&cs=0&ds=6&ft=pK~tdMvt8Zmo0fP5Q94jVdiAKpFrKsd.&mime_type=video_mp4&qs=0&rc=ZGY8aDU3Ozw4OWRkZGg0ZEBpM3c0Z3Q5cnk0bzMzODczNEBhMmM2Ll4xNjUxL14vYC5iYSNfYmRgMmQ0XmRgLS1kMTFzcw%3D%3D&l=202401021806008DEBFA5A066B0BC0136C&btag=e00088000",

"https://v16m-default.akamaized.net/43e918f95d28804d965d96bcec07b41b/6594a469/video/tos/alisg/tos-alisg-pve-0037/o4llKjeEE0BbBClCI62U7BA9JVFw1UfKFgvDKE/?a=0&ch=0&cr=0&dr=0&lr=all&cd=0%7C0%7C0%7C0&cv=1&br=428&bt=214&bti=Ozk3QGo4dik3OjlmMzAuYCM6bTQ0MDo%3D&cs=0&ds=6&ft=XE5bCqT0mcRPD12kcYxR3wUQMVm~EeF~O5&mime_type=video_mp4&qs=0&rc=Omk8NDw3PDk5NjVkaTo4OEBpanh4PGs5cmg0cDMzODgzNEAtLy0tYF9jNjExNGI0LzE1YSNhL15tMmRrMl5gLS1kLzFzcw%3D%3D&l=20240102180327C0CBAE0808B79BC43F7C&btag=e00088000",
]
        random_video_url = random.choice(video_links)
        message_text = f'BOT NGỌC AN VIP \n+ Username: @{username}. \n+Tên: {name} \n+ ID: {user_id} \nCảm ơn bạn đã sử dụng bot\n-/random_face random mặt m đấy\n-/facebook tạo fb\n-/ytb + <Link video> \n-/sms + <sdt>\n-/tt <link>\n- /search <từ khóa>\n- /admin.'
        markup = types.InlineKeyboardMarkup(row_width=1)
        delete_button = types.InlineKeyboardButton("Xóa tin nhắn", callback_data='delete_message')
        markup.add(delete_button)
        bot.send_video(message.chat.id, random_video_url, caption=message_text, reply_markup=markup)
    else:
        username = message.from_user.username
        name = message.from_user.first_name
        user_id = message.from_user.id
        username = user.username
        message_text = f'BOT NGỌC AN VIP \n+ Username: @{username}. \n+Tên: {name} \n+ ID: {user_id} \nCảm ơn bạn đã sử dụng bot\n-/random_face random mặt m đấy\n-/facebook tạo fb\n-/ytb + <Link video> \n-/sms + <sdt>\n-/tt <link>\n- /search <từ khóa>\n- /admin.'
        name = user.first_name
        markup = types.InlineKeyboardMarkup(row_width=1)
        delete_button = types.InlineKeyboardButton("Xóa tin nhắn", callback_data='delete_message')
        markup.add(delete_button)
        bot.send_video(message.chat.id, random_video_url, caption=message_text, reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data == 'delete_message')
def delete_message_callback(call):
    message_id = call.message.message_id
    chat_id = call.message.chat.id
    bot.delete_message(chat_id=chat_id, message_id=message_id)
    bot.answer_callback_query(call.id, text="xóa thành côngg")
@bot.message_handler(commands=['restart'])
def restart(message):
    bot.reply_to(message, 'Bot sẽ được khởi động lại trong giây lát')
    time.sleep(2)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    print('Bot khởi động lại')
    os.system('clear')
    print("♥️♥️♥️BOT ĐANG HOẠT ĐỘNG♥️♥️♥️")
@bot.message_handler(commands=['time'])
def timecheck(message):
    if not is_bot_active:
        bot.reply_to(message, 'Bot hiện đang tắt. Vui lòng chờ khi nào được bật lại.')
        return
    current_time = time.time()
    uptime = current_time - start_time
    hours = int(uptime // 3600)
    minutes = int((uptime % 3600) // 60)
    seconds = int(uptime % 60)
    uptime_str = f'{hours} giờ, {minutes} phút, {seconds} giây'
    sent_message = bot.reply_to(message, f'Bot Đã Hoạt Động Được: {uptime_str}')
   
    time.sleep(delay_delete)
    bot.delete_message(chat_id=message.chat.id, message_id=sent_message.message_id)
@bot.message_handler(commands=['off'])
def turn_off(message):
    global is_bot_active
    is_bot_active = False
    bot.reply_to(message, 'bot off')
@bot.message_handler(commands=['on'])
def turn_on(message):
    global is_bot_active
    is_bot_active = True
    bot.reply_to(message, 'Bot on')
@bot.message_handler(commands=['status'])
def status(message):
    process_count = len(processes)
    bot.reply_to(message, f'Số quy trình đang chạy: {process_count}.')
@bot.message_handler(commands=['stop'])
def stop(message):

    bot.reply_to(message, 'Bot sẽ dừng lại trong giây lát..')
    time.sleep(2)
    bot.stop_polling()
#########END Ngọc An Vip
is_bot_active = True
if __name__ == "__main__":
    bot.infinity_polling()