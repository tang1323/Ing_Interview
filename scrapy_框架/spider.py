
# -------------------------爬虫的原理--------------------
"""
1.首先spider拿到url封装成请求的对象后给引擎(engine)
2.引擎(engine)拿到对象后，将全部交给调度器(scheduler)
3.交给调度器(scheduler)拿到所有请求对象后，用过滤器过滤掉重复的url，
    去重后将所有url对应的请示压到队列中
    之后调度器(scheduler)调度出其中一个请求对象，再次交给引擎(engine)

4.引擎(engine)将调度出的一个请求对象，并交给下载器(Downloader)，是所有组件中负担最大的
5.下载器(Downloader)拿到请求对象去互联网下载数据
6.数据下载成功会放在response中，然后response会被交给下载器(Downloader)
7.下载器将response交给引擎
8.引擎将response交给spiders
9.spiders拿到response后调用回调方法进行数据解析,
    解析成功后生成item,item(在这里把数据的一些不要的数据清理掉，也可以加上一些数据)
    随后spiders将item交给引擎(engine)
10.引擎(engine)把item里面处理的数据拿到管道(pipelines)中,然后就可以放到数据库里做持久化保存
"""

















