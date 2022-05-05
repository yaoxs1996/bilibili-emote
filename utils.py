import json

def getHeaders():
    with open("./json/headers.json", "r") as f:
        headers = json.load(f)

    # print(type(headers))
    # print(headers)
    return headers

if __name__ == "__main__":
    getHeaders()