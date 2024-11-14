from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager
import html2text
import re

# 需要将html2text源码进行替换 https://github.com/Alir3z4/html2text/issues/386
# 配置 Chrome 选项
chrome_options = Options()
chrome_options.add_argument('--headless')  # 无头模式
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# 使用 ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
print('打开浏览器')

try:
    url = "https://mp.weixin.qq.com/s/gXPH_C9Ld8rtjmcwGz0uuA"
    driver.get(url)

    print('开始获取地址:')
    # 等待页面加载完成
    time.sleep(2)
    print('加载完成！')

    # 提取文章内容
    print('提取文章内容:')
    content_element = driver.find_element(By.CLASS_NAME, 'rich_media_content')
    content_html = content_element.get_attribute('outerHTML')
    print('提取文章内容完成！')

    # 使用 html2text 转换为 Markdown
    print('转换为 Markdown:')
    markdown_converter = html2text.HTML2Text()
    markdown_converter.ignore_links = False  # 如果需要保留链接可以设置为False
    markdown_converter.backquote_code_style = True  # 转换code代码
    markdown_content = markdown_converter.handle(content_html)
    print('转换成功！')

    # 写入文件
    with open("output.md", "w", encoding="utf-8") as file:
        file.write(markdown_content)
    print('写入文件成功！')

finally:
    driver.quit()
