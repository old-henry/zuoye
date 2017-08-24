# 1. 运行程序输出第一级菜单
# 2. 选择一级菜单某项，输出二级菜单，同理输出三级菜单
# 3. 返回上一级菜单和顶部菜单
# 4. 菜单数据保存在文件中"

current_layer = {}
last_layers = []

with open("menu",encoding="utf-8") as f_menu:
    str = f_menu.read() #读取文件里内容
    current_layer = eval(str) #转换为字典

while True:
    for key in current_layer:
        print(key)
    choice = input('>>:').strip()
    if choice in current_layer:  # 进入下一层
        last_layers.append(current_layer)  #将上一层加入列表，待后期返回调用
        current_layer=current_layer[choice] #将下一层更新为当前层

    if choice == 'b':  # 返回上一层
        if last_layers:  # 保证列表不为空
            current_layer = last_layers[-1]  # 取上一层更新为当前层
            last_layers.pop()  # 删除列表的最后一个
    if choice == 'q': break  # 退出
