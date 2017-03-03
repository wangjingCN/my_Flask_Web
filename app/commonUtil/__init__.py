#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import urllib2
from . import aesHelper
re1 = '\d+\.\d{2}$'  # 小数点后2位的数字
re2 = r'(?<!A)\d+'
# ree1 = '<img src="(.*)" alt=.*?/>(.*)<'
ree1 = '<img[^>]+src="([^"]+)[^>]+>([^<]+)'
ree = r'''
<tr onMouseOver="this.style.cursor='pointer';this.style.backgroundColor='#3A3A3A'" onMouseOut="this.style.background='none'" onClick="javascript:window.open('match.html?id=文字');">
<td>文字</td>
<td><img src="图片链接" alt="" height="32" width="32"/>文字</td>
<td>文字</td>
<td>文字</td>
</tr>
'''''


def add1(math):
    return str(int(math.group()) + 1)


def main():
    file = open('imoc.txt')
    return_result = []
    for line in file:
        # if line.startswith("imoc"):
        #     print line
        regStr = r'imoc'  # 需要匹配的正则表达式
        # re.I 代表忽略大小写
        result = re.compile(regStr, re.IGNORECASE).findall(line)

        if len(result):
            print result
            return_result.append(result)
            print line
            # g = re.compile(regStr,re.I).match(line).group()
            # if g:
            #     print len(g)
            #     print line
    print return_result


def x():
    regex = r'^[\w]{4,6}@163.com'
    na = re.match(regex, 'imoc@163.com')
    print na.group()


if __name__ == '__main__':
    re5 = r'^(\d+|((?![IO])[A-Za-z])+)$'
    parm = 'adcI'
    print re.compile(re5).match(parm).group()
    a1 = re.findall(ree1, ree)
    if a1:
        print a1
        print a1.__len__()
        print a1[0][0]
        print a1[0][1]

    str1 = '<xml>xml</xml>'
    ma = re.match(r'<(?P<Word>\w+)>\w+</(?P=Word)', str1)
    if ma:
        print ma.group()

    strni = 'a23987元'
    a = re.findall(r'(?<!A)\d+', strni)
    if a:
        print a
    stra = 'imoc videonum=1000,s=80'
    # regex=r'\d+'
    regex = r'[0-9]+'
    print  re.sub(regex, add1, stra)

    info = re.findall(regex, stra)
    print info
    print sum([int(x) for x in info])

    info = re.split(r' |=|,', stra)
    print info

    rex = r'^0\d{2,3}-\d{7,8}'
    str1 = '010-12345678'
    str2 = '0376-7654321'
    str3 = '0376-76543'
    ma = re.match(rex, str1)
    print ma.group()
    ma = re.match(rex, str2)
    print ma.group()
    ma = re.match(rex, str3)
    if ma:
        print ma.group()
    else:
        print 'not mathed str'
        # x()
        # print str.find('1000')
    req = urllib2.urlopen('http://tw.digiwin.biz/images/case/160-11.jpg')
    f = open('1.jpg', 'w')
    f.write(req.read())
    re.U
