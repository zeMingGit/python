import re
from collections import Counter
import jieba
import jieba.analyse
import jieba.posseg as pseg
import os
import csv
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import snownlp


# 设置中文字体
def set_chinese_font():
    try:
        font_path = "C:/Windows/Fonts/simhei.ttf"  # 根据实际系统设置
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


# 第三步：词频统计
def analyze_content(text):
    words = jieba.lcut(text)
    stop_words = set(["的", "是", "了", "在", "和", "也", "有", "就", "不", "我", "你", "他", "我们"])
    words = [word for word in words if word not in stop_words and len(word) > 1]
    word_counts = Counter(words)
    most_common = word_counts.most_common(10)
    return {
        "most_common_words": most_common,
        "word_counts": word_counts
    }


# 文本结构统计
def text_structure_analysis(text):
    num_chars = len(text)  # 字数
    num_words = len(jieba.lcut(text))  # 词数
    num_sentences = len(re.findall(r"[。！？]", text))  # 句子数
    num_paragraphs = len(text.split("\n"))  # 段落数
    return {
        "num_chars": num_chars,
        "num_words": num_words,
        "num_sentences": num_sentences,
        "num_paragraphs": num_paragraphs,
        "average_words_per_sentence": num_words / num_sentences if num_sentences else 0
    }


# 情感分析和关键词提取
def semantic_analysis(text):
    # 提取关键词
    keywords = jieba.analyse.extract_tags(text, topK=10, withWeight=True)
    # 情感分析
    sentiment = snownlp.SnowNLP(text).sentiments
    return {
        "keywords": keywords,
        "sentiment_score": sentiment
    }


# 词性分布统计
def pos_analysis(text):
    words = pseg.cut(text)
    pos_counter = Counter(word.flag for word in words)
    return dict(pos_counter)


# 主题建模
def topic_modeling(text, n_topics=5):
    vectorizer = CountVectorizer()
    text_matrix = vectorizer.fit_transform([text])
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=0)
    lda.fit(text_matrix)

    topics = []
    for idx, topic in enumerate(lda.components_):
        top_words = [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]]
        topics.append({"topic": idx + 1, "keywords": top_words})

    return topics


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


# 生成词云
def generate_wordcloud(text, output_image="词云图.png"):
    wordcloud = WordCloud(font_path="C:/Windows/Fonts/simhei.ttf", background_color="white").generate(text)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(output_image)
    print(f"词云图已保存为 {output_image}")


# 主程序
def main(file_path):
    set_chinese_font()  # 设置中文字体
    try:
        markdown_content = load_markdown_file(file_path)
        cleaned_text = preprocess_text(markdown_content)

        # 分析内容
        analysis = analyze_content(cleaned_text)
        structure = text_structure_analysis(cleaned_text)
        semantic = semantic_analysis(cleaned_text)
        pos_stats = pos_analysis(cleaned_text)
        topics = topic_modeling(cleaned_text)

        # 保存和绘图
        save_to_csv(analysis)
        plot_word_frequency(analysis)
        generate_wordcloud(cleaned_text)

        # 打印分析结果
        print("结构统计:", structure)
        print("关键词:", semantic["keywords"])
        print("情感评分:", semantic["sentiment_score"])
        print("词性分布:", pos_stats)
        print("主题:", topics)

    except Exception as e:
        print(f"发生错误：{e}")


# 支持命令行运行
if __name__ == "__main__":
    main("./output.md")
