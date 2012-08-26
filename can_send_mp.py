#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

import canlib_xl
import multiprocessing
import time
import msvcrt


def send(data):
    can=canlib_xl.can_api()
    ok=can.channel_init()
    
    n=0
    while (n < 100):
        print data
        can.send_msg(data[0], data[1])
        time.sleep(0.01)
        n+=1
    can.channel_close()
    return


max_process=10


def main():

#    p=multiprocessing.Process(target=send, args=([0x1, 0x2, 0x3], (0x100) ) )
#    p.start()
    args=list()
    p=multiprocessing.Pool(processes=max_process)
    for n in range(0, max_process):
        args.append(([0x1, 0x2, 0x3], (0x100+n)))
    #print args
    p.map(send, args)

    

if __name__ == "__main__":
    main()
