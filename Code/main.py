import Module.menu as menu  # 菜单
import Module.system_operations as system  # 系统操作
import time
from Module.student import Student


def main():
    students_system = system.SystemOperations()
    menu.system_menu()  # 打印菜单
    try:
        while True:
            choice = input("请输入选择的操作：")
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
            elif choice == "2":
                students_system.check()
            elif choice == "3":
                student_id = input("请输入要删除的学生学号：")
                students_system.delete(student_id)
            elif choice == "4":
                student_id = input("请输入要修改的学生学号：")
                students_system.change(student_id)
            elif choice == "5":
                student_id = input("请输入要查找的学生学号：")
                students_system.find(student_id)
            elif choice == "6":
                students_system.statistics()
            elif choice == "0":
                print("正在退出系统...")
                time.sleep(1)
                students_system.save()
                print("已保存数据，系统已退出")
                break
    except ValueError:
        print("输入格式错误，请确保成绩为数字！")


if __name__ == "__main__":
    main()
