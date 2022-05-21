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

![image](https://user-images.githubusercontent.com/22775890/169656681-b082cd68-3508-4521-bcb5-8d8e0feab864.png)


可以在定时任务中设置每天八点执行此脚本。

vim /etc/crontab

00 8    * * *   root    python3 /you_path/HScan/log_analysis.py












