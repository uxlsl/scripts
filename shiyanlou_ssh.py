#!-*- coding:utf-8 -*-
import re
from pexpect import pxssh


ip, port, username, password = None, None, None, None


while True:
    line = input()
    m = re.search(r'(?P<ip>(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)(?:\.(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}):(?P<port>\d{1,5})', line)
    if m:
        tmp = m.groupdict()
        ip, port = tmp['ip'], tmp['port']
    m = re.search(r'用户名：(?P<username>\w+)\s*密码：(?P<password>\d+)', line)
    if m:
        tmp = m.groupdict()
        username, password = m['username'], m['password']
    if ip and port and username and password:
        break


ssh = pxssh.pxssh()
ssh.login(server=ip,port=port, username=username, password=password)
ssh.sendline('zsh')
ssh.interact()
