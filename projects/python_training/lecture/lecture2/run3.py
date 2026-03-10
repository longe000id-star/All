import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'

# 函数和导数
def f(x):
    return x**3 - 8
def df(x):
    return 3*x**2

# 原始点
points = np.array([0,1,2,3,4])
y_points = f(points)

x = np.linspace(-0.5,4.5,400)
y = f(x)

fig, ax = plt.subplots(figsize=(25,11))
plt.subplots_adjust(bottom=0.2)  # 给按钮留空间

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

# 绘制原蓝色切线（除0和2）
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
paused = False
frame_index = [0]  # 可变帧索引

def animate(_):
    global current_line
    if paused:
        return past_lines + ([current_line] if current_line else [])

    # 删除上一帧红色切线
    if current_line is not None:
        current_line.set_linestyle('--')
        current_line.set_color('#FF9999')
        current_line.set_linewidth(1)
        past_lines.append(current_line)

    # 当前动画切线
    x0 = x_anim[frame_index[0]]
    y0 = f(x0)
    m = df(x0)
    x_axis = x0 - y0/m
    current_line, = ax.plot([x0, x_axis],[y0,0], color='red', linewidth=2)

    frame_index[0] += 1

    # 循环回到起点时，清理上一次动画的红色切线
    if frame_index[0] >= len(x_anim):
        for line in past_lines:
            line.remove()    # 删除上一轮红色虚线
        if current_line is not None:
            current_line.remove()
        past_lines.clear()
        current_line = None
        frame_index[0] = 0

    return past_lines + ([current_line] if current_line else [])

ani = FuncAnimation(fig, animate, frames=len(x_anim), interval=400, blit=False, repeat=True)

# 按钮回调
def toggle(event):
    global paused
    paused = not paused

# 创建 Play/Pause 按钮
ax_button = plt.axes([0.8, 0.05, 0.1, 0.075])  # 右下角
btn = Button(ax_button, 'Play/Pause')
btn.on_clicked(toggle)

plt.show()