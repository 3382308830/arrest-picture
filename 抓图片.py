import requests
import re
import os
# 正则表达式->找到对应的字符串内容
# 反爬虫->反反爬
# UAjiance-检测是否正常请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57'
}
name = input('请输入你要采集的数据内容：')
url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + name
try:
    response = requests.get(url, headers=headers)  # response是拿到的页面数据
    html = response.content.decode()
    a = re.findall('"objURL":"(.*?)",', html)
    num = 0
    for b in a:  # 把a里面的链接拿出来放到b里面
        num += 1
        img = requests.get(b)
        with open('./img/' + name + str(num) + '.jpg', 'wb') as f:  # 注意这里是'wb'模式，因为我们要写入二进制数据
            f.write(img.content)
            print('--正在下载第' + str(num) + '张图片数据--')
except requests.exceptions.RequestException as e:  # 处理请求异常
    print('请求失败：', e)
except UnicodeDecodeError as e:  # 处理解码异常
    print('解码失败：', e)
finally:
    os.makedirs('./img/', exist_ok=True)  # 如果目录不存在，创建它