#! /usr/bin/python

import paramiko
import time

f = open("inventory")
username = raw_input("Get username: ")
password = raw_input("Get password: ")

for line in f:
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=line, username=username, password=password)

    print "Successful connection with " + line

    remote_connection = ssh_client.invoke_shell()

    command = open("commands")
    for c in command:
        c = line.strip()
        remote_connection.send(c + '\n')
        time.sleep(1)

    remote_connection.send("end \n")
    output = remote_connection.recv(65535)
    print output

    ssh_client.close()
