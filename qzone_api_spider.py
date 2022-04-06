import json
import os
import pickle
import re

import requests

from qq_encry import gtk
from qzone_login import get_sessions

def get_qzonetoken(s):
    url = "https://h5.qzone.qq.com/mqzone/index"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Android 11; Mobile; rv:83.0) Gecko/83.0 Firefox/83.0'
    }

    response = s.get(url, headers=headers)
    qzonetoken = re.findall(r"[A-Za-z0-9]{96}", response.text)[0]

    return qzonetoken


def get_gtk(s):
    cookies_dict = s.cookies.get_dict()
    gtk_num = gtk(cookies_dict['p_skey'])
    return gtk_num


def get_active_feeds(s, qzonetoken, gtk_num):
    url = f"https://h5.qzone.qq.com/webapp/json/mqzone_feeds/getActiveFeeds?qzonetoken={qzonetoken}&g_tk={gtk_num}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Android 11; Mobile; rv:83.0) Gecko/83.0 Firefox/83.0',
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://h5.qzone.qq.com',
        'Referer': 'https://h5.qzone.qq.com/mqzone/index'
    }

    response = s.post(url, headers=headers)
    response_json = json.loads(response.text)

    with open('example.json', 'w') as f:
        json.dump(response_json, f)

s = get_sessions()
qzonetoken = get_qzonetoken(s)
gtk_num = get_gtk(s)
get_active_feeds(s, qzonetoken, gtk_num)