# _*_ coding:UTF-8 _*_
import win32api
import win32con
import win32gui
from ctypes import *
import time
import msvcrt
import threading
from time import sleep
import sys
import ctypes.wintypes

    
EXIT = False
def mouse_click(x=None,y=None):
	if not x is None and not y is None:
		mouse_move(x,y)
		time.sleep(0.05)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)		
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)	
def mouse_move(x,y):
	windll.user32.SetCursorPos(x, y)



class Hotkey(threading.Thread):  #创建一个Thread.threading的扩展类  
   
	def run(self):  
		global EXIT  #定义全局变量，这个可以在不同线程见共用。  
		user32 = ctypes.windll.user32  #加载user32.dll  
		if not user32.RegisterHotKey(None, 99, win32con.MOD_ALT, win32con.VK_F3):   # 注册快捷键 alt + f3 并判断是否成功。  
			raise																   # 返回一个错误信息  
	#以下为判断快捷键冲突，释放快捷键  
		try:  
			msg = ctypes.wintypes.MSG()  
			#print msg  
			while user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:  
				if msg.message == win32con.WM_HOTKEY:  
					if msg.wParam == 99:  
						EXIT = True  
						return  
				user32.TranslateMessage(ctypes.byref(msg))  
				user32.DispatchMessageA(ctypes.byref(msg))  
		finally:  
			user32.UnregisterHotKey(None, 1)  
  

if __name__ == "__main__":
	hotkey = Hotkey()  
	hotkey.start()  
	while 1:
		mouse_click(1150,665)
		win32api.keybd_event(17,0,0,0)  
		win32api.keybd_event(86,0,0,0)  
		win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) 
		win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0) 
		mouse_click(1272,710)
		time.sleep(180)
		if EXIT:
			sys.exit()
	
	
	
	
	
	
	
	
	
	
	
	
