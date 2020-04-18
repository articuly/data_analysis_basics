# coding:utf-8
import pandas as pd

# 读取数据
file1 = r'D:\Programing\python_projects\data_analysis_basics\data_set\to_read.csv'
to_read = pd.read_csv(file1)
file2 = r'D:\Programing\python_projects\data_analysis_basics\data_set\books.csv'
books = pd.read_csv(file2)
file3 = r'D:\Programing\python_projects\data_analysis_basics\data_set\book_tags.csv'
book_tags = pd.read_csv(file3)
file4 = r'D:\Programing\python_projects\data_analysis_basics\data_set\tags.csv'
tags = pd.read_csv(file4)

# 得到排序统计后的数据
to_read_counts = to_read['book_id'].value_counts().sort_values(ascending=False)
# print(to_read_counts)

# 截取前50的数据，找到最热门50本书的ID
top50_book_id = to_read_counts[:50].index
top50_book_counts = to_read_counts[:50].values
top50_book = pd.DataFrame({
    'book_id': top50_book_id,
    'to_read_count': top50_book_counts
})
print(top50_book)

# 取得带有标题的DF
book_id_title = books[['book_id', 'goodreads_book_id', 'title']]
# print(book_id_title)

# 合并DF，找到对应的书籍名称
top50_book_with_title = pd.merge(top50_book, book_id_title, on='book_id', how='left')
print(top50_book_with_title)
top50_book_with_title.to_csv(r'.\data_set\top50_book_with_title.csv', encoding='utf-8')

# 通过关联字段找到最热门标签
book_tags = book_tags[book_tags['_goodreads_book_id_'].isin(top50_book_with_title['goodreads_book_id'])]
del book_tags['_goodreads_book_id_']
top10_tags = book_tags.groupby('tag_id').sum()
top10_tags = top10_tags.sort_values(by='count', ascending=False)[:10]
print(top10_tags)

# 通过tag_id找到对应的名称
top10_tags_with_name = pd.merge(top10_tags, tags, on='tag_id', how='left')
print(top10_tags_with_name)
top10_tags_with_name.to_csv(r'.\data_set\top10_tags_with_name.csv')

# 绘图
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

top50_book = pd.read_csv(r'.\data_set\top50_book_with_title.csv')
top10_book = top50_book[:10]

bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width='1280px', height='720px'))
bar.add_xaxis(top10_book['title'].tolist())
bar.add_yaxis('书籍', top10_book['to_read_count'].tolist())
bar.set_global_opts(title_opts=opts.TitleOpts(title='最热门的20本书', subtitle='英文读物'),
                    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)))
bar.render(path='top10_books.html')
