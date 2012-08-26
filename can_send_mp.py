#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

import canlib_xl
import multiprocessing
import time
import msvcrt


def send(data, id, cycle):
    can=canlib_xl.can_api()
    ok=can.channel_init()
    
    n=0
    while (n < 100):
        print id
        can.send_msg(data, id)
        time.sleep(cycle)
        n+=1
    can.channel_close()
    return


max_process=5


def main():

#    p=multiprocessing.Process(target=send, args=([0x1, 0x2, 0x3], (0x100) ) )
#    p.start()

    jobs=list()
    for n in range(0, max_process):
        p=multiprocessing.Process(target=send, args=([0x1, 0x2, 0x3], 0x100+n, 0.01*n))
        jobs.append(p)
        p.start()
    print jobs
    #print args


    

if __name__ == "__main__":
    main()
