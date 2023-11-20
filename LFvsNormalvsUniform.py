import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def cauchy_simulation(num_steps, alpha):
    x = np.zeros(num_steps)
    y = np.zeros(num_steps)

    for i in range(1, num_steps):
        direction = np.random.uniform(0, 2 * np.pi)  # ランダムな方向
        jump_length = np.random.standard_cauchy() ** (-1 / alpha)  # レヴィ分布に従うジャンプの大きさ
        x[i] = x[i - 1] + jump_length * np.cos(direction)  # x方向の移動
        y[i] = y[i - 1] + jump_length * np.sin(direction)  # y方向の移動

    return x, y

def levy_flight_simulation(num_steps, alpha):
    x = np.zeros(num_steps)
    y = np.zeros(num_steps)

    for i in range(1, num_steps):
        direction = np.random.uniform(0, 2 * np.pi)  # ランダムな方向
        jump_length = np.random.standard_normal() ** (-1 / alpha)  # レヴィ分布に従うジャンプの大きさ
        x[i] = x[i - 1] + jump_length * np.cos(direction)  # x方向の移動
        y[i] = y[i - 1] + jump_length * np.sin(direction)  # y方向の移動

    return x, y

def normal_random_walk_simulation(num_steps):
    x = np.zeros(num_steps)
    y = np.zeros(num_steps)

    for i in range(1, num_steps):
        dx, dy = np.random.normal(0, 1, 2)  # 正規分布に従う変化量
        x[i] = x[i - 1] + dx  # x方向の移動
        y[i] = y[i - 1] + dy  # y方向の移動

    return x, y

def uniform_random_walk_simulation(num_steps):
    x = np.zeros(num_steps)
    y = np.zeros(num_steps)

    for i in range(1, num_steps):
        dx, dy = np.random.uniform(-1, 1, 2)  # 一様分布に従う変化量
        x[i] = x[i - 1] + dx  # x方向の移動
        y[i] = y[i - 1] + dy  # y方向の移動

    return x, y

# パラメータ設定
num_steps = 300  # ステップ数
alpha = 1.3  # レヴィ指数

# レヴィフライトのシミュレーション
levy_x, levy_y = levy_flight_simulation(num_steps, alpha)

# 正規分布に基づくランダムウォークのシミュレーション
normal_x, normal_y = normal_random_walk_simulation(num_steps)

# 一様分布に基づくランダムウォークのシミュレーション
# uniform_x, uniform_y = uniform_random_walk_simulation(num_steps)

# グラフの範囲設定
max_range = max(
    np.abs(np.max(levy_x)), np.abs(np.min(levy_x)), np.abs(np.max(levy_y)), np.abs(np.min(levy_y)),
    np.abs(np.max(normal_x)), np.abs(np.min(normal_x)), np.abs(np.max(normal_y)),
    # np.abs(np.min(uniform_x)), np.abs(np.max(uniform_x)), np.abs(np.min(uniform_y)), np.abs(np.max(uniform_y))
    )

# アニメーションの作成
fig, ax = plt.subplots()
# ax.set_xlim(np.min(x), np.max(x))
# ax.set_ylim(np.min(y), np.max(y))

ax.set_xlim(-max_range, max_range)
ax.set_ylim(-max_range, max_range)
line1, = ax.plot([], [], 'r-', lw=1)
line2, = ax.plot([], [], 'b-', lw=1)
# line3, = ax.plot([], [], 'b-', lw=1)

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    # line3.set_data([], [])
    # return line1, line2, line3,
    return line1, line2,


def update(frame):
    line1.set_data(levy_x[:frame], levy_y[:frame])
    line2.set_data(normal_x[:frame], normal_y[:frame])
    # line3.set_data(uniform_x[:frame], uniform_y[:frame])
    # return line1, line2, line3,
    return line1, line2,

# アニメーションの再生
ani = animation.FuncAnimation(fig, update, frames=num_steps, init_func=init, blit=True)
ani.save("LF_NORMoving300.gif", writer="pillow")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
plt.show()

