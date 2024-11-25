import argparse
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import html2text
# import analyse
from rich.console import Console
from rich.progress import Progress

# 初始化 Rich Console
console = Console()

# 设置命令行参数
parser = argparse.ArgumentParser(description="从网页提取内容并保存为 Markdown 文件")
parser.add_argument('-u', '--url', type=str, required=True, help="目标网页的 URL")
parser.add_argument('-o', '--output', type=str, default="output.md", help="保存 Markdown 文件的路径")
args = parser.parse_args()

url = args.url
output_file = args.output

# 配置 Chrome 选项
chrome_options = Options()
chrome_options.add_argument('--headless')  # 无头模式
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# 使用 ChromeDriver
console.log("[bold green]正在初始化 ChromeDriver...")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 定义一个辅助函数，用于执行并处理异常
def safe_execute(description, func, *args, **kwargs):
    """执行函数并处理异常，打印描述信息和错误信息。"""
    try:
        console.log(f"[cyan]{description}...")
        return func(*args, **kwargs)
    except Exception as e:
        console.log(f"[red]{description} 时发生错误: {e}")
        return None

try:
    # 加载页面
    console.log(f"[bold green]开始访问 URL: [blue]{url}")
    safe_execute(f'访问 {url}', driver.get, url)

    # 等待页面加载完成
    with Progress() as progress:
        task = progress.add_task("[cyan]等待页面加载...", total=2)
        for _ in range(2):
            time.sleep(1)
            progress.update(task, advance=1)
    console.log("[bold green]页面加载完成！")

    # 提取文章内容
    content_element = safe_execute('提取文章内容', driver.find_element, By.CLASS_NAME, 'rich_media_content')
    content_html = content_element.get_attribute('outerHTML') if content_element else None

    # 转换为 Markdown
    if content_html:
        markdown_converter = html2text.HTML2Text()
        markdown_converter.mark_code = True
        markdown_converter.ignore_links = False  # 保留链接
        markdown_converter.backquote_code_style = True  # 转换 code 代码
        markdown_content = safe_execute('转换为 Markdown', markdown_converter.handle, content_html)
    else:
        markdown_content = None

    # 写入文件
    if markdown_content:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        console.log(f"[bold green]Markdown 内容已保存到文件: [blue]{output_file}")
    else:
        console.log("[bold red]由于转换内容失败，跳过写入文件。")

    # 分析文件
    console.log("[bold green]开始分析文件...")
    # analyse.main(output_file)
    console.log("[bold green]文件分析完成！")

finally:
    driver.quit()
    console.log("[bold yellow]浏览器已关闭。")
