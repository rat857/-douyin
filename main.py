import requests
import json
import re
from lxml import html

etree = html.etree
a = input('要解析的视频链接：')
a1 = re.split('复制', a)[0]
a2 = re.split("http", a1)[-1]
url11 = 'http' + a2
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
}
response11 = requests.get(url=url11, headers=header, allow_redirects=False).text

# with open('./1.html', 'w', encoding='utf-8') as fp:
#     fp.write(response11)
tree = etree.HTML(response11)
print(tree)
urlx = tree.xpath("/html/body/a/@href")[0]
response12 = requests.get(url=urlx, headers=header, allow_redirects=False).text
print(response12)
# with open('./1.html','w',encoding='utf-8') as fp:
#     fp.write(response1)
res = re.split('"', response12)[1]  # 视频直链1
print(res)
res1 = re.split('\?', res)[0]
print(res1)
res2 = re.split('/', res1)[-1]  # 获取到视频的item_ids
print(type(res2))
url = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/'
peram = {
    'item_ids': res2
}
response = requests.get(url=url, params=peram, headers=header)
print(response.status_code)
list_data = json.loads(response.text)
print(type(list_data))
# fp = open('./text.json', 'w', encoding='utf-8')
# json.dump(list_data, fp=fp, ensure_ascii=False)
# print("over")
ywama = str(list_data['item_list'][0]['video']['play_addr']['uri'])  # 从json中筛选视频数据的id号
name = str(list_data['item_list'][0]['desc'])
print("视频的名字是：" + name)
vi_url0 = 'https://aweme.snssdk.com/aweme/v1/play/?video_id=' + ywama
response1 = requests.get(url=vi_url0, headers=header).content  # 视频数据
vi_name = name  # 视频名字
vi_path = "/root/视频/" + vi_name + ".mp4"  # 视频路径
with open(vi_path, 'wb') as fp:
    fp.write(response1)
    print("ok")
