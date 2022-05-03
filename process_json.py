import json
from pathlib import Path

file_path = Path(r"./panel.json")

def getAllPackages():
    with open(file_path, "r", encoding="utf-8") as f:
        packages = json.load(f)

    packages = packages["data"]["all_packages"]
    return packages

def get_info():
    obj = getAllPackages()

    info = []

    for i in range(len(obj)):
        item = {}
        item["index"] = i
        item["id"] = obj[i]["id"]
        item["text"] = obj[i]["text"]

        info.append(item)

    j = json.dumps(info, indent=4, ensure_ascii=False)
    j = j.encode()

    with open("./packages.json", "wb") as f:
        f.write(j)

if __name__ == "__main__":
    get_info()
