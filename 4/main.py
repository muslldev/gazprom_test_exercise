import json


def parser(data:str):
    dict = json.loads(data)
    outData = {}

    for key in dict.keys():
        outData[key]= '://'.join(dict.get(key))

    return outData

inData = '{"one": ["http", "yandex.ru"], "two": ["https", "google.com"]}'

print(parser(inData))