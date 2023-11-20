import numpy as np
import matplotlib.pyplot as plt

# パラメータ設定
mu = 0.0  # Levy分布の位置パラメータ
sigma = 1.0  # Levy分布の尺度パラメータ

# x軸の範囲 (0から15まで)
x = np.linspace(0, 15, 1000)

# Levy分布の確率密度関数（PDF）
levy_pdf = np.sqrt(1 / (2 * np.pi * sigma**2)) * np.exp(-1 / (2 * sigma**2 * (x - mu))) / (x - mu)**(3/2)

# 標準正規分布の確率密度関数（PDF）
normal_pdf = 1 / np.sqrt(2 * np.pi) * np.exp(-x**2 / 2)

# グラフのプロット
plt.plot(x, levy_pdf, label='Lévy', linewidth=3, color = 'red')
plt.plot(x, normal_pdf, label='Normal', linestyle = "dashed", linewidth=3)
# plt.xlabel('距離', fontname="HGGothicE")
# plt.ylabel('確率', fontname="HGGothicE")
#plt.title('標準正規分布(l>0)とLévy分布', fontname="HGGothicE")
plt.legend()
plt.grid(True)
plt.show()