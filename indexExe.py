import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import html2text
from rich.console import Console
from rich.progress import Progress
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

# 初始化 Rich Console
console = Console()

# 欢迎语句
console.print("""
[bold green]欢迎使用 zeMing 网页内容爬取工具！[/bold green]
[cyan]您可以通过此工具爬取指定网页内容并保存为 Markdown 文件。[/cyan]
""")

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

# 提供 class 选项
class_options = ["rich_media_content", "article-content", "main-content"]
class_completer = WordCompleter(class_options, ignore_case=True)

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
    while True:
        # 获取目标 URL
        url = prompt("请输入目标网页的 URL: ")

        # 获取 class 名称
        console.print("\n[bold cyan]请选择要提取的内容的 class 名称:[/bold cyan]")
        class_name = prompt("输入或选择 class 名称: ", completer=class_completer)

        # 设置输出文件名
        output_file = prompt("请输入输出文件路径 (默认 output.md): ", default="output.md")

        # 开始访问 URL
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
        content_element = safe_execute('提取文章内容', driver.find_element, By.CLASS_NAME, class_name)
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

        # 询问是否继续
        continue_choice = prompt("\n[bold yellow]是否继续爬取其他网页内容？(y/n): [/bold yellow]", default="y").lower()
        if continue_choice != 'y':
            console.log("[bold green]感谢使用 zeMing 工具！再见！")
            break

finally:
    driver.quit()
    console.log("[bold yellow]浏览器已关闭。")
