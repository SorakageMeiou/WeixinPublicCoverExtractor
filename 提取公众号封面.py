import requests
import re
import sys
from datetime import datetime
import pyperclip  # 更简单稳定的剪贴板库（需要安装）

def setText(aString):
    pyperclip.copy(aString)  # 复制到剪贴板

def save_image_from_url(image_url):
    try:
        print("正在下载图片...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'
        }
        response = requests.get(image_url, stream=True, headers=headers, timeout=10)
        if response.status_code == 200:
            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{current_time}.jpg"
            with open(file_name, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"图片已保存为 {file_name}")
        else:
            print("无法下载图片，服务器返回错误。")
    except Exception as e:
        print(f"下载图片时发生错误: {e}")

print("一键提取微信推送封面图\tSoraKaGe_MeiOu\n有bug联系我的QQ 3230987336\n\t文件自动会保存到程序所在的文件夹\n\t更新时日期2025/6/12\n")

# 安装依赖提示
try:
    import pyperclip
except ImportError:
    print("请先安装依赖模块：pip install pyperclip requests")
    input("输入任意字符退出")
    sys.exit()

URL = input("输入公众号链接：")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'
}

try:
    response = requests.get(URL, headers=headers, timeout=10)
    response.raise_for_status()
except Exception as e:
    print("连接失败，请检查网络或网址是否正确。", e)
    input("输入任意字符退出")
    sys.exit()

html = response.text

# 方法1：尝试匹配 JS 中的 msg_cdn_url
url_match = re.search(r'var\s+msg_cdn_url\s*=\s*"([^"]+)"', html)
if url_match:
    image_url = url_match.group(1)
else:
    # 方法2：尝试匹配 meta og:image 标签
    url_match = re.search(r'<meta property="og:image" content="(.*?)"', html)
    if url_match:
        image_url = url_match.group(1)
    else:
        print("未找到封面图链接，请确认是公众号文章页")
        input("输入任意字符退出")
        sys.exit()

print("找到封面图地址：", image_url)
setText(image_url)
save_image_from_url(image_url)

input("输入任意字符退出")