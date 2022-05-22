#! /usr/bin/python3
import sys,linecache,time
import subprocess
import shlex

def cmd_exec(cmd):
    last = ''  #命令执行后返回的字符串
    if '|' not in cmd:
        return subprocess.Popen(cmd if '*' in cmd else shlex.split(cmd),stdout=subprocess.PIPE,shell=True if '*' in cmd else False).stdout.read().decode()
    cmd_len = len(cmd.split('|'))
    for j,i in enumerate(cmd.split('|')):
        if j == 0:
            last = subprocess.Popen(i if '*' in i else shlex.split(i),stdout=subprocess.PIPE,shell=True if '*' in i else False)
        elif j>0 and j < cmd_len-1:
            last = subprocess.Popen(i if '*' in i else shlex.split(i),stdin=last.stdout,stdout=subprocess.PIPE,shell=True if '*' in i else False)
        elif j == cmd_len-1:
            last = subprocess.Popen(i if '*' in i else shlex.split(i),stdin=last.stdout,stdout=subprocess.PIPE,shell=True if '*' in i else False).stdout.read().decode()
    return last

if len(sys.argv) > 1:
    lao = sys.argv[1]
else:
    lao = 'out_log_analysis.txt'

line = linecache.getlines('log.cfg')
with open(lao,'w') as f:
    f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n')
    for i in line:
        if i.startswith('#') or i=='\n' or i=='\r\n':continue
        print('=====',i)
        one_line = i.split('//')
        cli,des = one_line[0],one_line[1]
        if cli.startswith('>'):
            cmd_exec(cli[1:])
            print(cli[1:])
            continue
        f.write(f'{des.strip()}   命令:{cli}\n')
        print(cli)
        f.write(cmd_exec(cli))
print(f'执行完成输入cat {lao}进行查看')
