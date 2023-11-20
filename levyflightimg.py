import numpy as np
import matplotlib.pyplot as plt

def levy_flight_simulation(num_steps, alpha):
    x = np.zeros(num_steps)
    y = np.zeros(num_steps)

    for i in range(1, num_steps):
        direction = np.random.uniform(0, 2 * np.pi)  # ランダムな方向
        jump_length = np.random.pareto(alpha) + 1  # レヴィ分布に従うジャンプの大きさ
        x[i] = x[i - 1] + jump_length * np.cos(direction)  # x方向の移動
        y[i] = y[i - 1] + jump_length * np.sin(direction)  # y方向の移動

    return x, y

# パラメータ設定
num_steps = 1000  # ステップ数
alpha = 1.5  # レヴィ指数

# レヴィフライトのシミュレーション
x, y = levy_flight_simulation(num_steps, alpha)

# 結果のプロット
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Levy Flight Simulation")
plt.show()
