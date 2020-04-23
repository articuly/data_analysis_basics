import pandas as pd
from pyecharts.charts import HeatMap
import pyecharts.options as opts

# 建立空表存放关键词与评分之间比例
kw_counts_by_score = [[] for _ in range(10)]
for i in range(4, 10):
    kw_counts_by_score[i] = pd.read_csv(r'.\data_set\{0}_movie_keywords.csv'.format(i))

kw_percentage_df = pd.DataFrame([], columns=list(range(4, 10)), index=kw_counts_by_score[9]['kw'][:10])

# 将数据写入空表
for i in range(4, 10):
    kw_df = kw_counts_by_score[i]
    kw_df = kw_df[kw_df['kw'].isin(kw_percentage_df.index)]
    kw_percentage_df[i] = pd.Series(list(kw_df['percentage']), index=kw_df['kw'])

# 用0替换NAN，否则无法计算
kw_percentage_df.fillna(0, inplace=True)

# 建立有三个元素的列表，作为绘制的数据
data = []
i = 0
for index in kw_percentage_df.index:
    j = 0
    for column in kw_percentage_df.columns:
        data.append([j, i, kw_percentage_df[column][index] * 100])
        j += 1
    i += 1

# 绘制热力图
heatmap = HeatMap()
heatmap.add_xaxis(list(kw_percentage_df.columns))
heatmap.add_yaxis('电影评论关键词热力图', list(kw_percentage_df.index), data)
heatmap.set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=0, max_=10, orient='horizontal'))
heatmap.render('comment_heatmap.html')
