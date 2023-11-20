import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# パラメータ設定
num_steps = 1000  # ステップ数
alpha = 1.5  # レヴィ指数（ジャンプの大きさを制御するパラメータ）

# 初期位置
x = np.zeros(num_steps)
y = np.zeros(num_steps)

# ランダムなジャンプの生成（レヴィ分布に従う）
jumps = np.random.pareto(alpha, num_steps) + 1

# 移動の計算
for i in range(1, num_steps):
    theta = np.random.uniform(0, 2 * np.pi)  # ランダムな方向
    dx = jumps[i] * np.cos(theta)  # x方向の移動
    dy = jumps[i] * np.sin(theta)  # y方向の移動
    x[i] = x[i - 1] + dx  # x座標の更新
    y[i] = y[i - 1] + dy  # y座標の更新

# アニメーションの作成
fig, ax = plt.subplots()
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(y), np.max(y))
line, = ax.plot([], [], 'b-', lw=1)


def init():
    line.set_data([], [])
    return line,


def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,


# アニメーションの再生
ani = animation.FuncAnimation(
    fig, update, frames=num_steps, init_func=init, blit=True)
plt.show()
