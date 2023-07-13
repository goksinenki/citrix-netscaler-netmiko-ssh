# First import processing connection
import netmiko
import cmd
import time
import sys
import datetime
import json
import textfsm
from pprint import pprint
from ntc_templates.parse import parse_output

from netmiko import ConnectHandler as ch



my_file = open("citrixips.txt", "rb")


for line in my_file:
        l = [i.strip() for i in line.decode().split(' ')]
        IP = l[0]
        #print (IP)
        file = open('citrixsonuc.txt', 'a')
        host = {
            'device_type': 'netscaler',
            'host': IP,
            'username': 'yourusername',
            'password': 'yourpassword',
            'port': 22,
            'secret': '', # Enable Password, no way without writing this line
        }

        # Connect the device, CONN can be understood as a terminal that has been connected to the device, at which time the command can be executed directly
        try:
            conn = ch(**host)
        # Error through the send_command method, check the interface information, the return value is a string
            #output = conn.send_command('show ssl certLink | grep "13102023"')
            output = conn.send_command('show ns runningConfig | grep "link ssl"')
            file.write(IP+"\n"+output+"\n")
        #output = conn.send_command('show version')
        #file.write(IP+"\n"+output+"\n")
            file.close()
        except:
            file.close()
