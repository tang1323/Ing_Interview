import redis


class redis_utils(object):
    def __init__(self):
        # 全局初始化redis连接，这样就不必要重复的代码了，因为有多处要连接redis，所以这样做
        # decode_responses=True加进来的作用是从redis拿cookies就不再是bytes类型
        self.redis_cli = redis.Redis("127.0.0.1", 6379, decode_responses=True)

    def req_set(self):
        # self.redis_cli.set("name", "zhangsan")
        # self.redis_cli.append("name", "是一个好人")
        # s = self.redis_cli.get("name")
        # print(s)

        # redis创建文件夹，必须是两个key才行，这里是创建一个li文件夹
        self.redis_cli.set("li:li", "tang")
        self.redis_cli.set("li:zhihu", "ta")


if __name__ == "__main__":
    red = redis_utils()
    red.req_set()


















