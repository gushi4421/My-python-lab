"""
菜单显示
"""


# 系统菜单打印
def system_menu():
    print("#" * 20)
    print("  学生成绩管理系统")
    print("#" * 20)
    print("-" * 20)
    print("1.添加学生成绩")
    print("2.查看学生成绩")
    print("3.删除学生成绩")
    print("4.修改学生成绩")
    print("5.查找学生成绩")
    print("6.成绩统计分析")
    print("0.退出系统")
    print("-" * 20)


# 修改菜单打印
def change_menu():
    print("-" * 20)
    print("1.修改学生学号")
    print("2.修改学生姓名")
    print("3.修改学生语文成绩")
    print("4.修改学生数学成绩")
    print("5.修改学生英语成绩")
    print("0.无修改，返回上级菜单")
    print("-" * 20)
