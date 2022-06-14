import requests 


red = "\033[1;31;40m"
green = '\033[1;32;40m'
Blue = "\033[1;36;40m"

def login():
    global password,get_session

    username = input(f"\n\n{Blue} Enter your username: ")
    password = input(f"{Blue} Enter your password: ")

    url = 'https://www.instagram.com/accounts/login/ajax/'

    headers = {
            
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '318',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'mid=Yb4voQAEAAHCocWa1qeJraP41MzP; ig_did=28116676-A0B3-40A1-A377-7141B84DAA08; ig_nrcb=1; csrftoken=Y14ejqrGAGmAxdVHCkKY4VO7x1f6YFsA',
        'origin':'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sect-ch-ua-platform': '"Linux"',
        'sec-fetch-des': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'x-asbd-id': '198387',
        'x-csrftoken': 'Y14ejqrGAGmAxdVHCkKY4VO7x1f6YFsA',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR26etHUEAB4w6eC8m0dG-uyjPmXLHyCNOyhc77EG2zqG_f6',
        'x-instagram-ajax': '05272981ffad',
        'x-requested-with': 'XMLHttpRequest'

        }
     
    data={
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
        'username': username,
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'stopDeletionNonce': '',
        'trustedDeviceRecords': '{}'
        }

    req_login = requests.post(url=url,headers=headers,data=data)

    if '"authenticated":true' in req_login.text:
        print("logged in")
        get_session = req_login.cookies['sessionid']
        Banned_sleep()
    
    elif '"authenticated"::false' in req_login.text:
        print(f"\n{red}Wrong password")
        login()

    else:
        print(req_login.text)
        login()


def Banned_sleep():

    url = 'https://www.instagram.com/accounts/remove/request/temporary/'
    headers = {

        'Host': 'www.instagram.com',
        'Cookie': f"csrftoken=oXWT54yZG7ClzyeSbTpKBcnnaJT13xoO; mid=YVZDKQAEAAFiUWJ0q0cAgrZKTUsc; ig_did=896C69E0-6495-461F-A014-0167FBD13E9B; ig_nrcb=1; sessionid={get_session}",
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': '*/*',
        'Accept-Language': 'ar-DZ,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'X-Csrftoken': 'oXWT54yZG7ClzyeSbTpKBcnnaJT13xoO',
        'X-Instagram-Ajax': '05272981ffad',
        'X-Ig-App-Id': '936619743392459',
        'X-Asbd-Id': '198387',
        'X-Ig-Www-Claim': 'hmac.AR26etHUEAB4w6eC8m0dG-uyjPmXLHyCNOyhc77EG2zqG5pn',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '235',
        'Origin': 'https://www.instagram.com',
        'Referer': 'https://www.instagram.com/accounts/remove/request/temporary/',
        'Te': 'trailers'
        }
    
    data={
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
        'deletion-reason': 'need-break'
        }

    sent = requests.post(url,headers=headers,data=data).text

    if '"status":"ok"' in sent:
        print(f'{green}[+] Your Account Has Been temporarily')


    else:
        print(red+'\n\n[!] Sorry, you can only disable your account once a week. Try again in a few days.')

if __name__ == "__main__":
    login()
