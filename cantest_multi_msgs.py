#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="mapl"
__date__ ="$01.03.2010 14:04:51$"

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
    event_list=canlib_xl.array_XLevent()
    print event_list
    event_count=ctypes.c_uint(1)
    print event_count
    ok = 1
    loop=1
    while loop:
        if msvcrt.kbhit():
            loop=0
        ok=1
        while (ok):
            event_count=ctypes.c_uint(5)
            #print phandle, event_count
            ok=can.receive_multiple_msgs(phandle, event_count, event_list)
            time.sleep(1)
            #print ok, event_list
        for n in event_list:
            rec_string=can.get_event_string(n)
            print rec_string


    can.deactivate_channel(phandle, mask)
    can.close_port(phandle)
    can.close_driver()
