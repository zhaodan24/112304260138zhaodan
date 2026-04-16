# 机器学习实验：基于 Word2Vec 的情感预测

## 1. 学生信息

- **姓名**：赵丹
- **学号**：112304260138
- **班级**：数据1231

> 注意：姓名和学号必须填写，否则本次实验提交无效。

***

## 2. 实验任务

本实验基于给定文本数据，使用 **Word2Vec 将文本转为向量特征**，再结合 **分类模型** 完成情感预测任务，并将结果提交到 Kaggle 平台进行评分。

本实验重点包括：

- 文本预处理
- Word2Vec 词向量训练或加载
- 句子向量表示
- 分类模型训练
- Kaggle 结果提交与分析

***

## 3. 比赛与提交信息

- **比赛名称**：**Bag of Words Meets Bags of Popcorn**
- **比赛链接**：[Bag of Words Meets Bags of Popcorn | Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/discussion?sort=hotness)
- **提交日期**：2026/4/15
- **GitHub 仓库地址**：<https://github.com/zhaodan24/112304260138zhaodan.git>
- **GitHub README 地址**：<https://github.com/zhaodan24/112304260138zhaodan>

> 注意：GitHub 仓库首页或 README 页面中，必须能看到“姓名 + 学号”，否则无效。

***

## 4. Kaggle 成绩

请填写你最终提交到 Kaggle 的结果：

- **Public Score**：0.95384
- **Private Score**（如有）：0.95384
- **排名**（如能看到可填写）：

***

## 5. Kaggle 截图

请在下方插入 Kaggle 提交结果截图，要求能清楚看到分数信息。

<br />

> 建议将截图保存在 `images` 文件夹中。![](<file:///C:\Users\16140\Documents\Tencent Files\1614039170\nt_qq\nt_data\Pic\2026-04\Ori\068f970112bb455a9918103fe94e697b.png>)\
> 截图文件名示例：`2023123456_张三_kaggle_score.png`

***

## 6. 实验方法说明

### （1）文本预处理

请说明你对文本做了哪些处理，例如：

- 分词
- 去停用词
- 去除标点或特殊符号
- 转小写

**我的做法：去HTML标签 → 转小写 → 标点处理 → 分词 → 停用词处理 → 词干提取**\
请在这里填写。

***

### （2）Word2Vec 特征表示

请说明你如何使用 Word2Vec，例如：

- 是自己训练 Word2Vec，还是使用已有模型
- 词向量维度是多少
- 句子向量如何得到（平均、加权平均、池化等）

\*\*我的做法：\*\*1. 模型训练方式

- 自己训练Word2Vec模型 ：使用比赛提供的训练数据和未标记数据进行训练
- 训练数据来源 ：
  - 标记训练数据（labeledTrainData.tsv）
  - 未标记训练数据的子集（从unlabeledTrainData.tsv中采样20,000条）
- 目的 ：利用更多数据训练出更适合电影评论领域的词向量

### 2. 词向量维度

- 维度设置 ： vector\_size=50
- 选择理由 ：
  - 平衡计算效率和表示能力
  - 50维向量足够捕捉单词的基本语义信息
  - 适合情感分析这类任务的需求

### 3. 训练参数

- 窗口大小 ： window=3 （考虑单词前后3个词的上下文）
- 最小词频 ： min\_count=10 （只保留出现至少10次的单词）
- 训练轮数 ： epochs=5
- 训练算法 ： sg=0 （使用CBOW算法，训练速度更快）
- 并行线程 ： workers=4 （利用多核CPU加速训练）

### 4. 句子向量计算方法

- 方法 ： 平均池化 （对句子中所有单词的词向量求平均值）
- 实现步骤 ：
  1. 将句子分词为单词列表
  2. 对每个单词，查找其对应的词向量
  3. 对所有单词向量求平均值，得到句子向量
  4. 如果句子中没有单词在词表中，返回全零向量
- 优点 ：
  - 计算简单高效
  - 能够捕捉句子的整体语义
  - 对噪声和异常值有一定的鲁棒性\
    请在这里填写。

***

### （3）分类模型

请说明你使用了什么分类模型，例如：

- Logistic Regression
- Random Forest
- SVM
- XGBoost

并说明最终采用了哪一个模型。

\*\*我的做法：\*\*1. 模型类型

- 逻辑回归（Logistic Regression）
- 实现库 ：scikit-learn

### 2. 模型参数

- 随机种子 ： random\_state=42 （确保结果可重现）
- 最大迭代次数 ： max\_iter=1000 （确保模型收敛）
- 正则化参数 ： C=1.0 （默认值，平衡模型复杂度和拟合能力）

### 3. 特征提取方法

- TF-IDF ：使用 TfidfVectorizer 提取特征
  - 最大特征数： max\_features=1000
  - n-gram范围： ngram\_range=(1, 1) （只使用单字词）

### 4. 模型评估

- 评估指标 ：AUC（ROC曲线下面积）
- 交叉验证 ：3折交叉验证
- 性能 ：TF-IDF + 逻辑回归模型的AUC分数为0.9358

### 5. 最终选择

- 最终采用模型 ： TF-IDF + 逻辑回归
- 选择理由 ：
  - 在所有测试的模型中，TF-IDF + 逻辑回归的AUC分数最高
  - 训练速度快，计算效率高
  - 模型简单，易于解释
  - 对特征维度的敏感性较低，不易过拟合\
    请在这里填写。

***

## 7. 实验流程

请简要说明你的实验流程。

示例：

1. 读取训练集和测试集
2. 对文本进行预处理
3. 训练或加载 Word2Vec 模型
4. 将每条文本表示为句向量
5. 用训练集训练分类器
6. 在测试集上预测结果
7. 生成 submission 文件并提交 Kaggle

**我的实验流程：**

\*\*1.\*\*读取数据 ：

- 读取标记训练数据（labeledTrainData.tsv）
- 读取测试数据（testData.tsv）
- 读取未标记训练数据（unlabeledTrainData.tsv）

  2.文本预处理 ：
- 去除HTML标签
- 转小写
- 处理标点符号（保留否定形式）
- 分词
- 去除停用词（保留否定词）
- 简单词干提取

  3.特征提取 ：
- 使用TF-IDF提取特征（max\_features=1000, ngram\_range=(1, 1)）

  4.模型训练 ：
- 训练逻辑回归模型（random\_state=42, max\_iter=1000, C=1.0）
- 3折交叉验证评估模型性能（AUC分数）

  5.模型选择 ：
- 比较不同模型的AUC分数
- 选择性能最佳的TF-IDF + 逻辑回归模型

  6.预测与提交 ：
- 在测试集上使用最佳模型进行预测
- 生成提交文件（submission\_TF-IDF.csv）
- 准备提交到Kaggle平台\
  请在这里填写。

***

## 8. 文件说明

请说明仓库中各文件或文件夹的作用。

示例：

- `data/`：存放数据文件
- `src/`：存放源代码
- `notebooks/`：存放实验 notebook
- `images/`：存放 README 中使用的图片
- `submission/`：存放提交文件

**我的项目结构：**

```text
project/
├─ data/
├─ src/
├─ notebooks/
├─ images/
├─ submission/
└─ README.md

```

