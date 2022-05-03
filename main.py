import json
import random
import sys
import time
from pathlib import Path

import requests

from process_json import file_path, get_info, getAllPackages

panel_url = "http://api.bilibili.com/x/emote/setting/panel?business=reply"
url = "https://api.bilibili.com/x/emote/user/panel/web?business=reply"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32",
    "Cookie": ""
}

def get():
    id = 2
    desc = "tv_小电视"

    resp = requests.get(url, headers=headers)
    for item in resp.json()["data"]["packages"][id]["emote"]:
        time.sleep(random.random())
        emote_title = item["text"].strip('[').rstrip(']')
        emote = requests.get(item["url"])
        with open(rf"emote/{desc}/{emote_title}.png", "wb") as f:
            f.write(emote.content)

def write():
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
    print(emote_name)

    if not Path("emote").joinpath(emote_name).exists():
        Path("emote").joinpath(emote_name).mkdir(parents=True)

    for item in target["emote"]:
        time.sleep(random.random())
        emote_title = item["text"].strip('[').rstrip(']')
        emote = requests.get(item["url"])
        with open(rf"emote/{emote_name}/{emote_title}.png", "wb") as f:
            f.write(emote.content)

def getPanelJson():
    resp = requests.get(panel_url, headers=headers)
    j = json.dumps(resp.json(), indent=4, ensure_ascii=False)
    j = j.encode()
    with open("panel.json", "wb") as f:
        f.write(j)

if __name__ == "__main__":
    # getPanelJson()
    getFromLocal(int(sys.argv[1]))
