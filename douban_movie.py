import sqlite3
import pandas as pd
import numpy as np
import jieba
from pyecharts.charts import WordCloud
import pyecharts.options as opts

# 读取数据
conn = sqlite3.connect(r'.\data_set\douban_comment_data.db')
comment_data = pd.read_sql_query('select * from comment;', conn)
movie_data = pd.read_excel(r'.\data_set\douban_movie_data.xlsx')


# 得到至少包含一定评论数的电影ID列表，从多到少排列
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


def generate_word_cloud(word_list, path_name=None):
    wordcloud = WordCloud()
    wordcloud.add('词云图', tuple(zip(word_list.index, word_list)), word_size_range=[20, 100])
    wordcloud.set_global_opts(title_opts=opts.TitleOpts(title='电影评论'))
    wordcloud.render(path=path_name)
    print(f'Generate word cloud file done: {path_name}')


# 根据电影ID在xlsx文件找到电影名和评分
def get_movie_name_and_score(movie_id):
    movie_link = 'https://movie.douban.com/subject/{0}/'.format(movie_id)
    search_result = movie_data[movie_data['链接'] == movie_link].iloc[0]
    movie_name = search_result['电影名']
    movie_score = search_result['评分']
    return (movie_name, movie_score)


# movie_id = '1292052'
# keywords_counts = get_comment_keywords_counts(movie_id, 30)
# movie_name, movie_score = get_movie_name_and_score(movie_id)
# path_name = 'wordcloud\{0}_{1}.html'.format(movie_name, movie_score)
# generate_word_cloud(keywords_counts, path_name)


kw_list_by_score = [[] for _ in range(10)]
kw_counts_list_by_score = [[] for _ in range(10)]
print(kw_list_by_score)
