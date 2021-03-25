import requests
import os
import log

# 获取cookie
COOKIE = ''
if os.environ.get('SGSCOOKIE', '') != '':
        COOKIE = os.environ['SGSCOOKIE']
        cookie_list = COOKIE.split('#')
url = 'http://wx.sanguosha.com/api/clock/do'
ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1316.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat'

# 开始签到
for i in range(len(cookie_list)):
    log.info(f'准备为 NO.{i + 1} 账号签到...')
    sendCookie = cookie_list[i]
    headers = {
        'User-Agent': ua,
        'cookie' : sendCookie
    } 
    r = requests.post(url=url, headers=headers)
    print.info(r.json())

if i >= (len(cookie_list)):
    log.info('签到完成')

log.info('任务结束')
# echo '${{ secrets.SGSCOOKIE }} 任务结束'




