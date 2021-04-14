
# requests -> urllib -> socket
import socket
from urllib.parse import urlparse


def get_url(url):
    # 通过sockety请求html
    url = urlparse(url)
    # netloc()是帮我们做了解析，提取主域名
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立连接
    # AF_INET就是指明我们的类型,SOCK_STREAM就是类型对应的协议
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 第2绑定域名和端口, 0.0.0.0这样可以通过ip访问，如果设置成127.0.0.1通过本机局域网就访问不到了
    client.connect((host, 80))

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode("utf8")
    print(data)
    client.close()


if __name__ == "__main__":
    get_url("http://www.baidu.com")

