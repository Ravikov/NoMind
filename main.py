"""

NoMind有一个构思,利用大量的变量数据构造一个内部状态,内部状态的改变,行为的产生,模拟实际人类的思维
但是这很难实现,或者说目前对于我来说很难实现,依靠大模型进行内部状态的改变,动作与思维,局限性太大,概率不能模仿人脑的决策
这个系统目前我的构思中有以下几个关键点:
    1. 感官. 就像人类一样,能感知到环境,且环境会影响人的决策,NoMind应该引入环境参数,比如温度这些的
    2. 记忆. 不能是传统的文字,上下文记忆,而应该是一种像人脑电信号一样的记忆方式,比如向量,但我学识尚浅,还不知道如何实现
    3. 自主性. 摒弃多数智能实现的方式,输入-处理-输出的管道逻辑,系统应该有内部决策,决定何时进行行动,可以自主发起行动,也可以选择
              不处理外部的输入,形似自我意识吧
    4. 快速响应. 用轻量的计算带来快速的响应,可以形成条件反射,不应有太大的延迟
    ......
以上仅是关键点,实际实现可能要引入更多
目前这个想法于我还难以实现
2026.7.2 Ravikov

"""

class MindBot:

    def __init__(self):
        self.hobby   = ['coding']     #爱好
        self.state   = 'thinking'     #当前状态
        self.mood    = [0.5,0.5,0.5]  #三维向量,兴奋度-开心-紧张
        self.dislike = ['running all day']  #不喜欢的

class Environment:
    """环境参数"""

    def __init__(self):
        self.season      = 'summer' #季节
        self.temperature = 30       #环境温度
        self.humidity    = 50       #环境湿度
        self.weather     = 'sunny'  #天气
        self.light       = 5        #光照强度,1~10
        self.location    = 'home'   #当前位置,可以细分,如bedroom
        self.noise       = 3        #噪声强度


#---------- A example from DeepSeek ----------
#以下是deepseek写的简易原型,仅供参考,与上文没有直接联系
import numpy as np
import time
import threading

class NoMindPrototype:
    def __init__(self):
        # 状态向量：3 维，初始随机
        self.state = np.array([0.5, 0.5, 0.5])
        self.running = True
        
    def evolve(self):
        """状态自动演化：每个维度做微小随机游走 + 向中心回归"""
        # 随机扰动
        noise = np.random.normal(0, 0.05, size=3)
        # 向中心 (0.5, 0.5, 0.5) 回归
        drift = (0.5 - self.state) * 0.02
        # 更新状态，并限制在 0~1 之间
        self.state = np.clip(self.state + noise + drift, 0, 1)
    
    def respond(self, user_input):
        """根据当前状态生成回应（不用 LLM，纯规则）"""
        # 用状态向量的平均值作为“温度”
        temp = np.mean(self.state)
        
        # 用状态向量的方差作为“混乱度”
        chaos = np.var(self.state)
        
        if temp > 0.7:
            mood = "兴奋"
        elif temp > 0.4:
            mood = "平静"
        else:
            mood = "低沉"
            
        if chaos > 0.05:
            tone = "跳跃"
        else:
            tone = "稳定"
            
        return f"[状态: {mood}, {tone}] 你说: '{user_input}'  | 状态值: {self.state.round(3)}"
    
    def state_loop(self):
        """后台线程：持续更新状态"""
        while self.running:
            self.evolve()
            time.sleep(1)
    
    def run(self):
        # 启动后台状态更新线程
        thread = threading.Thread(target=self.state_loop)
        thread.daemon = True
        thread.start()
        
        print("NoMind 原型已启动。输入文字观察响应，输入 'quit' 退出。")
        print("状态每 1 秒自动变化一次，影响我的回应方式。\n")
        
        while self.running:
            try:
                user_input = input(">>> ")
                if user_input.lower() == 'quit':
                    self.running = False
                    break
                print(self.respond(user_input))
                print()
            except KeyboardInterrupt:
                break
        
        print("原型已停止。")

if __name__ == "__main__":
    prototype = NoMindPrototype()
    prototype.run()