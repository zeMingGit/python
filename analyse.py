import re
from collections import Counter
import jieba
import os


# 第一步：读取 Markdown 文件
def load_markdown_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件 {file_path} 不存在。")
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# 第二步：清洗和预处理文本
def preprocess_text(text):
    # 去掉 Markdown 格式内容
    text = re.sub(r"\[.*?\]\(.*?\)", "", text)  # 去掉链接
    text = re.sub(r"(```.*?```)|(`.*?`)", "", text, flags=re.S)  # 去掉代码块
    text = re.sub(r"#", "", text)  # 去掉标题符号
    text = re.sub(r"\*|\-|\+|\d\.", "", text)  # 去掉列表符号
    text = re.sub(r"\s+", "", text)  # 去掉多余空白
    return text


# 第三步：分词并统计
def analyze_content(text):
    # 使用 jieba 进行分词
    words = jieba.lcut(text)

    # 去掉停用词（如“的”、“是”等）
    stop_words = set(["的", "是", "了", "在", "和", "也", "有", "就", "不", "我", "你", "他", "我们"])
    words = [word for word in words if word not in stop_words and len(word) > 1]

    # 词频统计
    word_counts = Counter(words)
    most_common = word_counts.most_common(10)

    # 总词数和独特词数
    total_words = len(words)
    unique_words = len(set(words))

    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "most_common_words": most_common,
    }


# 第四步：输出分析结果
def summarize_analysis(analysis):
    print("分析结果：")
    print(f"总词数：{analysis['total_words']}")
    print(f"独特词数：{analysis['unique_words']}")
    print("最常出现的词：")
    for word, count in analysis["most_common_words"]:
        print(f"  {word}: {count} 次")


# 主程序
try:
    # 加载 Markdown 文件
    markdown_content = load_markdown_file("./output.md")
    print("成功加载 Markdown 文件！")

    # 清洗和预处理文本
    cleaned_text = preprocess_text(markdown_content)
    print("文本清洗完成！")

    # 分析内容
    analysis = analyze_content(cleaned_text)
    summarize_analysis(analysis)

except Exception as e:
    print(f"发生错误：{e}")
