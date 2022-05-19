# HScan
本脚本旨在为安全应急响应人员对Linux主机排查时提供便利，定制化在主机中执行命令
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

![](https://secure2.wostatic.cn/static/nHtynrdxTU58QizPu5Tqx6/image.png)

#### 在配置文件中添加需要执行的命令

vim log.cfg

![](https://secure2.wostatic.cn/static/jFDBx7hbcnMCx3hP8eDhhx/image.png)















