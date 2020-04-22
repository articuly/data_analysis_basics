from sklearn import datasets

data = datasets.fetch_20newsgroups(subset='all')
print(data.data)
