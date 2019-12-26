"""
属性 也叫装饰器
"""


# 需要加的新功能
# 装饰器
def verify_permissions(func):
    def wrapper(*args, **kwargs):
        print("权限验证")
        func(*args, **kwargs)

    return wrapper


# ------------已有的功能
# 进入后台
# 这只是个过度  语法糖
# enter_background = verify_permissions(enter_background)
@verify_permissions
def enter_background(login_id, pwd):
    print("进入后台", login_id, pwd)


# 删除订单
@verify_permissions
def delete_order(id):
    print("删除订单", id)


# 函数式编程   体现开闭原则  闭包
# enter_background = 新功能 + 旧功能  拦截
# 缺点：每次拦截对已有功能的调用（enter_background），不科学
# enter_background = verify_permissions(enter_background)
# delete_order = verify_permissions(delete_order)

# 调用
enter_background('ssk', 1245)
delete_order(1234)
