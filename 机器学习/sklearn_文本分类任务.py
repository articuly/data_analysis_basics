from sklearn import datasets
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

data_train = datasets.fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'))
# print(data_tran.data[0])
# print(data_tran.target_names)
# print(data_tran.target_names[data_tran.target[0]])

# 计数向量转化，停用词参数传入列表
count_vect = CountVectorizer(stop_words='english')
# 数据统计转换
X_train_counts = count_vect.fit_transform(data_train.data)
# 使用tfidf方法
tfidf_transformer = TfidfTransformer().fit(X_train_counts)
X_train_tfidf = tfidf_transformer.transform(X_train_counts)
# 使用多项朴素贝叶斯
clf = MultinomialNB()
clf.fit(X_train_tfidf, data_train.target)

test_setences = [
    'do you use mac',
    'god loes you',
    'openGL on GPU is fast',
    'President Trump’s off-again, on-again commencement speech in June will bring back cadets who scattered across the country to counter the coronavirus.',
    'After weeks of briefings that sometimes last more than two hours, there is some agreement in the West Wing that some of the news conferences have gone on too long, resulting in a situation where Trump and administration officials simply run out of coronavirus-related questions. The result, aides have noticed, is that the briefings stray into politics instead of the matter at hand.',
    'Kim Jong Un has been enjoying Donald Trump presidency. After Trump threats of "fire and fury" turned to love letters and handshakes, the North Korean leader has largely gotten a free pass on a lot of destabilizing activities -- including the short-range missile tests he ramped up in recent weeks. In fact, Kim stayed in President Trump good graces for longer than many of Trump hand-picked cabinet secretaries.',
]
X_test_count = count_vect.transform(test_setences)
X_test_tdidf = tfidf_transformer.transform(X_test_count)
predicted = clf.predict(X_test_tdidf)

for doc, cate in zip(test_setences, predicted):
    print('{}=>{}'.format(doc, data_train.target_names[cate]))
