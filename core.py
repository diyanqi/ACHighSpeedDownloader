#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import tkinter as tk
import sys
import time

from ThreadDownload import *


def show_process(dl):
    while dl.get_complete_rate() < 1:
        complete_rate = int(dl.get_complete_rate()*100)  
        print('\r' + '下载中···（已下载' + str(complete_rate) + '%）', end='', flush=True)
        time.sleep(0.01)


def main():
    try:   
        Link = 'https://img-blog.csdnimg.cn/20190719150546671.jpg'
        file_path = 'C:\\Users\\diyan\\Desktop\\A.C.高速下载器\\保存目录\\a.jpg'
        thread_number = 8
        Link = input('[+]' + 'Link: ')
        file_path = input('[+]' + 'File Path: ')
        thread_number = input('[+]' + 'Thread Number: ')
        thread_number = int(thread_number)
        dl = Download(Link, file_path, thread_number)
        dl.download()
        print('\n开始下载!')
        show_process(dl)
        print('\r' + '下载中···（已下载' + '100%)', end='', flush=True)
        print('\n下载完成!')
    except Exception:
            print('Parameter Setting Error')
            sys.exit(1)

if __name__=='__main__':
        main()
