from netmiko import ConnectHandler
import sys
import time
import paramiko

platform = 'cisco_wlc'
username = 'user' # edit to reflect
password = 'password' # edit to reflect

ip_add_file = open(r'/home/user/ipadd.txt','r') # a simple list of IP addresses you want to connect to each one on a new line

for host in ip_add_file:
    host = host.strip()
    device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
    output = device.send_config_from_file('/home/user/wlc_conf.txt')