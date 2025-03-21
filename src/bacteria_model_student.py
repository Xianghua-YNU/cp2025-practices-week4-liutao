# bacteria_model_solution.py
import numpy as np
import matplotlib.pyplot as plt

class BacteriaModel:
    def __init__(self, A, tau):
        self.A = A
        self.tau = tau

    def v_model(self, t):
        """V(t) = 1 - e^(-t/τ)"""
        return 1 - np.exp(-t/self.tau)

    def w_model(self, t):
        """W(t) = A(e^(-t/τ) - 1 + t/τ)"""
        return self.A * (np.exp(-t/self.tau) - 1 + t/self.tau)

    def plot_models(self, t):
        """绘制V(t)和W(t)模型曲线"""
        v = self.v_model(t)
        w = self.w_model(t)
        
        plt.figure(figsize=(8, 5))
        plt.plot(t, v, 'b-', label=f'V(t) (τ={self.tau})')
        plt.plot(t, w, 'r--', label=f'W(t) (A={self.A}, τ={self.tau})')
        plt.xlabel('Time (hours)')
        plt.ylabel('Response')
        plt.title('Bacteria Growth Models')
        plt.grid(alpha=0.3)
        plt.legend()
        plt.show()

def load_bacteria_data(filepath):
    """加载实验数据文件"""
    try:
        # 正确加载二维数组数据
        data = np.loadtxt(filepath, delimiter=',')
        return data[:, 0], data[:, 1]  # 第一列为时间，第二列为响应值
    except Exception as e:
        print(f"数据加载失败: {str(e)}")
        return None, None

def main():
    # 初始化模型参数（与原代码完全一致）
    model = BacteriaModel(A=1.0, tau=2.0)
    
    # 生成时间序列（0-10小时，100个点）
    t = np.linspace(0, 10, 100)
    
    # 绘制模型曲线
    model.plot_models(t)
    
    # 加载实验数据
    time_data, response_data = load_bacteria_data('g149novickA.txt')
    
    # 绘制实验数据点（保持原样式）
    if time_data is not None:
        plt.figure(figsize=(8, 5))
        plt.scatter(time_data, response_data, 
                   edgecolor='black', facecolor='none',
                   label='Experimental Data')
        plt.xlabel('Time (hours)')
        plt.ylabel('Response')
        plt.title('Experimental Data Plot')
        plt.grid(alpha=0.3)
        plt.legend()
        plt.show()

if __name__ == "__main__":
    main()
