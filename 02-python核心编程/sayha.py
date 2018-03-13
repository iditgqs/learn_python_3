
def application(env, start_response):
    start_response("200 OK", [("Content-Type","text/html;charset=utf-8")])
    return "haha"
