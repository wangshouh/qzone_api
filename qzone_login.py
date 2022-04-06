import pickle
import time

import requests

from qq_encry import hash33


def get_qr_img(s):
    url = "https://ssl.ptlogin2.qq.com/ptqrshow?appid=549000912&e=2&l=M&s=3&d=72&v=4&daid=5&pt_3rd_aid=0"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
    }

    with open('qr.png', 'wb') as f:
        response = s.get(url, headers=headers)
        img_data = response.content
        f.write(img_data)


def get_ptqrtoken(s):
    cookies_doct = s.cookies.get_dict()
    ptqrtoken = hash33(cookies_doct['qrsig'])
    return ptqrtoken


def get_ptqrlogin(s, ptqrtoken):
    url = 'https://ssl.ptlogin2.qq.com/ptqrlogin'
    params = {
        'u1': 'https://qzs.qzone.qq.com/qzone/v5/loginsucc.html?para=izone',
        'ptqrtoken': ptqrtoken,
        'from_ui': '1',
        'aid': '549000912',
        'daid': '5'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
    }

    while True:
        time.sleep(4)
        response = s.get(url, params=params, headers=headers)
        if '登录成功' in response.text:
            break
        elif '67' in response.text:
            print('二维码正在认证')
        else:
            print('二维码未失效')
    return response.text


def get_jump_url(s, jump_text):
    jump_url = jump_text.split("'")[5]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
    }

    response = s.get(jump_url, headers=headers)
    if "<title>登录成功</title>" in response.text:
        print('cookies跳转成功')


def save_session(s):
    '''
    保存session
    '''
    with open('session.pickle', 'wb') as f:
        pickle.dump(s, f)


def login_session():
    s = requests.session()
    get_qr_img(s)
    ptqrtoken = get_ptqrtoken(s)
    jump_text = get_ptqrlogin(s, ptqrtoken)
    get_jump_url(s, jump_text)
    save_session(s)
    return s



