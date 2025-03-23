import numpy as np
import matplotlib.pyplot as plt

class HIVModel:
    def __init__(self, A, alpha, B, beta):
        self.A = A
        self.alpha = alpha
        self.B = B
        self.beta = beta  # TODO: 初始化模型参数
        pass

    def viral_load(self, time):
        return self.A * np.exp(-self.alpha * time) + self.B * np.exp(-self.beta * time)# TODO: 计算病毒载量

    def plot_model(self, time):
        viral_load = self.viral_load(time)
        plt.plot(time, viral_load, label=label)# TODO: 绘制模型曲线
        pass

def load_hiv_data(filepath):
    data = np.loadtxt(filepath, delimiter=',')
    time_data = data[:, 0]
    viral_load_data = data[:, 1]
    return time_data, viral_load_data# TODO: 加载HIV数据

def main():
    # 1.1 探索模型
    # 生成时间序列
    time = np.linspace(0, 1, 11)

    # 设置模型参数
    A = 1000
    alpha = 5
    B = 0  # 先将B设为0
    beta = 1  # 即使B为0，beta也需要一个值

    # 创建HIV模型实例
    hiv_model = HIVModel(A, alpha, B, beta)

    # 绘制模型曲线
    hiv_model.plot_model(time)
    plt.xlabel('Time')
    plt.ylabel('Viral Load')
    plt.title('HIV Viral Load Model')
    plt.legend()
    plt.show()

    # 1.2 拟合实验数据
    # 加载实验数据
    time_data, viral_load_data = load_hiv_data('HIVseries.csv')

    # 绘制实验数据
    plt.scatter(time_data, viral_load_data, label='Experimental Data', color='red')
    plt.xlabel('Time (days)')
    plt.ylabel('Viral Load')
    plt.title('HIV Viral Load Experimental Data')
    plt.legend()
    plt.show()

    # 拟合模型
    # 初始猜测参数
    A_guess = 1200
    alpha_guess = 0.6
    B_guess = 400
    beta_guess = 0.2

    # 创建拟合模型实例
    fitted_model = HIVModel(A_guess, alpha_guess, B_guess, beta_guess)

    # 绘制拟合模型和实验数据
    fitted_model.plot_model(time_data, label='Fitted Model')
    plt.scatter(time_data, viral_load_data, label='Experimental Data', color='red')
    plt.xlabel('Time (days)')
    plt.ylabel('Viral Load')
    plt.title('HIV Viral Load Model Fitting')
    plt.legend()
    plt.show()

    # 作业部分
    # a. 调整参数直到模型与数据匹配
    # 你可以手动调整 A_guess, alpha_guess, B_guess, beta_guess 的值
    # 例如：
    A_guess = 1500
    alpha_guess = 0.7
    B_guess = 300
    beta_guess = 0.15

    # 重新拟合模型
    fitted_model = HIVModel(A_guess, alpha_guess, B_guess, beta_guess)
    fitted_model.plot_model(time_data, label='Adjusted Model')
    plt.scatter(time_data, viral_load_data, label='Experimental Data', color='red')
    plt.xlabel('Time (days)')
    plt.ylabel('Viral Load')
    plt.title('Adjusted HIV Viral Load Model Fitting')
    plt.legend()
    plt.show()

    # b. 分析参数关系，减少自由参数
    # 例如，假设 beta > alpha，可以根据长期行为固定 alpha 和 beta，然后调整 A 和 B
    # 这里假设 alpha 和 beta 已经固定，只调整 A 和 B
    A_guess = 1300
    B_guess = 350
    fitted_model = HIVModel(A_guess, alpha_guess, B_guess, beta_guess)
    fitted_model.plot_model(time_data, label='Final Model')
    plt.scatter(time_data, viral_load_data, label='Experimental Data', color='red')
    plt.xlabel('Time (days)')
    plt.ylabel('Viral Load')
    plt.title('Final HIV Viral Load Model Fitting')
    plt.legend()
    plt.show()

    # c. 比较 T 细胞感染率的倒数 1/alpha 与潜伏期
    # HIV 潜伏期大约为 10 年，即 3650 天
    latency_period = 3650
    alpha_inverse = 1 / alpha_guess
    print(f"T 细胞感染率的倒数 1/alpha: {alpha_inverse} 天")
    print(f"HIV 潜伏期: {latency_period} 天")
    if alpha_inverse < latency_period:
        print("1/alpha 小于潜伏期，表明感染率较高。")
    else:
        print("1/alpha 大于潜伏期，表明感染率较低。")

if __name__ == "__main__":
    main()
