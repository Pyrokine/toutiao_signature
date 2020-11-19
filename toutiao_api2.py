#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests


def get_signature(nonce, url):
    params = {
        "nonce": nonce,
        "url": url
    }
    signature = requests.get("http://127.0.0.1:8888", params=params).text
    print(signature)
    return signature


def try_sign():
    url = 'https://www.toutiao.com/i6891084759091544590/'
    userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'";

    headers = {
        "User-Agent": userAgent,
    }
    session = requests.Session()
    resp = session.get(url, headers=headers)
    # print(resp.text)
    cookie = resp.cookies.get_dict()
    if "__ac_nonce" in cookie:
        nonce = cookie["__ac_nonce"]
        print(nonce)
        signature = get_signature(nonce, url)
        Cookie = '__ac_nonce=' + nonce + '; ' + '__ac_signature=' + signature
        headers.update(
            {
                "Cookie": Cookie
            }
        )
        resp = session.get(url=url, headers=headers).text
        return resp
    else:
        return False


if __name__ == "__main__":
    result = try_sign()
    if result:
        print(result)
    else:
        print("获取失败")
