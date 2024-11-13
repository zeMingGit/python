from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager


# 配置 Chrome 选项
chrome_options = Options()
chrome_options.add_argument('--headless')  # 无头模式
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# 使用 ChromeDriver
service = Service(ChromeDriverManager().install()) # 替换为你的 chromedriver 路径
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    url = "https://mp.weixin.qq.com/s/TGdp5Eyf86YJHcG4lTQDDw"
    driver.get(url)

    # 等待页面加载完成
    time.sleep(2)

    # 提取文章标题和内容
    title = driver.find_element(By.TAG_NAME, 'h1').text
    content = driver.find_element(By.CLASS_NAME, 'rich_media_content').text

    print("标题:", title)
    print("内容:", content)

finally:
    driver.quit()
