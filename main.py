import json
import random
import sys
import time
from pathlib import Path

import requests

from process_json import file_path, get_info, getAllPackages
from utils import getHeaders

panel_url = "http://api.bilibili.com/x/emote/setting/panel?business=reply"
url = "https://api.bilibili.com/x/emote/user/panel/web?business=reply"

def get():
    id = 2
    desc = "tv_小电视"

    headers = getHeaders()
    resp = requests.get(url, headers=headers)
    for item in resp.json()["data"]["packages"][id]["emote"]:
        time.sleep(random.random())
        emote_title = item["text"].strip('[').rstrip(']')
        emote = requests.get(item["url"])
        with open(rf"emote/{desc}/{emote_title}.png", "wb") as f:
            f.write(emote.content)

def write():
    headers = getHeaders()
    resp = requests.get(url, headers=headers)
    # print(type(resp.json()))
    j = json.dumps(resp.json(), indent=4, ensure_ascii=False)
    j = j.encode()
    with open("test.json", "wb") as f:
        f.write(j)

def getFromLocal(index: int):
    packages = getAllPackages()

    target = packages[index]
    emote_name = target["text"]
    id = target["id"]
    print(emote_name)

    if not Path("emote").joinpath(str(id) + "_" + emote_name).exists():
        Path("emote").joinpath(str(id) + "_" + emote_name).mkdir(parents=True)

    for item in target["emote"]:
        # time.sleep(random.random())
        emote_title: str = item["text"].strip('[').rstrip(']')
        # 排除文件名中的'?'，防止生成文件时出错
        if '?' in emote_title:
            emote_title = emote_title.replace('?', '')
        
        emote = requests.get(item["url"])
        with open(rf"emote/{id}_{emote_name}/{emote_title}.png", "wb") as f:
            f.write(emote.content)

def getPanelJson():
    headers = getHeaders()
    resp = requests.get(panel_url, headers=headers)
    j = json.dumps(resp.json(), indent=4, ensure_ascii=False)
    j = j.encode()
    with open("./json/panel.json", "wb") as f:
        f.write(j)

def main(index: int, redownload_json: bool):
    if redownload_json:
        getPanelJson()
        get_info()
        print("重新生成json文件成功")

    getFromLocal(index)
    print("表情包下载完成")

if __name__ == "__main__":
    index = int(sys.argv[1])
    redownload_json = False
    if len(sys.argv) == 3 and sys.argv[2] == 'y':
        redownload_json = True
    
    main(index, redownload_json)
