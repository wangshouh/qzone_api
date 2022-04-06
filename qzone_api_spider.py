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


def get_active_feeds(s, qzonetoken, gtk_num, n=1):
    url = f"https://h5.qzone.qq.com/webapp/json/mqzone_feeds/getActiveFeeds?qzonetoken={qzonetoken}&g_tk={gtk_num}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Android 11; Mobile; rv:83.0) Gecko/83.0 Firefox/83.0',
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://h5.qzone.qq.com',
        'Referer': 'https://h5.qzone.qq.com/mqzone/index'
    }
    for i in range(n):
        if i == 0:
            response = s.post(url, headers=headers)
            response_json = json.loads(response.text)

            payload = response_json["data"]["attachinfo"]
            feeds_list = response_json["data"]["vFeeds"]
        else:
            response = s.post(url, headers=headers, data=payload)
            response_json = json.loads(response.text)
            payload = response_json["data"]["attachinfo"]
            feeds_list += response_json["data"]["vFeeds"]

    return feeds_list


def get_person_feeds(s, gtk_num, uin, qzonetoken, n=1):
    feeds_list = []

    for i in range(n):
        url = 'https://h5.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?'
        params = {
            "sort": 0,
            "start": 0,
            "num": 20,
            "cgi_host": "http://taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6",
            "replynum": 100,
            "callback": "_preloadCallback",
            "code_version": 1,
            "inCharset": "utf-8",
            "outCharset": "utf-8",
            "notice": 0,
            "format": "jsonp",
            "need_private_comment": 1,
            "g_tk": gtk_num,
            "qzonetoken": qzonetoken,
            "uin": uin,
            "pos": 20
        }

        response = s.get(url, params=params)
        response_str = re.findall(
            '^_preloadCallback\((.*?)\);$', response.text)[0]
        response_json = json.loads(response_str)
        feeds_list += response_json["msglist"]
    with open("test_data3.json", "w", encoding="utf-8") as f:
        json.dump(feeds_list, f)
