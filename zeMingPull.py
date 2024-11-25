from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager
import html2text
from rich.console import Console
from rich.text import Text
from rich.progress import Progress
import pyfiglet
# import analyse

# 创建 rich 控制台
console = Console()
# 打印 zeMing 图案
# console.print("[bold magenta]zeMing[/bold magenta]", style="bold magenta")
ascii_art = pyfiglet.figlet_format("zeMing", font="block")  # 你可以尝试不同的字体，如 "slant", "block", "starwars" 等
console.print(ascii_art, style="bold cyan on black", justify="center")

# 配置 Chrome 选项
chrome_options = Options()
chrome_options.add_argument('--headless')  # 无头模式
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# 使用 ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 定义一个辅助函数，用于执行并处理异常
def safe_execute(description, func, *args, **kwargs):
    """执行函数并处理异常，打印描述信息和错误信息。"""
    try:
        console.print(f"[cyan]{description}[/cyan]")
        return func(*args, **kwargs)
    except Exception as e:
        console.print(f"[red]{description} 时发生错误: {e}[/red]")
        return None

# 获取 URL 和 class 选择
url = console.input("请输入目标网页的 URL: ")
class_options = [
    "rich_media_content",
    "article_content",
    "text_area"
]

class_choice = console.input(f"请选择 class (可选值: {', '.join(class_options)}): ")

if class_choice not in class_options:
    console.print("[red]无效的 class 选择，使用默认值 'rich_media_content'[/red]")
    class_choice = "rich_media_content"

# 打开浏览器并执行操作
try:
    # 加载页面
    safe_execute(f'开始获取地址: {url}', driver.get, url)

    # 等待页面加载完成
    time.sleep(2)
    console.print('[green]页面加载完成！[/green]')

    # 提取文章内容
    content_element = safe_execute('提取文章内容', driver.find_element, By.CLASS_NAME, class_choice)
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
        safe_execute('写入文件', open, "output.md", "w", encoding="utf-8").write(markdown_content)
        console.print('[green]写入文件成功！[/green]')
    else:
        console.print("[yellow]由于转换内容失败，跳过写入文件。[/yellow]")

    # 分析文件
    # analyse.main('./output.md')

finally:
    driver.quit()
    console.print('[yellow]关闭浏览器。请手动关闭 CMD 窗口。[/yellow]')
