"""
    功能：欧拉螺线（羊角螺线）
    作者：焦奎洸
    版本：3.0
    2.0新增功能：运算次数增大，呈现螺旋
    3.0新增功能：火树银花
    日期：2020/5/16
"""
import turtle
# 引入turtle绘图库


def draw_clothoid_line(fun_length, fun_angle, fun_times):
    """
    功能：绘图函数（迭代）
    :param fun_length: 函数内部单位长度
    :param fun_angle:函数内部单位角度
    :param fun_times:函数循环次数
    :return: 循环次数
    """
    for i in range(1, fun_times):
        turtle.left(fun_angle)
    turtle.forward(fun_length)
    fun_angle += 1
    set_position = turtle.position()
    set_direction = turtle.towards(0, 0)
    print(set_position)
    print(set_direction)


def main():
    """
        主函数：控制迭代次数
    :return:
    """
    # 修改项目
    # 迭代次数
    cycle_times = 200
    # 长度
    unit_length = 5
    # 角度
    unit_angle = 7
    # 速度（0， 10）
    unit_speed = 9

    turtle.title("Welcome to see the clothoid lines!")

    # 画笔宽度
    turtle.pensize(2)
    # 设置画笔颜色
    turtle.pencolor("red")
    # 初始绘画
    # 定位
    turtle.penup()
    turtle.setpos(50, 0)
    turtle.pendown()
    # 直线
    turtle.forward(unit_length)
    # 画笔速度
    turtle.speed(unit_speed)

    # 循环计时器
    add_cycle_times = 1
    # 循环使用绘图
    while add_cycle_times < cycle_times:
        draw_clothoid_line(unit_length, unit_angle, add_cycle_times)
        add_cycle_times += 1

    turtle.exitonclick()


if __name__ == '__main__':
    main()
