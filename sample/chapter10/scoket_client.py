import socket


# bind(协议，地址，端口),AF_INET就是ipv4, AF_INET6就是ipv6, SOCK_DGRAM就是UDP
# AF_INET就是指明我们的类型,SOCK_STREAM就是类型对应的协议
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 第2绑定域名和端口, 这里就指明是我们本机发送的数据了，用127.0.0.1
client.connect(('127.0.0.1', 8000))

while True:

    # 手动输入发送数据
    re_data = input()
    client.send(re_data.encode("utf8"))

    # 接收服务端发来的数据
    data = client.recv(2048)
    # 编码成一个utf-8
    print(data.decode("utf8"))



# 向服务端发送一个数据用send()
# client.send("唐明锐".encode("utf8"))
#
# # 这是接收服务端发送过来的数据
# data = client.recv(1024)
# print(data.decode('utf8'))
#
# client.close()






