#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

import canlib_xl
import threading
import time
import msvcrt

class msg_send_thread(threading.Thread):
    def __init__(self, id, data, interval, can):
        threading.Thread.__init__(self)
        self.can=can
        self.id=id
        self.data=data
        self.interval=interval
        self.send_msg=1

    def stop_msg(self):
        self.send_msg=0

    def send_msg_periodic(self):
        self.send_msg=1

    def run(self):
        while (self.send_msg):
            self.can.send_msg(self.data, self.id)
            time.sleep(self.interval)

__author__="uid14026"
__date__ ="$19.03.2010 13:51:35$"

max_threads=0x10


def main():
    can=canlib_xl.can_api()
    ok=can.channel_init()
    msg_thread=list([])
    for n in range(0, max_threads):
        msg_thread.append(msg_send_thread(0x100+n, [0x1, 0x2, 0x3], 0.01, can))
        msg_thread[n].start()
    ok=1
    while ok:
        if msvcrt.kbhit():
            ok=0
            for n in range(0, max_threads):
                msg_thread[n].stop_msg()
    can.channel_close()

if __name__ == "__main__":
    main()
