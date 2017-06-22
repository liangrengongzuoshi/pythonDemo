# encoding=utf-8

'''
@author: liangzai
'''
'''支持多线程的webserver'''

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
import json
import threading

from com.http.http_util import getRequestParams


class myHandler(BaseHTTPRequestHandler):

    def do_action(self, method):
        retData = {"code":1, "msg":"ok", "data":None}
        actionPath, params = getRequestParams(self.path, self.headers, self.rfile)

        print(actionPath, params)
        retData["method"] = method
        retData["data"] = params
        retData["action"] = actionPath

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Uri', self.path)
        self.end_headers()
        self.wfile.write(json.dumps(retData))
        # return json.dumps(retData)
    
    def do_GET(self):
        self.do_action("get")
    
    def do_POST(self):
        self.do_action("post")
    
class ThreadingHttpServer(ThreadingMixIn, HTTPServer):
    pass


'''监听端口'''
MY_PORT = 8080

if __name__ == '__main__':
    
    server = ThreadingHttpServer(("", MY_PORT), myHandler)
    print("程序启动，监听端口：%s." %MY_PORT)
    
    thread = threading.Thread(target=server.serve_forever)
    thread.start()
    
    print("程序启动完成...")
