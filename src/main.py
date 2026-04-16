import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import time

from preprocessing import preprocess_text

# 数据文件路径
labeled_train_path = r'labeledTrainData.tsv'
test_path = r'testData.tsv'
unlabeled_train_path = r'unlabeledTrainData.tsv'


# 读取数据
def load_data()
    print(Loading
    data...)
    train = pd.read_csv(labeled_train_path, sep='t', quoting=3)
    test = pd.read_csv(test_path, sep='t', quoting=3)
    unlabeled_train = pd.read_csv(unlabeled_train_path, sep='t', quoting=3)
    print(fTrain
    shape
    {train.shape})
    print(fTest
    shape
    {test.shape})
    print(fUnlabeled
    train
    shape
    {unlabeled_train.shape})
    return train, test, unlabeled_train


# 预处理数据
def preprocess_data(train, test, unlabeled_train)
    print(Preprocessing
    data...)
    start_time = time.time()

    # 预处理训练数据
    train['processed_review'] = train['review'].apply(preprocess_text)

    # 预处理测试数据
    test['processed_review'] = test['review'].apply(preprocess_text)

    # 预处理未标记数据
    unlabeled_train_subset = unlabeled_train.sample(20000, random_state=42)
    unlabeled_train_subset['processed_review'] = unlabeled_train_subset['review'].apply(preprocess_text)

    print(fPreprocessing
    completed in {time.time() - start_time
    .2
    f} seconds)
    return train, test, unlabeled_train, unlabeled_train_subset


# TF-IDF 模型
def train_tfidf_model(train, test)
    print(Training
    TF - IDF
    model...)
    start_time = time.time()

    # 使用TfidfVectorizer
    vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1, 1))
    X_train = vectorizer.fit_transform(train['processed_review'])
    y_train = train['sentiment']

    # 训练逻辑回归模型
    lr = LogisticRegression(random_state=42, max_iter=1000, C=1.0)
    lr.fit(X_train, y_train)

    # 交叉验证计算AUC
    cv_scores = cross_val_score(lr, X_train, y_train, cv=3, scoring='roc_auc')
    auc_score = np.mean(cv_scores)
    print(fTF - IDF
    AUC
    {auc_score
    .4
    f})
    print(fTF - IDF
    training
    completed in {time.time() - start_time
    .2
    f} seconds)

    # 预测测试集
    X_test = vectorizer.transform(test['processed_review'])
    test_pred = lr.predict_proba(X_test)[, 1]

    return test_pred, auc_score


# 生成提交文件
def generate_submission(test, predictions, filename)
    submission = pd.DataFrame({'id'
    test['id'], 'sentiment'
    predictions})
    submission.to_csv(filename, index=False, quoting=3)
    print(fSubmission
    file
    generated
    {filename})

    # 主函数
    def main()
        # 加载数据
        train, test, unlabeled_train = load_data()

        # 预处理数据
        train, test, unlabeled_train, unlabeled_train_subset = preprocess_data(train, test, unlabeled_train)

        # 训练模型
        tfidf_pred, tfidf_auc = train_tfidf_model(train, test)

        # 生成提交文件
        generate_submission(test, tfidf_pred, 'submission_TF-IDF.csv')

    if __name__ == __main__
        main()