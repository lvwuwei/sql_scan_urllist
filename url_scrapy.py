#for python3
import requests,re
from urllib import parse
from time import sleep,time
 '''inurl:php?id='''
'''URL采集器Author:h4ckg3h2y1'''
 
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'}
 
def google(keyword,pagenumber):
    time_stamp = str(time())
    try:
        for page in range(0,(pagenumber-1)*10+1,10):
            google_url = 'https://www.google.com/search?q={}&start={}'.format(keyword,page)
            html = requests.get(google_url)
            patt = re.compile('"><a href="/url\?q=(.*?)&amp;sa=')
            url_list = re.findall(patt,html.text)
            ext(url_list,time_stamp)
            sleep(5)
    except requests.exceptions.ProxyError:
        print('请求被拦截，可能需要进行人机验证')
 
def baidu(keyword,pagenumber):
    time_stamp = str(time())
    try:
        for page in range(0,(pagenumber-1)*10+1,10):
            baidu_url = 'https://www.baidu.com/s?wd={}&pn={}'.format(keyword,page)
            html = requests.get(baidu_url,headers=header)
            patt = re.compile('"><a target="_blank" href="(.*?)" class="')
            url_list = re.findall(patt,html.text)
            baidu_ext(url_list,time_stamp)
            sleep(5)
    except requests.exceptions.ProxyError:
        print('请求被拦截，可能需要进行人机验证')
 
def bing(keyword,pagenumber):
    time_stamp = str(time())
    try:
        for page in range(1,pagenumber*10+1,10):
            bing_url = 'https://cn.bing.com/search?q={}&go=%e6%90%9c%e7%b4%a2&qs=ds&mkt=zh-CN&first={}&FORM=PERE'.format(keyword,page)
            html = requests.get(bing_url,headers=header)
            patt = re.compile('<a target="_blank" href="(.*?)" h=')
            url_list = re.findall(patt,html.text)
            ext(url_list,time_stamp)
            sleep(5)
    except requests.exceptions.ProxyError:
        print('请求被拦截，可能需要进行人机验证')
 
def ext(url_list,time_stamp):
    try:
        for url in url_list:
            url = parse.unquote(url)
            with open('{}.txt'.format(time_stamp),'a') as f:
                f.write(url+'\n')
                print('[+]'+url)
    except:
        print('请求超时')
 
#百度采集的URL需要经过二次访问才能获得原ip
def baidu_ext(url_list,time_stamp):
    try:
        for url in url_list:
            again = requests.get(url,headers=header,timeout=5.0)
            with open('{}.txt'.format(time_stamp),'a') as f:
                f.write(again.url+'\n')
                print('[+]'+again.url)
                sleep(1)
    except:
        print('请求超时')
 
def main(Search_engine,Search_key,Search_page):
    if Search_engine == 1:
        google(Search_key,Search_page)
    elif Search_engine == 2:
        bing(Search_key,Search_page)
    elif Search_engine == 3:
        baidu(Search_key,Search_page)
    else:
        print('请输入正确的编号')
 
if __name__ == '__main__':
    print('''Instructions：URL采集，请求超时可能是触发了搜索引擎的人机验证。''')
    Search_engine = input('请输入调用的搜索引擎编号[1 : Google][2 : Bing][3 : BaiDu]: ')
    Search_key = input('请输入关键词: ')
    Search_page = input('请输采集页数(10条/1页): ')
    main(int(Search_engine),Search_key,int(Search_page))