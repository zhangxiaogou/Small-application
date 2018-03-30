# -*- coding:utf-8 -*-
import urllib2, urllib
import json

def geocoding(filename):
    '''实现通过百度地图API查询地址的位置坐标，并返回到新的文件中'''
    result = open("address_geocoding.txt", "w") #结果文件
    wronglog = open("wronglog.txt", "w") #错误日志
    # 将需要查找的地址名称储存在一个文件中，例如TXT中，每行存一个需要查询的地址。
    f = open(filename)
    names = f.readlines()
    for name in names:
        name = name.decode('gbk').encode('utf-8')  # 对name进行转码
        name = name[:-1]  # 去除name最后的/n 如果确认没有需要注释掉此行
        address = urllib.quote(name)  # 屏蔽掉特殊的字符name
        try:
            ak = '**************You AK***************'  #你的百度ak值
            req = urllib2.urlopen(
                'http://api.map.baidu.com/geocoder/v2/?address=%s&output=json&ak=%s' % (address, ak)).read() #这个url能够返回含有位置坐标的json字符串在页面上
            res = json.loads(req)
            coordinate = res['result']['location']
            lat = coordinate['lat']
            lng = coordinate['lng']
            msg = "%s 经度%s 纬度%s  " % (name, str(lng), str(lat))
            result.write(msg)
        except Exception:
            wronglog.write(name + "  ")
    f.close()
    result.close()
    wronglog.close()

#调用测试
if __name__ == '__main__':
    geocoding("text_address.txt")
