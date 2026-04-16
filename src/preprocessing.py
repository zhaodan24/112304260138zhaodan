import re
from bs4 import BeautifulSoup

# 手动定义常见停用词，排除否定词
stop_words = {
    'the', 'a', 'an', 'and', 'or', 'but', 'if', 'because', 'as', 'what', 'which',
    'this', 'that', 'these', 'those', 'then', 'just', 'so', 'than', 'such', 'both',
    'through', 'about', 'for', 'is', 'of', 'while', 'during', 'to', 'from', 'in',
    'on', 'by', 'at', 'with', 'around', 'against', 'between', 'into', 'through',
    'after', 'before', 'above', 'below', 'up', 'down', 'out', 'off', 'over', 'under',
    'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why',
    'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some',
    'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very',
    's', 't', 'can', 'will', 'don', 'should', 'now'
}
negative_words = {'not', 'no', 'never', 'nor'}
stop_words = stop_words - negative_words


# 简单的词干提取函数
def simple_stemmer(word):
    suffixes = ['ing', 'ed', 'es', 's']
    for suffix in suffixes:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word


def preprocess_text(text):
    # 1. 去HTML标签
    soup = BeautifulSoup(text, 'html.parser')
    text = soup.get_text()

    # 2. 小写化
    text = text.lower()

    # 3. 标点处理：保留 ' 用于 don't 等否定形式
    text = re.sub(r'[^a-zA-Z\s\']', ' ', text)

    # 4. 分词
    words = text.split()

    # 5. 停用词处理和简单词干提取
    processed_words = []
    for word in words:
        if word in stop_words:
            continue
        word = simple_stemmer(word)
        processed_words.append(word)

    return ' '.join(processed_words)