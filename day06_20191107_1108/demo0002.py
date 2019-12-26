import turtle

# 画一个奥运五环

turtle.showturtle()          # 显示箭头

turtle.width(10)             # 设置划线的粗细
turtle.color("blue")         # 画笔颜色改为 蓝
turtle.circle(50)            # 画直径100像素的圆
turtle.penup()               # 抬笔
turtle.goto(120, 0)          # 去坐标
turtle.pendown()             # 下笔
turtle.color("black")        # 画笔颜色改为 黑
turtle.circle(50)            # 画直径50像素的圆

turtle.penup()               # 抬笔
turtle.goto(240, 0)          # 去坐标
turtle.pendown()             # 下笔
turtle.color("red")          # 画笔颜色改为 红
turtle.circle(50)            # 画直径50像素的圆red

turtle.penup()               # 抬笔
turtle.goto(60, -37)         # 去坐标
turtle.pendown()             # 下笔
turtle.color("orange")       # 画笔颜色改为 橙
turtle.circle(50)            # 画直径50像素的圆

turtle.penup()               # 抬笔
turtle.goto(180, -37)        # 去坐标
turtle.pendown()             # 下笔
turtle.color("green")        # 画笔颜色改为 绿
turtle.circle(50)            # 画直径50像素的圆