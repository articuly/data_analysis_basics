import pandas as pd
from pyecharts.charts import WordCloud
import pyecharts.options as opts

kw_counts_by_score = [[] for _ in range(10)]
for i in range(4, 10):
    kw_counts_by_score[i] = pd.read_csv(r'.\data_set\{0}_movie_keywords.csv'.format(i))
    kw_percentage_df = pd.DataFrame([],
                                    columns=list(range(4, 10)),
                                    index=kw_counts_by_score[9]['kw'][:10])

for i in range(4, 10):
    kw = kw_counts_by_score[i]
    kw = kw[kw['kw'].isin(kw_percentage_df.index)]
    kw_percentage_df[i] = pd.Series(list(kw['percentage']), index=kw['kw'])
