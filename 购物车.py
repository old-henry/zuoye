# 1. 商品信息- 数量、单价、名称
# 2. 用户信息- 帐号、密码、余额
# 3. 用户可充值
# 4. 购物历史信息
# 5. 允许用户多次购买，每次可购买多件
# 6. 余额不足时进行提醒
# 7. 用户退出时 ，输出档次购物信息
# 8. 用户下次登陆时可查看购物历史
# 9. 商品列表分级
import sys,os

l_list=[]
choice_list=[]
shopping_car={}
f_list=[]
while True:
    #判断用户登录部分
    with open("user_shopping",encoding="utf-8") as f_user:
        user_name = input("请输入用户名：>>>").strip()
        pass_word = input("请输入密码：>>>").strip()
        for line1 in f_user:
            username,password,money,flag = line1.strip().split(":")
            f_username = "shopping_history" + user_name
            if username == user_name and password == pass_word :
                print("欢迎您来购物%s,您的余额为%s。"%(user_name,money))
                balance = int(money)
                if flag == "#":
                    m = input("您是否查看之前的购物清单，查看请输入y，否则输入n").strip()
                    if m == "y":
                        print('您之前购买过以下商品'.center(50, '-'))
                        print("%s\t%s\t%s\t%s" % ("商品编号", "商品名称", "商品单价", "库房数量"))
                        with open(f_username,encoding='utf-8') as f_his:
                            for line in f_his:
                                print(line)
                break
        else:
            print("用户名或密码错误")
            continue
    # 开始购物部分
    with open("commodity",encoding="utf-8") as commodity_list:
        while True:
            for line in commodity_list:
                f_list.append(line.strip())
                l_list.append(f_list)
                f_list = []
            print('您可以购买以下商品'.center(50, '-'))
            print("%s\t%s\t%s\t%s" % ("商品编号", "商品名称", "商品单价", "库房数量"))

            for key in l_list:
                print(key)
            for key in range(len(l_list)):
                cu_list = l_list[key]
                u = str(cu_list[0])
                choice_list.append(u.split(","))
            print("您的当前账户余额为%s"%balance)
            num = input('请输入商品编号，或者q直接退出').strip()
            if num == "q":
                with open("user_shopping", encoding="utf-8") as f_user,open("user_shop_back",'a+', encoding="utf-8") as f_user_back:
                    for line in f_user :
                        if line == line1:
                            date = user_name+":"+pass_word+":"+str(balance)+":"+"#"
                            f_user_back.write(date+"\n")
                        else:
                            f_user_back.write(line.strip()+"\n")
                if os.path.exists("shopping.back"):
                    os.remove("shopping.back")
                else:
                    os.rename("user_shopping","shopping.back")
                    os.rename("user_shop_back","user_shopping")
                print('您以及购买以下商品'.center(50, '-'))
                total = 0
                print('商品编号     商品名称      单价    购买数量')
                with open(f_username, 'a+', encoding='utf-8') as f_history:
                    f_history.write("\n"+'商品编号     商品名称      单价    购买数量')
                    for key in shopping_car:
                        msg = ("%s\t\t\t%s\t\t\t%s\t\t%d"% (key,shopping_car[key][0],shopping_car[key][1],shopping_car[key][2]))
                        print(msg)
                        total += int(shopping_car[key][1]) * int(shopping_car[key][2])
                        f_history.write('\n' + msg)
                    f_history.write("\n" + "您上次共消费" + str(total))
                print("您本次共消费"+str(total))
                sys.exit()
            choice = int(num)-1
            if choice > len(choice_list):
                print("您输入的商品编号错误请重新输入")
                continue
            p = choice_list[choice]
            print("您选择购买的是:", p[1])
            choice_num = int(input("请输入购买的数量").strip())
            if choice_num <= int(p[3]):
                if p[0] in shopping_car:
                     shopping_car[p[0]][2]+=1
                else:
                    shopping_car[p[0]]=[p[1],p[2],choice_num]
                    print('您已购买以下商品'.center(50, '-'))
                    print(shopping_car)
                if balance >= int(p[2])*int(choice_num):
                    com_num = int(p[3])
                    com_num -= int(com_num)
                    p[3] = str(com_num)
                    balance = balance - int(p[2])*int(choice_num)
                    print(balance)
                else:
                    choice = input("对不起您的余额不足，无法购买商品.如果需要充值请按y,如果重新选择商品请按c，如果退出购买请按q").strip()
                    if choice == "c": continue
                    if choice == "y":
                        chongzhi = int(input("请输入充值金额>>>").strip())
                        balance +=chongzhi
                        del shopping_car[p[0]]
                        continue
            else:
                print("对不起，我们的" + str(p[1]) + "库存不足，请重新选择商品。")
                print('您已购买以下商品'.center(50, '-'))
                print(shopping_car)