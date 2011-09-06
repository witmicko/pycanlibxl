#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="mapl"
__date__ ="$03.09.2011 12:06:07$"



import canlib_xl
import ctypes


if __name__ == "__main__":
    can=canlib_xl.can_api()
    ok=can.channel_init()
    print ok
    ok=0
    p=can.get_driver_info()
    print "dll ", p.dllVersion
    print "channels ", p.channelCount
    if p.channelCount > 0:
        print "name ", p.channel[0].name
        print "hwType", p.channel[0].hwType
        print "hwIndex", p.channel[0].hwIndex
        print "hwChannel", p.channel[0].hwChannel
        print "driver version", p.channel[0].driverVersion
        print "interface version", p.channel[0].interfaceVersion