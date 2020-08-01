#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫
 
import tkinter as tk  # 使用Tkinter前需要先导入
 
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
def new_task():
	window_sign_up = tk.Toplevel(window)
	window_sign_up.geometry('300x200')
	window_sign_up.title('Sign up window')

# 第5步，在窗口界面设置放置Button按键
b = tk.Button(window, text='新建任务', font=('宋体', 12), width=10, height=1, command=new_task)
b.pack()

# 第6步，主窗口循环显示
window.mainloop()