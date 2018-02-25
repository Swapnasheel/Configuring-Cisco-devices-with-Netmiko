#! /usr/bin/python

'''
Make sure you have running SSH connections/ setup within the network.
It is important that the switches in the network can communicate with the PC that has python installed in it.
And the PC will be runnig the script in it.
'''

import telnetlib
import getpass


# Get the username and password
username = raw_input("Enter the username: ")
password = getpass.getpass()

#Open the file that has the information of the switches (IP address)
f = open("switchIP")

#Telnet to each switch and get the running configurations
for line in f:

    print "Saving configurations of " + line + " switch."
    HOST = line.strip()
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(username + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("terminal length 0 \n")
    tn.write("show run \n")
    tn.write("exit \n")

    readoutput = tn.read_all()
    saveoutput = open("Switch" + HOST, "w")
    saveoutput.write(readoutput)
    saveoutput.write("\n")
    saveoutput.close()

f.close()

    
    



