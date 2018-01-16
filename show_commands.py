from __future__ import print_function
from netmiko import ConnectHandler
import sys
import time
import select
import paramiko
import re
fd = open(r'/home/user/show_output.txt','w') # Where you want the file to save to.
old_stdout = sys.stdout
sys.stdout = fd
platform = 'cisco_ios'
username = 'user' # edit to reflect
password = 'password' # edit to reflect

ip_add_file = open(r'/home/user/ipadd.txt','r') # a simple list of IP addresses you want to connect to each one on a new line

for host in ip_add_file:
    host = host.strip()
    device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
    output = device.send_command('terminal length 0')
    output = device.send_command('enable') #Editable to be what ever is needed
    print('##############################################################')
#    print('...................CISCO COMMAND SHOW VER OUTPUT......................\n')
    output = device.send_command('sh run | in hostname')
    print(output)
    output = device.send_command('sh ver | in Base ethernet MAC Address')
    print(output)
    output = device.send_command('sh ver | in System serial number')
    print(output)
#    print('##############################################################')
fd.close()

# opens the output file and deletes the line with $(hostname) 
with open("/home/user/show_output.txt","r") as f:
  lines = f.readlines()
with open("/home/user/show_output.txt","w") as f:
  for line in lines:
    if line!="***   You are connected to $(hostname)  ***"+"\n":
      f.write(line)


# opens the output file and deletes the string System serial number and MAC address
f = open("/home/user/show_output.txt").read()
f_new = re.sub('System serial number            : ','',f)
open("/home/user/show_output.txt",'w').write(f_new)

f = open("/home/user/show_output.txt").read()
f_new = re.sub('Base ethernet MAC Address       : ','',f)
open("/home/user/show_output.txt",'w').write(f_new)
