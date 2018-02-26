#! /usr/bin/python

from netmiko import ConnectHandler


## Open file and send config to the device function

def config(config_file, device_list):

    with open(config_file) as f:
        line = f.read().splitlines()
    print line

    for device in device_list:
        net_connect = ConnectHandler(**device)
        output = net_connect.send_config_set(line)
        print output

def Main():

    config(config_file = 'access_file', device_list = ['SW5','SW4','SW3'])
    config(config_file = 'core_file', device_list = ['SW2','SW1'])


## My Devices

SW1 = {
        'device_type': 'cisco_ios',
        'ip' : '192.168.122.'
        'username': 'swapnasheel',
        'password': 'cisco'
}

SW2 = {
        'device_type': 'cisco_ios',
        'ip' : '192.168.122.'
        'username': 'swapnasheel',
        'password': 'cisco'
}

SW3 = {
        'device_type': 'cisco_ios',
        'ip' : '192.168.122.'
        'username': 'swapnasheel',
        'password': 'cisco'
}

SW4 = {
        'device_type': 'cisco_ios',
        'ip' : '192.168.122.'
        'username': 'swapnasheel',
        'password': 'cisco'
}

SW5 = {
        'device_type': 'cisco_ios',
        'ip' : '192.168.122.'
        'username': 'swapnasheel',
        'password': 'cisco'
}

Main()

