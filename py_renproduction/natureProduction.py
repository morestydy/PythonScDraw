import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoLocator, FixedLocator

x = np.arange(1, 100)
y = x**2

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111)

# 准备 x/y轴刻度，以及刻度标签
# x轴
xmajor = MultipleLocator(10)  # 主 10 的倍数
xminor = MultipleLocator(2)  # 次 2的倍数
# y轴
ymajor_1 = MultipleLocator(2000)
yminor_1 = MultipleLocator(400)

# 设置 x/y轴刻度，以及刻度标签
# x 轴
ax.xaxis.set_minor_locator(xminor)
ax.xaxis.set_major_locator(xmajor)
ax.tick_params(axis="x", direction="in", which="minor", length=4)
ax.tick_params(axis="x", direction="out", which="major", labelsize=15, length=5)
'''
axis: x轴还是y轴
direction："in" 向内,"out"向外
which:"major" 设置主轴参数，"minor"设置次轴参数，"both"l两个轴的参数一起设置
labelsize:设置刻度标签的字体大小
length：设置标签刻度的长度
'''
# y轴
ax.yaxis.set_minor_locator(yminor_1)
ax.yaxis.set_major_locator(ymajor_1)
ax.tick_params(axis="y", direction="in", which="minor", length=4)
ax.tick_params(axis="y", direction="out", which="major", labelsize=15, length=5)

ax.plot(x,y)
plt.show()
