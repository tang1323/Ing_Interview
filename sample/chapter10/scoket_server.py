import socket
import threading


# bind(协议，地址，端口),AF_INET就是ipv4, AF_INET6就是ipv6, SOCK_DGRAM就是UDP
# AF_INET就是指明我们的类型,SOCK_STREAM就是类型对应的协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 第2绑定域名和端口, 0.0.0.0这样可以通过ip访问，如果设置成127.0.0.1通过本机局域网就访问不到了
server.bind(('0.0.0.0', 8000))
# 第3，监听端口
server.listen()
# 第4，点进accept()看，它会返回sock, addr， 所以要等于sock, addr
# 如果写在这里只能接收处理一个请求，如果是多人聊天那就不行了
# 做成一个线程就可以，在while里面
# sock, addr = server.accept()


def handle_sock(sock, addr):
    while True:
        # 接收客户发来的数据
        data = sock.recv(2048)
        # 编码成一个utf-8
        print(data.decode("utf8"))
        # 手动输入发送数据
        re_data = input()

        # 用send()发送到客户端
        sock.send(re_data.encode("utf8"))


while True:
    sock, addr = server.accept()

    # 用线程去处理新接收的连接（用户）
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

    # 第5步就可以从客户端发送的数据, 1024就可以接收多少数据，这是1kb
    # 一次获取1k的数据, 这里接收client端的send()发来的数据
    # data = sock.recv(2048)
    # # 编码成一个utf-8
    # print(data.decode("utf8"))
    #
    # # 手动输入发送数据
    # re_data = input()
    # sock.send(re_data.encode("utf8"))



    # 这是服务端接收数据后向客户端发送数据
    # sock.send("hello {}".format(data.decode("utf8")).encode("utf8"))
    # 一般我们在server是不会关闭服务端的
    # server.close()
    # sock.close()












