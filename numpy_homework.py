import numpy as np

file = r'D:\Programing\python_projects\data_analysis_basics\data_set\rating.txt'
data = np.genfromtxt(file, delimiter=',')
data = data.astype(int)

# 创建0数组存放评分总和与评分总人数
rating_sum = np.zeros(10000)
rating_amount = np.zeros(10000)

for line in data:
    book_id = line[1] - 1
    rating_sum[book_id] += line[2]
    rating_amount[book_id] += 1

# 计算每本书平均得分
print(rating_sum / rating_amount)
