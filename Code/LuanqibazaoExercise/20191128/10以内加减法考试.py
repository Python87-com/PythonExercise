"""
    10以内加法考试 MVC思想
    需求：1、界面选项菜单： 1 加法考试 2 减法考试 3 比大小考试 4 查看错题
        2、初始成绩为0，每次考试提取20道题目，答对+5分，答错不加分
"""
import random


# 模型 model
class OperationModel:
    # def __init__(self):
    #     self.__list_add = []
    # __list_add = []
    def num_create(self):
        x1 = random.randint(1, 6)
        # self.__list_add.append(x1)
        y1 = random.randint(1, 6)
        # self.__list_add.append(y1)
        # return self.__list_add
        return [x1, y1]


# 逻辑控制
class OperationControl:
    # 类变量 错题起始编号
    __init_id = 1

    def __init__(self):
        # self.__user_count = 0
        # 错题
        self.__user_error_exercise = {}

    @property
    def list_error(self):
        return self.__user_error_exercise

    # # 成绩类变量()
    user_count = 0

    # 加法                      列表        用户输入的数据
    def add_operation(self, list_target, user_input):
        add_target = list_target[0] + list_target[1]
        # 如果答案是正确的 则 加5分 返回给类变量 user_count
        if user_input == add_target:
            OperationControl.user_count += 5
        else:
            # 如果答案是错的，则存入字典中
            self.__user_error_exercise[self.__init_id] = "{0} + {1} = {2}".format(list_target[0], list_target[1],
                                                                                  user_input)

    def __generate_id(self):
        OperationControl.__init_id += 1
        return OperationControl.__init_id

    # 减法
    def sub_operation(self, list_target, user_input):
        sub_target = list_target[0] - list_target[1]
        self.__init_id = self.__generate_id()
        # 如果答案是正确的 则 加5分 返回给类变量 user_count
        if user_input == sub_target:
            OperationControl.user_count += 5
        else:
            # 如果答案是错的，则存入字典中
            self.__user_error_exercise[self.__init_id] = "{0} - {1} = {2}".format(list_target[0], list_target[1],
                                                                                  user_input)

    # 比大小
    def big_or_small_operation(self):
        pass

    # 遍历错题
    def for_operation(self):
        # self.__user_error_exercise
        # if len(self.__user_error_exercise) == 0:
        #     print("暂无错题哦！！")
        # return self.__user_error_exercise
        return self.__user_error_exercise


# 界面视图 View
class OperationView:
    def __init__(self):
        self.__manager = OperationControl()
        self.__list_num = OperationModel()
        self.__count = 0  # 执行次数

    def __display_menu(self):
        print("小朋友，欢迎来到学前模拟考试界面,请在家长的陪同下考试哦！！！")
        print("1 加法考试 2 减法考试 3 比大小考试 4 查看错题")
        print("*" * 50)

    def __select_menu(self):
        userInput = input("请输入你的选项:")
        if userInput == '1':
            self.__add_oper()
        elif userInput == '2':
            self.__sub_oper()
        elif userInput == '3':
            self.__big_small_oper()
        elif userInput == '4':
            self.display_wrong_questions()

    def main(self):
        """
            程序入口
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __add_oper(self):
        count = 0
        while count < 5:
            # 从模型中获取随机的2个数字
            target = self.__list_num.num_create()
            # 显示在界面上
            print("{0} + {1} = (   )".format(target[0], target[1]), end=" ")
            # 获取用户的答案
            user_add_input = int(input("本题的答案是多少呢？请仔细想想在写答案哦："))
            # 返回逻辑层处理
            self.__manager.add_operation(target, user_add_input)
            # self.__count += 1  # 以上操作执行成功后 执行次数 +1
            count += 1
        # 显示最终成绩
        user_result = self.__manager.user_count
        print("小朋友，你的最终成绩是：%s 分。" % user_result)

    def __sub_oper(self):
        count = 0
        while count < 20:
            # 从模型中获取随机的2个数字
            target = self.__list_num.num_create()
            # 显示在界面上
            if target[0] > target[1]:
                print("{0} - {1} = (   )".format(target[0], target[1]), end=" ")
            else:
                continue
            # 获取用户的答案
            user_add_input = int(input("本题的答案是多少呢？请仔细想想在写答案哦："))
            # 返回逻辑层处理
            self.__manager.sub_operation(target, user_add_input)
            # self.__count += 1  # 以上操作执行成功后 执行次数 +1
            count += 1
        # 显示最终成绩
        user_result = self.__manager.user_count
        print("小朋友，你的最终成绩是：%s 分。" % user_result)

    def __big_small_oper(self):
        pass

    def display_wrong_questions(self):
        re = self.__manager.for_operation()
        for key, value in re.items():
            print("错误的题目入下：")
            print(key, value)

    def display_wrong_questions_by_score(self):
        # 遍历 错题字典   注意，在选择菜单的时候，要清空上一次考试的成绩和字典中存入的数据
        # self.__manager.for_operation()
        # self.display_wrong_questions(self.__manager.list_error)
        pass


# 调用
view = OperationView()
view.main()
