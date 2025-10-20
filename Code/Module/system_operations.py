from Module.student import Student
from Module.files_operations import (
    load_students,
    save_students,
    import_files,
)  # 导入文件操作
import Module.menu as menu


class SystemOperations:
    def __init__(self):
        self.students = load_students()

    # 保存学生成绩至grades.txt文件
    def save(self):
        save_students(self.students)

    # 1.添加学生成绩
    def add(self, student: Student):
        # 学号重复检测
        for stu in self.students:
            if stu.id == student.id:
                print("学号已存在，添加失败")
                return
        self.students.append(student)
        print("添加成功")

    # 2.查看所有成绩
    def check(self):
        if len(self.students) == 0:
            print("系统中暂无学生信息")
            return
        for stu in self.students:
            print(stu.info())

    # 3.删除学生成绩
    def delete(self, id):
        # 学生存在检测
        for stu in self.students:
            if stu.id == id:
                self.students.remove(stu)
                print("删除成功")
                return
        print("系统中无该学生，删除失败")

    # 4.修改学生成绩
    def change(self, id):
        # 学生存在检测
        for stu in self.students:
            if stu.id == id:
                stu.info()
                menu.change_menu()  # 打印菜单
                choice = input("请输入选择的操作：")
                if choice == "1":
                    new_id = input("请输入新的学号：")
                    # 学号重复检测
                    for s in self.students:
                        if s.id == new_id:
                            print("学号已存在，修改失败")
                            return
                    stu.id = new_id
                    print("学号修改成功")
                elif choice == "2":
                    new_name = input("请输入新的姓名：")
                    stu.name = new_name
                    print("姓名修改成功")
                elif choice == "3":
                    new_chinese = int(input("请输入新的语文成绩："))
                    stu.chinese = new_chinese
                    print("语文成绩修改成功")
                elif choice == "4":
                    new_math = int(input("请输入新的数学成绩："))
                    stu.math = new_math
                    print("数学成绩修改成")
                elif choice == "5":
                    new_english = int(input("请输入新的英语成绩："))
                    stu.english = new_english
                    print("英语成绩修改成功")
                else:
                    print("返回上一级")
                return
        print("系统中无该学生，修改失败")

    # 5.查找学生成绩
    def find(self, id):
        # 学生存在检测
        for stu in self.students:
            if stu.id == id:
                print(stu.info())
                return
        print("未找到该学生")

    # 6.成绩统计分析
    def analysis(self):
        len_students = len(self.students)
        if len_students == 0:
            print("系统中暂无学生信息")
            return
        # 各科总分初始化
        total_chinese = 0
        total_math = 0
        total_english = 0
        # 最高分进行初始化
        max_chinese = self.students[0].chinese
        max_math = self.students[0].math
        max_english = self.students[0].english

        # 最低分进行初始化
        min_chinese = self.students[0].chinese
        min_math = self.students[0].math
        min_english = self.students[0].english

        for stu in self.students:
            # 统计各科总分
            total_chinese += stu.chinese
            total_math += stu.math
            total_english += stu.english
            # 查找各科最高分
            max_chinese = max(max_chinese, stu.chinese)
            max_math = max(max_math, stu.math)
            max_english = max(max_english, stu.english)
            # 查找各科最低分
            min_chinese = min(min_chinese, stu.chinese)
            min_math = min(min_math, stu.math)
            min_english = min(min_english, stu.english)
        # 求各科平均分
        average_chinese = total_chinese / len_students
        average_math = total_math / len_students
        average_english = total_english / len_students
        # 打印
        print(
            f"语文：总分：{total_chinese},平均分：{average_chinese:.2f},最高分：{max_chinese},最低分：{min_chinese}"
        )
        print(
            f"数学：总分：{total_math},平均分：{average_math:.2f},最高分：{max_math},最低分：{min_math}"
        )
        print(
            f"英语：总分：{total_english},平均分：{average_english:.2f},最高分：{max_english},最低分：{min_english}"
        )

    # 7.导入学生成绩
    def import_students(self, import_file_path):
        extend_students = []
        extend_students = import_files(import_file_path, extend_students)
        self.students.extend(extend_students)
        print(f"成功从 {import_file_path} 中导入 {len(extend_students)} 名学生成绩")
