from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager
import html2text

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


# 定义一个辅助函数，用于执行并处理异常
def safe_execute(description, func, *args, **kwargs):
    """执行函数并处理异常，打印描述信息和错误信息。"""
    try:
        print(description)
        return func(*args, **kwargs)
    except Exception as e:
        print(f"{description} 时发生错误: {e}")
        return None


try:
    # 加载页面
    url = "https://mp.weixin.qq.com/s/gXPH_C9Ld8rtjmcwGz0uuA"
    safe_execute(f'开始获取地址: {url}', driver.get, url)

    # 等待页面加载完成
    time.sleep(2)
    print('页面加载完成！')

    # 提取文章内容
    content_element = safe_execute('提取文章内容', driver.find_element, By.CLASS_NAME, 'rich_media_content')
    content_html = content_element.get_attribute('outerHTML') if content_element else None

    # 转换为 Markdown
    if content_html:
        markdown_converter = html2text.HTML2Text()
        markdown_converter.ignore_links = False  # 保留链接
        markdown_converter.backquote_code_style = True  # 转换 code 代码
        markdown_content = safe_execute('转换为 Markdown', markdown_converter.handle, content_html)
    else:
        markdown_content = None

    # 写入文件
    if markdown_content:
        safe_execute('写入文件', open, "output.md", "w", encoding="utf-8").write(markdown_content)
        print('写入文件成功！')
    else:
        print("由于转换内容失败，跳过写入文件。")

finally:
    driver.quit()
    print('关闭浏览器')
