# Author:Jason.wang

'''readme
用户信息存放在磁盘文件中
登陆时读取文件内容验证用户密码
密码连续输错三次锁定用户
'''

#读取文件 注意:
# 1.文件路径需用 /
# 2.open打开文件后一定要close关闭
# 3.参数 r 读取  w 覆盖写 w+ 追加写
def isLock():
    try:
        user_lock = open('C:/Users/Think/Desktop/学习笔记/python/源码/user_lock.txt', 'r')
        for line in user_lock:
            if user_name == line.replace("\n",""):
                print("用户已锁定")
                return True
            else:
                return False
    finally:
        user_lock.close()


def login(user_name,pw,n):
    if isLock():
        exit()
    else:
        try:
            user_data = open('C:/Users/Think/Desktop/学习笔记/python/源码/user_data.txt','r')
            for line in user_data:
                wn = 0 #连续输错次数
                name_ok = line.split(":")[0]
                pw_ok = line.split(":")[1]
                if user_name == name_ok:
                    while wn<3:
                        if pw == pw_ok.replace("\n",""):
                            print("登录成功!")
                            break
                        else:
                            wn += 1
                            print("密码错误！（第%s次，超过三次将被锁定）" %wn)
                            if wn>=3:
                                print("用户已被锁定")
                                user_lock = open('C:/Users/Think/Desktop/学习笔记/python/源码/user_lock.txt', 'w+')
                                user_lock.write(name_ok)
                                user_lock.close()
                                break
                            else:
                                pw = input("密码： ")
                    n += 1
            if n==0:
                print("用户不存在")
        finally:
            user_data.close()



user_name = input("用户名： ")
pw = input("密码：")
n = 0 #判断是否存在用户的计数器
login(user_name,pw,n)
