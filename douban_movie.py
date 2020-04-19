import sqlite3
import pandas as pd

# 读取数据
conn = sqlite3.connect(r'D:\Programing\python_projects\data_analysis_basics\data_set\douban_comment_data.db')
comment_data = pd.read_sql_query('select * from comment;', conn)
# print(comment_data.head())
