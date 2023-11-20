import numpy as np
import matplotlib.pyplot as plt

# パラメータ設定
lamda = 0.5  # 指数分布のレートパラメータ

# x軸の範囲 (0から10まで)
x = np.linspace(0, 10, 1000)

# 指数分布の確率密度関数（PDF）
exponential_pdf = lamda * np.exp(-lamda * x)

# グラフのプロット
plt.plot(x, exponential_pdf, label='Exponential Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Exponential Distribution')
plt.legend()
plt.grid(True)
plt.show()
