import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'

# function
def f(x):
    return x**3 - 8

def df(x):
    return 3*x**2

points = np.array([0,1,2,3,4])
y_points = f(points)

x = np.linspace(-0.5,4.5,400)
y = f(x)

fig, ax = plt.subplots(figsize=(25,11))

# 主曲线
ax.plot(x, y, linewidth=2)

# 投影线和点
for x0, y0 in zip(points, y_points):
    ax.plot([x0,x0],[0,y0],'k--', linewidth=0.8)
    ax.plot([0,x0],[y0,y0],'k--', linewidth=0.8)
    if x0 == 2:
        ax.scatter(x0, y0, color="red", s=120, zorder=5)
    else:
        ax.scatter(x0, y0, color="black", s=30, zorder=5)

# 绘制原本的蓝色切线（除0和2）
for x0, y0 in zip(points, y_points):
    if x0 == 0 or x0 == 2:
        continue
    m = df(x0)
    x_axis = x0 - y0/m
    ax.plot([x0, x_axis],[y0,0], color="blue", linewidth=0.8)

# 轴和外框
ax.axhline(0)
ax.axvline(0)
ax.set_xlim(-1,5)
ax.set_ylim(-30,60)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(r"$y = x^3 - 8$")

for spine in ['top','right','left','bottom']:
    ax.spines[spine].set_visible(False)

ax.set_xticks(points)
ax.set_yticks([])

# 动画切线：两段 x 序列合并
x_anim1 = np.arange(4, 1.9, -0.1)  # 4 -> 2
x_anim2 = np.arange(1, 2.1, 0.1)   # 1 -> 2
x_anim = np.concatenate([x_anim1, x_anim2])

past_lines = []  # 已经过的动画切线
current_line = None

def animate(i):
    global current_line
    # 将上一帧的当前切线变浅红虚线
    if current_line is not None:
        current_line.set_linestyle('--')
        current_line.set_color('#FF9999')
        current_line.set_linewidth(1)
        past_lines.append(current_line)
    
    # 当前动画切线
    x0 = x_anim[i]
    y0 = f(x0)
    m = df(x0)
    x_axis = x0 - y0/m
    current_line, = ax.plot([x0, x_axis],[y0,0], color='red', linewidth=2)
    
    return past_lines + [current_line]

# 延长间隔，动画慢一点
ani = FuncAnimation(fig, animate, frames=len(x_anim), interval=400, blit=False, repeat=False)

plt.show()