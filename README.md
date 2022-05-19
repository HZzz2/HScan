# HScan
本脚本旨在为安全应急响应人员对Linux主机排查，日志分析等提供便利，定制化在主机中执行命令
#### 获取脚本

git clone https://github.com/HZzz2/HScan.git

cd HScan

#### 使用脚本

```Bash
python log_analysis.py     #默认输出至当前目录out_log_analysis.txt
或者
python log_analysis.py out.txt  #进行指定输出至out.txt

```

#### 查看输出

cat out_log_analysis.txt
![image](https://user-images.githubusercontent.com/22775890/169294044-9dbe9dcb-db95-46e4-a104-f09b255aa809.png)

![](https://secure2.wostatic.cn/static/nHtynrdxTU58QizPu5Tqx6/image.png)

#### 在配置文件中添加需要执行的命令

vim log.cfg

![image](https://user-images.githubusercontent.com/22775890/169294093-dd39e336-c537-4e3d-a96d-61d5b56656d3.png)

![](https://secure2.wostatic.cn/static/jFDBx7hbcnMCx3hP8eDhhx/image.png)

可以在定时任务中设置每天执行此脚本。













