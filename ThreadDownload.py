# 文件名：ThreadDownload.py
import threading
from urllib.request import *


class Download:
    def __init__(self, link, file_path, thread_num):
        # 下载路径
        self.link = link
        # 保存位置
        self.file_path = file_path
        # 使用多少线程
        self.thread_num = thread_num
        # 初始化threads数组
        self.threads = []

    def download(self):
        req = Request(url=self.link, method='GET')
        req.add_header('Accept', '*/*')
        req.add_header('Charset', 'UTF-8')
        req.add_header('Connection', 'Keep-Alive')
        f = urlopen(req)
        # 获取要下载的文件的大小
        self.file_size = int(dict(f.headers).get('Content-Length', 0))
        f.close()
        # 计算每个线程要下载的资源的大小
        current_part_size = self.file_size // self.thread_num + 1
        for i in range(self.thread_num):
            # 计算每个线程下载的开始位置
            start_pos = i * current_part_size
            # 每个线程使用一个wb模式打开的文件进行下载
            t = open(self.file_path, 'wb')
            t.seek(start_pos, 0)
            # 创建下载线程
            td = ThreadDownload(self.link, start_pos, current_part_size, t)
            self.threads.append(td)
            td.start()

    # 获下载的完成百分比
    def get_complete_rate(self):
        sum_size = 0
        for i in range(self.thread_num):
            sum_size += self.threads[i].length
        return sum_size / self.file_size

class ThreadDownload(threading.Thread):
    def __init__(self, link, start_pos, current_part_size, current_part):
        super().__init__() 
        # 下载路径
        self.link = link
        # 当前线程的下载位置
        self.start_pos = start_pos
        # 定义当前线程负责下载的文件大小
        self.current_part_size = current_part_size
        # 当前文件需要下载的文件快
        self.current_part = current_part
        # 定义该线程已经下载的字节数
        self.length = 0
    
    def run(self):
        req = Request(url = self.link, method='GET')
        req.add_header('Accept', '*/*')
        req.add_header('Charset', 'UTF-8')
        req.add_header('Connection', 'Keep-Alive')

        f = urlopen(req)
        # 跳过self.start_pos个字节，表明该线程只负责下载自己负责的那部分内容
        for i in range(self.start_pos):
            f.read(1)
        # 读取网络数据，并写入本地
        while self.length < self.current_part_size:
            data = f.read(1024)
            if data is None or len(data) <= 0:
                break
            self.current_part.write(data)
            # 累计该线程下载的总大小
            self.length += len(data)
        self.current_part.close()
        f.close()
