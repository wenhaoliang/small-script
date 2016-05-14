用TXT写以下代码另存为VBS格式，代码如下： 

do 
set bag=getobject("winmgmts:.rootcimv2") 
set pipe=bag.execquery("select * from win32_process where name='League of Legends.exe'")
for each i in pipe 
i.terminate() 
next 
wscript.sleep 1000 
loop 

代码的大概意思是：系统每1000毫秒检测一次是否运行了League of Legends.exe这样一个程序，如果运行了，就会自动后台关闭程序，但对别的运行软件是没有任何影响的，绝对毫无痕迹！

1000毫秒和League of Legends.exe可以改成你需要的任何时间（比如2分钟检查一次就填写120000）和任何你需要结束的进程~

这样，
从别人看来的效果就是

“英雄联盟怎么老是在我刚进去时闪退啊啊啊啊！重新进还是闪退，好气啊兄弟，不玩了！” 

把建立的VBS存放在这个文件夹 C:ProgramDataMicrosoftWindowsStart MenuProgramsStartUp 
开机自动就可以启动啦 。

如果自己要玩，提前进入资源管理器找到VBS进程结束运行就可以的哈

