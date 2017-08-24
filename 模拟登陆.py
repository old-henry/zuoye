# 模拟登陆
#1. 用户输入帐号密码进行登陆
#2. 用户信息保存在文件内
#3. 用户密码输入错误三次后锁定用户"



while True :
    user_name = input("请输入用户名：").strip()
    with open("lock","r",encoding="utf-8") as f_lock:
        for line in f_lock:
            if user_name == line.strip():
                print("该用户已经被锁定:",user_name)
                exit()
    for i in range(3):
        password = input("请输入密码：").strip()
        with open("user",encoding="utf-8") as f_user:
            for line in f_user:
                l=line.strip().split(":")
                if user_name == l[0] and password == l[1] :
                    print("登录成功")
                    print("=======欢迎%s进入系统"%user_name)
                    exit()
            print("用户名或密码错误请重新输入")

    print("输错次数已经3次，该用户已锁定")
    with open("lock", "a", encoding="utf-8") as f_lock:
        f_lock.write(user_name + "\n")
        exit()
