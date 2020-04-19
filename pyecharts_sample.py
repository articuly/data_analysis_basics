from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar3D, Line, Pie, EffectScatter, Funnel, Geo, Liquid, Radar, WordCloud
from pyecharts.globals import ThemeType, SymbolType
import numpy as np

# 3D柱状图
data = [(i, j, np.random.randint(0, 15)) for i in range(24) for j in range(7)]  # 创建三位元组的列表
bar3d = Bar3D(init_opts=opts.InitOpts(height='720px', width='1280px', theme=ThemeType.LIGHT))
bar3d.add('', data,
          xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_='category'),
          yaxis3d_opts=opts.Axis3DOpts(Faker.week, type_='category'),
          zaxis3d_opts=opts.Axis3DOpts(type_='value'))
bar3d.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=20),  # 设定最大值边界
                      title_opts=opts.TitleOpts(title='Bar3D Sample'))
bar3d.render(path='pyecharts-bar3d.html')

# 折线图，面积图
line = Line()
line.add_xaxis(Faker.choose())
line.add_yaxis('Sample A', Faker.values(), is_smooth=True)
line.add_yaxis('Sample B', Faker.values(), areastyle_opts=opts.AreaStyleOpts(opacity=0.3, color='blue'))
line.set_global_opts(title_opts=opts.TitleOpts(title='Line Sample'))
line.render(path='pyecharts-line.html')

# 饼图
pie = Pie()
data = [list(z) for z in zip(Faker.choose(), Faker.values())]  # 创建有二个元素列表的列表
pie.add('', data,
        radius=['40%', '80%'],  # 内部中空的饼图，指定内环和外环半径
        rosetype='area')  # 通过半径大小区分的玫瑰饼图
pie.set_global_opts(title_opts=opts.TitleOpts(title='Pie Sample'))
pie.set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{c}'))  # 标签显示格式
pie.render(path='pyecharts-pie.html')

# 特效散点图
effect_scatter = EffectScatter()
effect_scatter.add_xaxis(Faker.choose())
effect_scatter.add_yaxis('', Faker.values(), symbol=SymbolType.DIAMOND)
effect_scatter.set_global_opts(title_opts=opts.TitleOpts(title='EffectScatter Sample'))
effect_scatter.render(path='pyecharts-effect-scatter.html')

# 漏斗图
funnel = Funnel()
data = [list(z) for z in zip(Faker.choose(), Faker.values())]  # 创建有二个元素列表的列表
funnel.add('用户转化率', data,
           label_opts=opts.LabelOpts(position='inside'))  # 标签内置
funnel.set_global_opts(title_opts=opts.TitleOpts(title='Funnel Sample'))
funnel.render(path='pyecharts-funnel.html')

# 地理图
geo = Geo()
geo.add_schema(maptype='china')
data = [list(z) for z in zip(Faker.provinces, Faker.values())]
geo.add('geo', data, type_='heatmap')
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
geo.set_global_opts(title_opts=opts.TitleOpts(title='Geo Sample'),
                    visualmap_opts=opts.VisualMapOpts())
geo.render('pyecharts-geo.html')

# 水球图
liquid = Liquid()
shape = 'path://M512 1024c-209.066667 0-384-170.666667-384-379.733333V640c145.066667 0 277.333333 81.066667 341.333333 204.8v-115.2c-51.2-12.8-89.6-51.2-106.666666-102.4-12.8 4.266667-21.333333 4.266667-34.133334 4.266667-55.466667 0-106.666667-29.866667-136.533333-76.8-34.133333-59.733333-25.6-136.533333 21.333333-183.466667-46.933333-51.2-55.466667-128-21.333333-187.733333 29.866667-46.933333 81.066667-76.8 136.533333-76.8 12.8 0 21.333333 0 34.133334 4.266666C384 42.666667 443.733333 0 512 0s128 42.666667 149.333333 110.933333c12.8-4.266667 21.333333-4.266667 34.133334-4.266666 55.466667 0 106.666667 29.866667 136.533333 76.8 34.133333 59.733333 25.6 136.533333-21.333333 183.466666 46.933333 51.2 55.466667 123.733333 21.333333 183.466667-29.866667 46.933333-81.066667 76.8-136.533333 76.8-12.8 0-21.333333 0-34.133334-4.266667-17.066667 51.2-55.466667 89.6-106.666666 102.4v115.2c64-128 196.266667-209.066667 341.333333-204.8 0 217.6-170.666667 388.266667-384 388.266667zM362.666667 362.666667c0 81.066667 68.266667 149.333333 149.333333 149.333333s149.333333-68.266667 149.333333-149.333333S593.066667 213.333333 512 213.333333 362.666667 281.6 362.666667 362.666667z'
liquid.add('Liquid', [0.7, 0.6, 0.5],
           is_outline_show=False,
           shape=shape)
liquid.set_global_opts(title_opts=opts.TitleOpts(title='Liquid Sample'))
liquid.render('pyecharts-liquid.html')

# 雷达图
v1 = [[4300, 10000, 28000, 35000, 50000, 19000],
      [3300, 13000, 25000, 30000, 48000, 24000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
radar = Radar()
radar.add_schema(
    schema=[
        opts.RadarIndicatorItem(name='销售', max_=6500),
        opts.RadarIndicatorItem(name='管理', max_=16000),
        opts.RadarIndicatorItem(name='信息技术', max_=30000),
        opts.RadarIndicatorItem(name='客服', max_=38000),
        opts.RadarIndicatorItem(name='研发', max_=52000),
        opts.RadarIndicatorItem(name='市场', max_=25000),
    ]
)
radar.add('预算分配', v1)
radar.add('实际开销', v2)
radar.set_global_opts(title_opts=opts.TitleOpts(title='Radar Sample'))
radar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
radar.render('pyecharts-radar.html')

# 词云图
words = [
    ('Sam S Club', 10000),
    ('Macys', 6181),
    ('Amy Schumer', 4386),
    ('Jurassic World', 4055),
    ('Charter Communications', 2467),
]
wordcloud = WordCloud()
wordcloud.add('', words, word_size_range=[20, 100])
wordcloud.set_global_opts(title_opts=opts.TitleOpts(title='WordCloud Sample'))
wordcloud.render('pyecharts-wordcloud.html')

# 更多图表 https://pyecharts.org/#/zh-cn/basic_charts http://gallery.pyecharts.org/#/Boxplot/boxplot_light_velocity
