# encoding=utf-8
'''
@author: liangzai
'''

import json

'''
json.dumps    将 Python 对象编码成 JSON 字符串
json.loads    将已编码的 JSON 字符串解码为 Python 对象
'''

'''
python 原始类型向 json 类型的转化对照表：
    dict——> object
    list, tuple——> array
    str, unicode——> string
    int, long, float——> number
    True——> true
    False——> false
    None——> nul
'''

'''
json 类型转换到 python 的类型对照表：
    object——> dict
    array——> list
    string——> unicode
    number (int)——> int, long
    number (real)——> float
    true——> True
    false——> False
    null——> None
'''

data = {"name":"张三", "age":19, "sex":"男"}

_str = json.dumps(data)

print(_str)

_str = '''
{
    "total_cnt": "429",
    "currentAccountId": "36",
    "list": [{
            "res_id_real": "77087121",
            "res_id": "88051303",
            "url": "http://ehire.51job.com/Candidate/ResumeView.aspx?hidUserID=88051303&hidEvents=23&hidKey=250eba44fb0b914808e549b96b8c5ab5&v=1",
            "age": "27",
            "res_workyear": "6年",
            "res_sex": "男",
            "res_dq_name": "深圳-南山区",
            "res_dq_nameCode": "050090030",
            "edu_major": "计算机信息管理",
            "edu_level": "大专",
            "edu_levelCode": "050",
            "res_industry_name": "互联网/电子商务",
            "res_industry_nameCode": "040",
            "res_jobtitle_name": "高级软件工程师",
            "res_modifytime": "2017-03-20",
            "edu_university": "黄石理工学院",
            "res_ajax": "a42b006bed1c04da",
            "res_title": "安卓开发工程师",
            "res_context": "2014/9-2017/2&nbsp;&nbsp;|&nbsp;&nbsp;武汉斗鱼网络科技有限公司&nbsp;&nbsp;|&nbsp;&nbsp;安卓开发工程师<br />2014/3-2014/9&nbsp;&nbsp;|&nbsp;&nbsp;杭州新世纪深圳分公司&nbsp;&nbsp;|&nbsp;&nbsp;软件工程师<br />2012/3-2014/2&nbsp;&nbsp;|&nbsp;&nbsp;深圳华科远讯&nbsp;&nbsp;|&nbsp;&nbsp;软件工程师",
            "res_company": "武汉斗鱼网络科技有限公司"
        }]
}
'''

mydict = json.loads(_str)

print(mydict)
print(mydict["currentAccountId"])
print(mydict.get("list", None)[0].get("res_sex"))

