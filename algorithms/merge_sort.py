from time import sleep
from threading import Thread
from queue import Queue
def funtion_1(x,y):
    print('thread one starts')
    sleep(2)
    print('thread one ends')
    return x+y

def function_2(x,y):
    print('thread two starts')
    print('thread two ends')
    return x*y


t1 =Thread(target=funtion_1,daemon=True,args=(2,3))
t2 =Thread(target=function_2,args=(2,3))


t1.start()
t2.start()


