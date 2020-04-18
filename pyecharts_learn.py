from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

# bar=Bar()
# bar.add_xaxis(Faker.choose())
# bar.add_yaxis('商家', Faker.values())
# bar.render()

# 初始化参数
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.SHINE, width='1600px', height='900px'))
# 生成数据
bar.add_xaxis(Faker.choose())
bar.add_yaxis('商家A', Faker.values(), stack='stack1')
bar.add_yaxis('商家B', Faker.values(), stack='stack1')
bar.add_yaxis('商家C', Faker.values(), stack='stack2')
bar.add_yaxis('商家D', Faker.values(), stack='stack2')
# 设置其它参数
bar.set_global_opts(title_opts=opts.TitleOpts(title='Bar Sample', subtitle='我是副标题'),
                    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)),
                    datazoom_opts=[opts.DataZoomOpts()])
bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                    markpoint_opts=opts.MarkPointOpts(
                        data=[opts.MarkPointItem(type_='max', name='最大值'),
                              opts.MarkPointItem(type_='min', name='最小值'), ]),
                    markline_opts=opts.MarkLineOpts(
                        data=[opts.MarkLineItem(type_='average', name='平均值'), ]))
# 绘制
bar.reversal_axis()
bar.render()
