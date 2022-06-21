# while True 无限循环，用户break决定什么时候结束循环
import cards_tools

while True:

    # 显示功能菜单
    cards_tools.show_menu()

    action_str = input("请选择希望执行的操作:")
    print("您选择的操作是【%s】" % action_str)

    # 123 继续操作  0 退出  其他 输入错误
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            cards_tools.new_card()
            # 新增名片

        elif action_str == "2":
            cards_tools.show_all()
            # 显示全部

        elif action_str == "3":
            cards_tools.search_card()
            # 查询名片

        pass
    # 如果在开发程序时，不希望立刻编写分支内部的程序，用pass作为一个占位符
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print("您输入的不正确，请从新选择")
