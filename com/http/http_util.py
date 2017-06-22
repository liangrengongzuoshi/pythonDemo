# encoding:utf-8

import json
from urllib import unquote
import traceback


def paramsToDict(strParam):
    params = {}
    if strParam:
        for x in strParam.split("&"):
            kv = x.split("=")
            if len(kv) == 2:
                kv[1] = kv[1].replace("+", " ")
                valueStr = unquote(kv[1].strip())
                if valueStr.startswith("[") or valueStr.startswith("{"):
                    try:
                        valueStr = json.loads(valueStr)
                    except Exception:
                        traceback.print_exc()
                params[kv[0].strip()] = valueStr
    
    return params


def getRequestParams(path, headers, rfile):
    params = {}
    if path:
        actionPath = path
        if '?' in path:
            index = path.index('?')
            actionPath = path[0:index]
            params = paramsToDict(path[index + 1:])
        if rfile:
            bodySize = 0
            try:
                if headers:
                    contentLength = headers.getheader('content-length')
                    if contentLength:
                        bodySize = int(contentLength)
                        params.update(paramsToDict(rfile.read(bodySize)))
            except Exception:
                traceback.print_exc()
                
    return actionPath, params

