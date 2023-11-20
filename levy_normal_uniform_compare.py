import numpy as np
import matplotlib.pyplot as plt

# レヴィ分布のパラメータ
mu_levy = 0  # 位置パラメータ
sigma_levy = 1  # 尺度パラメータ

# 標準正規分布のパラメータ
mu_normal = 0  # 平均
sigma_normal = 1  # 標準偏差

# 一様分布のパラメータ
a_uniform = 0  # 下限
b_uniform = 1  # 上限

# x軸の値の範囲
x = np.linspace(0,15, 1000)

# レヴィ分布の確率密度関数
levy_pdf = np.sqrt(1 / (2 * np.pi * sigma_levy**2)) * np.exp(-1 / (2 * sigma_levy**2 * (x - mu_levy))) / (x - mu_levy)**(3/2)

# 標準正規分布の確率密度関数
normal_pdf = 1 / (np.sqrt(2 * np.pi) * sigma_normal) * np.exp(-(x - mu_normal)**2 / (2 * sigma_normal**2))

# 一様分布の確率密度関数
uniform_pdf = np.where((x >= a_uniform) & (x <= b_uniform), 1 / (b_uniform - a_uniform), 0)

# グラフのプロット
plt.plot(x, levy_pdf, label='Levy Distribution')
plt.plot(x, normal_pdf, label='Standard Normal Distribution')
plt.plot(x, uniform_pdf, label='Uniform Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Comparison of Distributions')
plt.legend()
plt.show()
