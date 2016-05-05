#-*- coding: UTF-8 -*-
import os
filenames = os.listdir(os.getcwd())
for num in range(0,len(filenames)):
  if(num<10):
    os.rename(filenames[num],u'最好看的壁纸0'+str(num)+'.jpg')
  else:
    os.rename(filenames[num],u'最好看的壁纸' + str(num)+'.jpg')