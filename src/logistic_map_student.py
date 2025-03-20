"""
Logistic映射与混沌系统研究
"""

import numpy as np
import matplotlib.pyplot as plt

def iterate_logistic(r, x0, n):
    """
    迭代Logistic映射
    
    参数:
        r: 增长率参数
        x0: 初始值
        n: 迭代次数
        
    返回:
        x: 迭代序列数组
    """
    x = np.zeros(n)  # 初始化数组
    x[0] = x0  # 设置初始值
    for i in range(1, n):
        x[i] = r * x[i-1] * (1 - x[i-1])  # Logistic映射迭代公式
    return x

def plot_time_series(r_values, x0, n):
    """
    绘制时间序列图
    
    参数:
        r: 增长率参数
        x0: 初始值
        n: 迭代次数
        
    返回:
        fig: matplotlib图像对象
    """
    x = iterate_logistic(r, x0, n)  # 获取迭代序列
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(range(n), x, 'b-')  # 绘制时间序列，去除图例
    ax.set_xlabel('Iteration')
    ax.set_ylabel('x')
    ax.set_title(f'Logistic Map Time Series (r = {r})')
    ax.grid(True)
    return fig

def plot_bifurcation(r_min, r_max, n_r, n_iterations, n_discard):
    """
    绘制分岔图
    
    参数:
        r_min: r的最小值
        r_max: r的最大值
        n_r: r的取值个数
        n_iterations: 每个r值的迭代次数
        n_discard: 每个r值丢弃的初始迭代点数
        
    返回:
        fig: matplotlib图像对象
    """
    r = np.linspace(r_min, r_max, n_r)  # 生成r的取值范围
    x_values = []  # 存储x的值
    for ri in r:
        x = 0.5  # 初始值
        for i in range(n_iterations):
            x = ri * x * (1 - x)  # Logistic映射迭代
            if i >= n_discard:  # 丢弃前n_discard次迭代
                x_values.append((ri, x))
    
    fig, ax = plt.subplots(figsize=(10, 6))
    r_plot, x_plot = zip(*x_values)  # 解压r和x的值
    ax.plot(r_plot, x_plot, 'k.', markersize=0.1)  # 绘制分岔图
    ax.set_xlabel('r')
    ax.set_ylabel('x')
    ax.set_title('Bifurcation Diagram of Logistic Map')
    ax.grid(True)
    return fig

def main():
    """主函数"""
    # 时间序列分析
    r_values = [2.0, 3.2, 3.45, 3.6]
    x0 = 0.5
    n = 100
    
    # 创建一幅包含四个子图的图像
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle('Logistic Map Time Series for Different r Values')  # 设置总标题
    
    for i, r in enumerate(r_values):
        x = iterate_logistic(r, x0, n)  # 获取迭代序列
        row = i // 2  # 子图的行索引
        col = i % 2   # 子图的列索引
        axs[row, col].plot(range(n), x, 'b-')  # 绘制时间序列，去除图例
        axs[row, col].set_xlabel('Iteration')
        axs[row, col].set_ylabel('x')
        axs[row, col].set_title(f'r = {r}')
        axs[row, col].grid(True)
    
    plt.tight_layout()  # 调整子图布局
    fig.savefig("logistic_time_series.png", dpi=300)
    plt.close(fig)
    
    # 分岔图分析
    fig = plot_bifurcation(2.5, 4.0, 1000, 1000, 100)
    fig.savefig("bifurcation.png", dpi=300)
    plt.close(fig)

if __name__ == "__main__":
    main()
