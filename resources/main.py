# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File: main.py
# @Author: SWHL
# @Contact: liekkaskono@163.com
import os
import random
import time

import numpy as np
import pyautogui
import pyperclip
from tqdm import tqdm
from PIL import ImageGrab

from rapidocr import TextSystem


det_model_path = "resources/models/ch_PP-OCRv2_det_infer.onnx"
cls_model_path = "resources/models/ch_ppocr_mobile_v2.0_cls_infer.onnx"
rec_model_path = "resources/models/ch_ppocr_mobile_v2.0_rec_infer.onnx"
dict_path = "resources/ppocr_keys_v1.txt"

text_sys = TextSystem(det_model_path,
                      rec_model_path,
                      cls_model_path,
                      dict_path)


def read_txt(txt_path: str) -> list:
    with open(txt_path, 'r', encoding='utf-8') as f:
        data = list(map(lambda x: x.rstrip('\n'), f))
    return data


class WeChat(object):
    def __init__(self, wechat_path):
        self.wechat_path = wechat_path
        self._open_wechat()
        self._get_ocr()

    def _open_wechat(self):
        pyautogui.hotkey('win', 'd')
        file = os.popen(self.wechat_path)
        file.close()
        time.sleep(2)

    def _get_ocr(self):
        result_boxes = None
        dt_boxes, rec_res = text_sys(np.array(ImageGrab.grab()))
        for dt_box, rec in zip(dt_boxes, rec_res):
            if rec[0].__contains__('搜索'):
                result_boxes = dt_box

        self.x = np.mean(result_boxes[:, 0])
        self.y = np.mean(result_boxes[:, 1])

    def send_msg_obj(self, name):
        print('点击搜索')
        pyautogui.moveTo(self.x, self.y)
        pyautogui.click(self.x, self.y)
        time.sleep(1)

        print('输入姓名')
        pyperclip.copy(name)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        print('点击搜素')
        pyautogui.hotkey('enter')
        time.sleep(2)


if __name__ == '__main__':
    wechat = WeChat(r'"F:\WeChat\WeChat.exe"')

    message_list = read_txt('info.txt')
    person_list = read_txt('bless_names.txt')
    for one_name in tqdm(person_list):
        # 选择人
        wechat.send_msg_obj(one_name)

        # 生成文案
        random_one = random.choice(message_list)
        random_one = f'{one_name}\n{random_one}'

        print(random_one)
        # wechat.send_msg(random_one)
