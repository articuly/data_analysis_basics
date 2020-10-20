from sklearn import svm, linear_model, ensemble, datasets
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts

# 读取鸢尾花数据集
iris = datasets.load_iris()
# print(iris)
X = iris.data
y = iris.target

# 拆分数据为训练集与测试集，使用分类模型
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
clf = svm.LinearSVC()
clf.fit(X_train, y_train)
y_predict = clf.predict(X_test)

# 计算预测数据与测试集差异
print(y_predict)
print(y_test)
sc = clf.score(X_test, y_test)
mse = mean_squared_error(y_test, y_predict)
print('score is ', sc)
print('mse is', mse)

# 读取波士顿房价数据集
boston = datasets.load_boston()
# print(boston)
X = boston.data
y = boston.target

# 拆分数据集，使用回归模型
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
lasso = linear_model.Lasso(alpha=0.1)
lasso.fit(X_train, y_train)
y_predict = lasso.predict(X_test)

# 计算预测评分
mse = mean_squared_error(y_test, y_predict)
score = lasso.score(X_test, y_test)
print('score is ', score)
print('mse is', mse)

# 使用网格搜索调节参数
alpha_range = np.arange(0.05, 1, 0.05)
param_grid = {'alpha': alpha_range}
lasso_search = GridSearchCV(lasso, param_grid)
lasso_search.fit(X_train, y_train)
for result in lasso_search.cv_results_:
    print(result, lasso_search.cv_results_[result])
print(lasso_search.best_score_)
print(lasso_search.best_params_)
print(lasso_search.best_estimator_)

gbr_reg = ensemble.GradientBoostingRegressor()
gbr_reg.fit(X_train, y_train)
# 查看各个特征的重要程度
feature_importance_df = pd.DataFrame({
    'name': boston.feature_names,
    'importance': gbr_reg.feature_importances_
})
feature_importance_df.sort_values(by='importance', ascending=False, inplace=True)
bar = Bar(init_opts=opts.InitOpts(width='1280px', height='720px'))
bar.add_yaxis('各特征重要性', list(feature_importance_df['importance'].apply(lambda x: round(x*100,4))))
bar.add_xaxis(list(feature_importance_df.name))
bar.render(path='各特征重要性.html')

# 使用随机搜索调节参数
n_estimators_range = np.arange(100, 1000, 100)
max_depth_range = np.arange(3, 10)
learn_rate_range = [0.001, 0.001, 0.01, 0.1]
param_grid = {
    'n_estimators': n_estimators_range,
    'max_depth': max_depth_range,
    'learning_rate': learn_rate_range
}
gbr_search = RandomizedSearchCV(gbr_reg, param_grid, n_iter=30)  # 测试30次
gbr_search.fit(X_train, y_train)
for result in gbr_search.cv_results_:
    print(result)
print(gbr_search.best_score_)
print(gbr_search.best_params_)
print(gbr_search.best_estimator_)
