import os, threading
import sys
import colorama, random
import requests, subprocess
import json, random, string, time
sent = 0
def clear():
    os.system('cls')
colorama.init()
clear()
def header():
    print(colorama.Fore.RED + '=============================================================================================================================================================')
    header = r'''
        __  ___       __       ____       __                      _____                ___ __     _____                                          
       / / / (_)___ _/ /_     / __ \_____/ /_____ _____  ___     / ___/___  ____  ____/ (_) /_   / ___/____  ____ _____ ___  ____ ___  ___  _____
      / /_/ / / __ `/ __ \   / / / / ___/ __/ __ `/ __ \/ _ \    \__ \/ _ \/ __ \/ __  / / __/   \__ \/ __ \/ __ `/ __ `__ \/ __ `__ \/ _ \/ ___/
     / __  / / /_/ / / / /  / /_/ / /__/ /_/ /_/ / / / /  __/   ___/ /  __/ / / / /_/ / / /_    ___/ / /_/ / /_/ / / / / / / / / / / /  __/ /    
    /_/ /_/_/\__, /_/ /_/   \____/\___/\__/\__,_/_/ /_/\___/   /____/\___/_/ /_/\__,_/_/\__/   /____/ .___/\__,_/_/ /_/ /_/_/ /_/ /_/\___/_/     
            /____/                                                                                 /_/                                                                             
    '''

    print(colorama.Fore.MAGENTA + header + '\n' + colorama.Fore.RED + '=============================================================================================================================================================')
header()
print(colorama.Fore.CYAN + 'Input enter to continue.')
def options():
    _options = {'threaded' : False, 'fromfile' : False, 'random' : True}
    while True:
        if not _options['threaded']:
            print(colorama.Fore.MAGENTA + f'[1] threaded ({colorama.Fore.RED + "O" + colorama.Fore.MAGENTA})\t\t\t', end='')
        elif _options['threaded']:
            print(colorama.Fore.MAGENTA + f'[1] threaded ({colorama.Fore.GREEN + "O" + colorama.Fore.MAGENTA})\t\t\t',end='')
        if not _options['random']:
            print(colorama.Fore.MAGENTA + f'[2] random sticker ({colorama.Fore.RED + "O" + colorama.Fore.MAGENTA})\t\t\t',end='')
        elif _options['random']:
            print(colorama.Fore.MAGENTA + f'[2] random sticker ({colorama.Fore.GREEN + "O" + colorama.Fore.MAGENTA})\t\t\t',end='')
        if not _options['fromfile']:
            print(colorama.Fore.MAGENTA + f'[3] from file ({colorama.Fore.RED + "O" + colorama.Fore.MAGENTA})')
        if _options['fromfile']:
            print(colorama.Fore.MAGENTA + f'[3] from file ({colorama.Fore.GREEN + "O" + colorama.Fore.MAGENTA})')
        optionsinput = input('\n(?)>')
        clear()
        header()
        print(colorama.Fore.CYAN + 'Input enter to continue.')
        if optionsinput == '1':
            if _options['threaded']:
                _options['threaded'] = False
            elif not _options['threaded']:
                _options['threaded'] = True
        if optionsinput == '2':
            if _options['random']:
                _options['random'] = False
            elif not _options['random']:
                _options['random'] = True
        if optionsinput == '3':
            if _options['fromfile']:
                _options['fromfile'] = False
            elif not _options['fromfile']:
                _options['fromfile'] = True
        if optionsinput == '':
            return _options
        if optionsinput.lower() == 'enter':
            return _options
_options = options()
def getdata():
    if _options['fromfile']:
        if os.path.exists(r'.\idlist.csv'):
            pass
        else:
            open(r'.\idlist.csv', 'x')

    clear()
    header()
    message = input(colorama.Fore.CYAN + 'Input message: ' + colorama.Fore.GREEN)
    print(colorama.Fore.RED + '\n=======================================\n')
    if not _options['fromfile']:
        recipient_identity = input(colorama.Fore.CYAN + 'Input recipient identity: ' + colorama.Fore.GREEN)
        print(colorama.Fore.RED + '\n=======================================\n')
    else:
        data = open(r'.\idlist.csv').read()
        data = data.splitlines()
        for string in data:
            if string == '':
                data.remove('')
        if len(data) == 0:
            quit('please put at least 1 recipient identity in idlist.csv')
        recipient_identity = data
    if _options['threaded']:
        thread_amount = input(colorama.Fore.CYAN + 'Input thread amount: ' + colorama.Fore.GREEN)
        print(colorama.Fore.RED + '\n=======================================\n')
    else:
        thread_amount = None
    if not _options['random']:
        custom_sticker = input(colorama.Fore.CYAN + 'Input custom sticker value: ' + colorama.Fore.GREEN)
        print(colorama.Fore.RED + '\n=======================================\n')
    else:
        custom_sticker = None
    datalist = {"message" : message, "recipient_identity" : recipient_identity, "thread_amount" : thread_amount, "custom_sticker" : custom_sticker}
    return datalist
    # message = 'hi'
    #author_shadow_token = 'a5f367a7-f909-4dec-b26c-74f5eac361cd'
    #reply_post_id = 'dffff61d-2281-44dc-a14d-e90ca561e5e2'
    #sticker_id = '778b025a-3506-4a8e-b094-a04b0f915327'
    #recipient_identity = 'f8100df0-64af-4e27-9a2b-8c1f54e64209'

