#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="uid14026"
__date__ ="$03.03.2010 12:06:07$"



import canlib_xl
import ctypes
import msvcrt
import time

if __name__ == "__main__":
    can=canlib_xl.can_api()
    ok=can.channel_init()
    print ok
    ok=0
    while not(ok):
        time.sleep(0.01)
        ok=can.send_msg([1, 2, 3, 4], 4)
        msg=can.get_msg()
        print msg
        if msvcrt.kbhit():
            ok=1
        else:
            ok=0
    print ok
    can.channel_close()


