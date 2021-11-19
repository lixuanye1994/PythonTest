import os
url = input("复制视频地址:")
space = ' '
path = '-o D:/video'
order = 'you-get' + space + path + space + url
print(f"当前获取指令 {order}")
print("指令正确，正在下载中....")
print("----------------------------------")

print(os.system(order))
