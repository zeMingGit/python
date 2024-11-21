import re
from collections import Counter
import jieba
import os
import csv
import matplotlib.pyplot as plt
from matplotlib import rcParams
import pandas as pd
from matplotlib.font_manager import FontProperties


# 设置中文字体
def set_chinese_font():
    try:
        # 思源黑体或微软雅黑路径（根据实际系统字体路径调整）
        font_path = "C:/Windows/Fonts/simhei.ttf"  # Windows 系统
        # font_path = "/usr/share/fonts/truetype/arphic/ukai.ttc"  # Linux 系统
        # font_path = "/System/Library/Fonts/STHeiti Light.ttc"  # macOS 系统
        font = FontProperties(fname=font_path)
        rcParams['font.family'] = font.get_name()
    except Exception as e:
        print(f"无法设置中文字体，请检查字体路径是否正确：{e}")


# 第一步：读取 Markdown 文件
def load_markdown_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件 {file_path} 不存在。")
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# 第二步：清洗和预处理文本
def preprocess_text(text):
    text = re.sub(r"\[.*?\]\(.*?\)", "", text)  # 去掉链接
    text = re.sub(r"(```.*?```)|(`.*?`)", "", text, flags=re.S)  # 去掉代码块
    text = re.sub(r"#", "", text)  # 去掉标题符号
    text = re.sub(r"\*|\-|\+|\d\.", "", text)  # 去掉列表符号
    text = re.sub(r"\s+", "", text)  # 去掉多余空白
    return text


# 第三步：分词并统计
def analyze_content(text):
    words = jieba.lcut(text)
    stop_words = set(["的", "是", "了", "在", "和", "也", "有", "就", "不", "我", "你", "他", "我们"])
    words = [word for word in words if word not in stop_words and len(word) > 1]
    word_counts = Counter(words)
    most_common = word_counts.most_common(10)
    return {
        "most_common_words": most_common,
    }


# 保存结果为 CSV 文件
def save_to_csv(analysis, output_file="词频统计excel.csv"):
    with open(output_file, mode="w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["词语", "出现次数"])
        for word, count in analysis["most_common_words"]:
            writer.writerow([word, count])
    print(f"分析结果已保存到 {output_file}")


# 绘制柱状图
def plot_word_frequency(analysis, output_image="词频统计图.png"):
    words, counts = zip(*analysis["most_common_words"])
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color="skyblue")
    plt.xlabel("词语", fontsize=12)
    plt.ylabel("出现次数", fontsize=12)
    plt.title("最常出现的词频统计", fontsize=16)
    plt.xticks(rotation=45, fontsize=10)
    plt.tight_layout()
    plt.savefig(output_image)
    print(f"词频柱状图已保存为 {output_image}")


# 主程序
def main(file_path):
    set_chinese_font()  # 设置中文字体
    try:
        markdown_content = load_markdown_file(file_path)
        cleaned_text = preprocess_text(markdown_content)
        analysis = analyze_content(cleaned_text)
        save_to_csv(analysis)
        plot_word_frequency(analysis)
    except Exception as e:
        print(f"发生错误：{e}")


# 支持命令行运行
if __name__ == "__main__":
    main("./output.md")
