import os
import datetime
import requests
from colorama import Fore

def current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def cls():
    os.system("cls")

class Colors:
    CYAN = "\033[38;5;74m"

def WebhookSpammer():
    cls()
    webhook = input(f" {Fore.RESET}[{Colors.CYAN}{current_time()}{Fore.RESET}] Webhook URL: ")
    message = input(f" {Fore.RESET}[{Colors.CYAN}{current_time()}{Fore.RESET}] Message: ")
    amount = int(input(f" {Fore.RESET}[{Colors.CYAN}{current_time()}{Fore.RESET}] Amount: "))

    for _ in range(amount):     
        try:
            response = requests.post(webhook, json={'content': message}, headers={'Content-Type': 'application/json'})
            response.raise_for_status()
            print(f" [{Colors.CYAN}{current_time()}{Fore.RESET}] Message successfully sent!")
        except requests.exceptions.HTTPError as e:
            print(f" [{Colors.CYAN}{current_time()}{Fore.RESET}] The resource is being rate limited!")
    cls()
WebhookSpammer()