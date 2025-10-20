import os
from Module.student import Student


def ensure_data_directory(file_path):
    """确保数据目录存在"""
    data_dir = os.path.dirname(file_path)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)


def load_students(file_path="Data/grades.txt"):
    students = []
    try:
        # 确保目录存在
        ensure_data_directory(file_path)

        # 读取文件
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:  # 跳过空行
                    try:
                        # 解析数据行：学号,姓名,语文,数学,英语
                        data = line.split(",")
                        if len(data) == 5:
                            student = Student(
                                data[0],  # 学号
                                data[1],  # 姓名
                                int(data[2]),  # 语文成绩
                                int(data[3]),  # 数学成绩
                                int(data[4]),  # 英语成绩
                            )
                            students.append(student)

                    except (ValueError, IndexError):
                        # 跳过格式错误的数据行
                        continue

        print(f"成功加载 {len(students)} 名学生数据")
        return students

    except Exception as e:
        print(f"加载数据文件时发生错误: {e}")
        return []


def save_students(students, file_path="Data/grades.txt"):
    try:
        ensure_data_directory(file_path)
        with open(file_path, "w", encoding="utf-8") as file:
            for student in students:
                # 将学生数据转换为纯文本格式：学号,姓名,语文,数学,英语
                line = f"{student.id},{student.name},{student.chinese},{student.math},{student.english}\n"
                file.write(line)

        print(f"成功保存 {len(students)} 名学生数据到 {file_path}")
        return True

    except Exception as e:
        print(f"保存数据时发生错误: {e}")
        return False
