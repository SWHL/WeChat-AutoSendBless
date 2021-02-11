# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File: WeChat.py
# @Time: 2021/02/11 07:32:20
# @Author: Max
import uiautomator2 as u2
import time
import random
from tqdm import tqdm

def sleep(s):
    time.sleep(s)


def read_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        data = f.readlines()

    data = list(map(lambda x: x.rstrip('\n'), data))
    return data


data = read_txt('bless.txt')
names = read_txt('assets/friend_name.txt')

d = u2.connect('192.168.31.191')
print(d.info)

print('打开微信')
d.app_start('com.tencent.mm')

# 点击搜索
d.xpath('//*[@resource-id="com.tencent.mm:id/he6"]').click()

for name in tqdm(names):
    info = random.choice(data)

    # 输入内容
    d.xpath('//*[@resource-id="com.tencent.mm:id/fdi"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
    d.send_keys(name, clear=True)
    sleep(0.3)

    # 点击第一个人
    d.xpath('//*[@resource-id="com.tencent.mm:id/hf1"]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]').click()
    sleep(0.2)

    # 获取当前好友名称
    friend_name = d(resourceId="com.tencent.mm:id/ipt").get_text()

    # 输入内容
    d(resourceId="com.tencent.mm:id/iki").click()
    info = f"{friend_name}，过年好啊！我在这里给您拜年了，{info}[烟花][烟花][烟花]"
    d.send_keys(info, clear=True)
    sleep(0.3)

    # 点击发送
    d(resourceId="com.tencent.mm:id/ay7").click()
    sleep(0.5)

    # 点击返回
    d(resourceId="com.tencent.mm:id/un").click()
    sleep(0.3)


print('运行完毕')