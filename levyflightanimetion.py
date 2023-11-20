import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def levy_flight_simulation(num_steps, alpha):
    x = np.zeros(num_steps)
    y = np.zeros(num_steps)

    for i in range(1, num_steps):
        direction = np.random.uniform(0, 2 * np.pi)  # ランダムな方向
        jump_length = np.random.standard_normal() ** (-1 / alpha)  # レヴィ分布に従うジャンプの大きさ
        x[i] = x[i - 1] + jump_length * np.cos(direction)  # x方向の移動
        y[i] = y[i - 1] + jump_length * np.sin(direction)  # y方向の移動

    return x, y

# パラメータ設定
num_steps = 150  # ステップ数
alpha = 1.3  # レヴィ指数

# レヴィフライトのシミュレーション
x, y = levy_flight_simulation(num_steps, alpha)

# グラフの範囲設定
max_range = max(np.abs(np.min(x)), np.abs(np.max(x)), np.abs(np.min(y)), np.abs(np.max(y)))

# アニメーションの作成
fig, ax = plt.subplots()
# ax.set_xlim(np.min(x), np.max(x))
# ax.set_ylim(np.min(y), np.max(y))

ax.set_xlim(-max_range, max_range)
ax.set_ylim(-max_range, max_range)
line, = ax.plot([], [], 'r-', lw=1)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,

# アニメーションの再生
ani = animation.FuncAnimation(fig, update, frames=num_steps, init_func=init, blit=True)
ani.save("LFMoving150a.gif", writer="pillow")
plt.show()
