import requests
import json
# https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5
# https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign

# 分析历史数据
url_history = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign"

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.114 Safari/537.36 '
    }
# 历史数据
# resp = requests.get(url_history)
# # 获取页面json数据
# json_data = resp.text
# print(json_data)
#
# # 将json字符串转换为字典
# d_data = json.loads(json_data)
# print(d_data['data'])
# data_history = json.loads(d_data['data'])
# for item in data_history.keys():
#     print(data_history[item])

#details详细数据
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
resp = requests.get(url,headers)
json_data = resp.text
# print(json_data)
# 转换为字典
dict_data = json.loads(json_data)
data = json.loads(dict_data['data'])
for item in data.keys():
    print(item)
    # print(data[item])
for i in data['areaTree'][0]['children']:
    print(i)