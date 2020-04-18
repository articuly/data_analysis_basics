from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar3D
from pyecharts.globals import ThemeType
import numpy as np

data = [(i, j, np.random.randint(0, 15)) for i in range(24) for j in range(7)]

bar3d = Bar3D(init_opts=opts.InitOpts(height='720px', width='1280px', theme=ThemeType.LIGHT))
bar3d.add('', data,
          xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_='category'),
          yaxis3d_opts=opts.Axis3DOpts(Faker.week, type_='category'),
          zaxis3d_opts=opts.Axis3DOpts(type_='value'))
bar3d.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=20),
                      title_opts=opts.TitleOpts(title='Bar3D Sample'))
bar3d.render()
