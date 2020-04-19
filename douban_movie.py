import sqlite3
import pandas as pd
import jieba
from pyecharts.charts import WordCloud
import pyecharts.options as opts

# 读取数据
conn = sqlite3.connect(r'D:\Programing\python_projects\data_analysis_basics\data_set\douban_comment_data.db')
comment_data = pd.read_sql_query('select * from comment;', conn)


# 得到至少包含一定评论数的电影ID列表
def get_movie_id_list(minimum_comment):
    movie_list = comment_data['MOVIEID'].value_counts()  # 统计各电影ID的评论数
    movie_list = movie_list[movie_list.values > minimum_comment]
    return movie_list.index


# 得到某电影评论分词，并统计
def get_comment_keywords_counts(movie_id, count):
    # 汇集电影评论
    comment_list = comment_data[comment_data['MOVIEID'] == movie_id]['CONTENT']
    comment_str_all = ''
    for comment in comment_list:
        comment_str_all += comment + '\n'
    # 分词
    seg_list = list(jieba.cut(comment_str_all))
    # 过滤一个字的分词
    keywords_counts = pd.Series(seg_list)
    keywords_counts = keywords_counts[keywords_counts.str.len() > 1]
    # 过滤停用词
    with open('my_stopwords.txt', encoding='utf-8') as f:
        stop_words = f.read()
    stop_words = stop_words.replace('\n', '|')  # 转换正则格式的字符串
    keywords_counts = keywords_counts[~keywords_counts.str.contains(stop_words)]  # ~取反逻辑，表示不包含停用词
    # 取出前若干个分词
    keywords_counts = keywords_counts.value_counts()[:count]
    # print(keywords_counts)
    return keywords_counts


keywords_counts = get_comment_keywords_counts('1292052', 30)
wordcloud = WordCloud()
wordcloud.add('词云图', tuple(zip(keywords_counts.index, keywords_counts)), word_size_range=[20, 100])
wordcloud.set_global_opts(title_opts=opts.TitleOpts(title='《肖申克的救赎》评论'))
wordcloud.render()