thinglist = [
"afcbd83d-3246-4bc3-85d5-9e12a78a5583",
"bc5fa35b-ed8f-41ae-8ab7-ac9cdc9a8a92",
"7b931a0f-4851-4055-bc1a-f92fb35c5b1c",
"e98d7864-8d81-47ea-ae56-6985c7e1c287",
"f9a31b88-3e55-43ee-a5ae-b5528a978942",
"7d0cb5c8-5799-435b-a88a-c216da7403ad",
"73435224-c222-4c0e-8b80-56920148b6b9",
"5566df4d-c026-4721-9629-d6be8df5276c",
"19f21547-0b6f-44ea-b968-58f97c85dab3",
"f406d572-fe8f-4af7-ae1a-da109c60b0c4",
"16ed4963-d0c8-465b-9693-db5357bd0028",
"9b619faf-d200-4e6c-b0e4-8180dbad97a0",
"9df93fcc-4b99-4aee-8916-f1cf2ca1e9bb",
"fdb4ddf7-a0f8-4dde-90de-281fb100a9bb"]
def send_message(datalist):
    global sent
    while True:
        try:
            try:
                if _options['random']:
                    sticker = random.choice(thinglist)
                else:
                    sticker = datalist['custom_sticker']
                if _options['fromfile']:
                    for _id in datalist['recipient_identity']:
                        head = {'app-id': 'c2ad997f-1bf2-4f2c-b5fd-83926e8f3c65', 'app-version': '1.0'}
                        data = {"recipient_identity": {"type": "id", "value": _id},
                                "type": "sendit.post-type:question-and-answer-v1", "data": {"question": datalist['message']},
                                "ext_data": {"sticker_id": sticker,
                                             "author_shadow_token": 'a5f367a7-f909-4dec-b26c-74f5eac361cd'}, "timer": 0}
                        response = requests.post(url='https://api.getsendit.com/v1/posts', json=data, headers=head).text
                        status = json.loads(response)['status']
                        if status == 'success':
                            sent += 1
                            print(colorama.Fore.GREEN + '\r' + f'success! message {sent}      ', end='')
                        elif status == 'failure':
                            print(colorama.Fore.RED + '\r' + f'message failed to send.', end='')
                else:
                    head = {'app-id': 'c2ad997f-1bf2-4f2c-b5fd-83926e8f3c65', 'app-version': '1.0'}
                    data = {"recipient_identity": {"type": "id", "value": datalist['recipient_identity']},
                            "type": "sendit.post-type:question-and-answer-v1", "data": {"question": datalist['message']},
                            "ext_data": {"sticker_id": sticker,
                                         "author_shadow_token": 'a5f367a7-f909-4dec-b26c-74f5eac361cd'}, "timer": 0}
                    response = requests.post(url='https://api.getsendit.com/v1/posts', json=data, headers=head).text
                    status = json.loads(response)['status']
                    if status == 'success':
                        sent += 1
                        print(colorama.Fore.GREEN + '\r' + f'success! message {sent}      ', end='')
                    elif status == 'failure':
                        print(colorama.Fore.RED + '\r' + f'message failed to send.', end='')
                    #print(status + '\n')
            except KeyboardInterrupt:
                print(colorama.Fore.BLUE + '\nexiting!!')
                quit()
        except:
            pass
if _options['threaded']:
    try:
        datalist = getdata()
        threadamount = int(datalist['thread_amount'])
        threads = []
        for i in range(threadamount):
            t = threading.Thread(target=send_message, args=[datalist])
            t.daemon = True
            threads.append(t)
        for i in range(threadamount):
            threads[i].start()
        for i in range(threadamount):
            threads[i].join()
    except KeyboardInterrupt:
        print(colorama.Fore.BLUE + '\nexiting!!')
        quit()
elif not _options['threaded']:
    try:
        datalist = getdata()
        send_message(datalist=datalist)
    except KeyboardInterrupt:
        print(colorama.Fore.BLUE + '\nexiting!!')
        quit()
