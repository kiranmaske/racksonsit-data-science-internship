import threading

def cube(no):
    print("Cube is ={}".format(no*no*no))
def squre(no):
    print("squre is ={}".format(no*no))
if __name__ == "__main__":
    t1 = threading.Thread(target=cube,args=(5,))
    t2 = threading.Thread(target=squre,args=(5,))
    # starting thread
    t1.start()
    t2.start()
# waiting
    t1.join()
    t2.join()
    
    
   
# import os
# def assignTask1():
#     print("task1 assign to thread={}".format(threading.current_thread().name))
#     print("Id of an process running task1 ={}".format(os.getpid()))
# def assignTask2():
#     print("task2 assign to thread={}".format(threading.current_thread().name))
#     print("Id of an process running task2 ={}".format(os.getpid()))
    
# if __name__=="__main__":
#     print("id of process runing main program={}".format(os.getpid()))
#     t1 = threading.Thread(target=assignTask1,name='t1')
#     t2 = threading.Thread(target=assignTask2,name='t2')
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()