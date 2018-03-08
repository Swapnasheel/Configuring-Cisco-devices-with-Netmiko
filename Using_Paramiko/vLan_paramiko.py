#! /usr/bin/python

import paramiko
import time

f = open("inventory")
username = raw_input("Get username: ")
password = raw_input("Get password: ")

for line in f:
    # Connect to the client using the paramiko SSHClient function
    ssh_client = paramiko.SSHClient()
    # For testing purposes, AutoAddPolicy is added to allow auto-add unknown host keys
    # This should be avoided in the production environment, and set to RejectPolicy
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=line, username=username, password=password)

    print "Successful connection with " + line
    
    # Start an interactive session with the router
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
