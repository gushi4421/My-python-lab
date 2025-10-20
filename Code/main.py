import Module.menu as menu  # 菜单
import Module.system_operations as system  # 系统操作
import time
from Module.student import Student


def main():
    students_system = system.SystemOperations()
    menu.system_menu()  # 打印菜单

    while True:
        choice = input("请输入选择的操作：")
        # 1.添加学生成绩
        if choice == "1":
            student_id = input("请输入学生学号：")
            student_name = input("请输入学生姓名：")
            student_chinese = int(input("请输入学生语文成绩："))
            student_math = int(input("请输入学生数学成绩："))
            student_english = int(input("请输入学生英语成绩："))
            students_system.add(
                Student(
                    student_id,
                    student_name,
                    student_chinese,
                    student_math,
                    student_english,
                )
            )
        # 2.查看所有成绩
        elif choice == "2":
            students_system.check()
        # 3.删除学生成绩
        elif choice == "3":
            student_id = input("请输入要删除的学生学号：")
            students_system.delete(student_id)
        # 4.修改学生成绩
        elif choice == "4":
            student_id = input("请输入要修改的学生学号：")
            students_system.change(student_id)
        # 5.查找学生成绩
        elif choice == "5":
            student_id = input("请输入要查找的学生学号：")
            students_system.find(student_id)
        # 6.成绩统计分析
        elif choice == "6":
            students_system.analysis()
        # 7.导入学生成绩
        elif choice == "7":
            import_path = input("请输入需要导入的文件路径：")
            students_system.import_students(import_path)
        # 0.退出系统
        elif choice == "0":
            print("正在退出系统...")
            time.sleep(1)
            students_system.save()
            print("已保存数据，系统已退出")
            break
        else:
            print("请保证输入为数字，且在0-7之间！")


if __name__ == "__main__":
    main()
