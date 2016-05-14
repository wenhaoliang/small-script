#-*- coding: UTF-8 -*-
import os
filenames = os.listdir(os.getcwd())
for num in range(0,len(filenames)):
  if(num<10):
    os.rename(filenames[num],u'第'+str(num)+'章.MP4')
  else:
    os.rename(filenames[num],u'第' + str(num)+'章.MP4')