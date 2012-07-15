#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="mapl"
__date__ ="$03.03.2010 08:50:02$"

import canlib_xl
import ctypes
import msvcrt
import time

if __name__ == "__main__":
    can=canlib_xl.candriver()
    can.open_driver()
    mask=can.get_channel_mask()
    ok, phandle, pmask=can.open_port()
    print ok
    #ok=can.can_set_channel_bitrate(phandle, mask, 500000)
    #print ok, "ChannelBitrate"
    ok=can.get_appl_config()
    print ok, "appl config"
    ok=can.activate_channel(phandle)
    print ok, phandle
    event_msg=canlib_xl.XLevent(0)
    event_msg.tag=canlib_xl.XL_TRANSMIT_MSG
    event_msg.tagData.msg.id=0x04
    event_msg.tagData.msg.flags=0
    event_msg.tagData.msg.data[0]=0
    event_msg.tagData.msg.data[1]=1
    event_msg.tagData.msg.data[2]=2
    event_msg.tagData.msg.data[3]=3
    event_msg.tagData.msg.data[4]=4
    event_msg.tagData.msg.data[5]=5
    event_msg.tagData.msg.data[6]=6
    event_msg.tagData.msg.data[7]=7
    event_msg.tagData.msg.dlc=8

    #print event_list
    event_count=ctypes.c_uint(1)
    print event_count
    ok = 1
    loop=1
    while loop:
        if msvcrt.kbhit():
            loop=0
        ok=1
        try_n=0
        while (ok and try_n<3):
            time.sleep(0.1)
            #cycle time 100 ms
            event_count=ctypes.c_uint(1)
            ok=can.can_transmit(phandle, mask, event_count, event_msg)
            #ok=1 if sending was successful
            if try_n > 0:
                print "retry",
            print "code", ok, "msg", event_msg
            try_n+=1


        #print ok, event_count, event_list

    can.deactivate_channel(phandle, mask)
    can.close_port(phandle)
    can.close_driver()
