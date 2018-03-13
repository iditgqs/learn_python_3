import time


def application(evn, start_response):
    start_response("200 OK",[])
    
    return time.ctime()
