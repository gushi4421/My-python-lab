class Student:
    # 初始化
    def __init__(self, id, name, chinese, math, english):
        self.id = id
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    # 计算总分
    def total(self):
        return self.chinese + self.math + self.english

    # 计算平均分
    def average(self):
        return self.total() / 3

    # 打印学生信息
    def info(self):
        return f"学号:{self.id},姓名:{self.name},语文:{self.chinese},数学:{self.math},英语:{self.english},总分:{self.total()},平均分:{self.average():.2f}"
