# coding: utf-8
import time
import random
import requests
from wxpy import *
from . import settings

API_URL = 'http://www.tuling123.com/openapi/api'
TULING_TOKEN = settings.TOKEN
DDD = '。。。'
EMOJI = ['[可怜]', '[微笑]', '[愉快]', '[委屈]', '🤔', '😳']


def choose_suffix(rand_num):
    if rand_num > 100:
        return ''
    elif rand_num >= 70:
        return DDD
    else:
        return random.choice(EMOJI) * random.randint(1, 3)


def echo_reply(msg):
    rst = u'自动回复喵喵喵'
    rst += msg.text
    return rst


def tuling_reply(msg):
    data = {
        'key': TULING_TOKEN,
        'info': msg.text.encode('utf-8'),
        'userid': msg.sender.puid.encode('utf-8')
    }
    s = requests.post(API_URL, data=data).json()
    if s['code'] == 100000:
        rst = s['text']
        suf = choose_suffix(random.randint(0, 110))
        uni_suf = unicode(suf, "utf8")
        l = len(rst + uni_suf)
        time.sleep(l / 3)
        return rst + uni_suf


def main():
    bot = Bot(console_qr=True, cache_path=True)
    bot.enable_puid('wxpy_puid.pkl')
    tuling = Tuling(api_key=TULING_TOKEN)
    # Florrie
    # f = bot.friends().search(puid='c1a97fd0')[0]
    # ZJDTT
    friend = bot.friends().search(puid='a3261a9b')[0]

    @bot.register()
    def reply_my_friend(msg):
        return tuling_reply(msg)
        # return echo_reply(msg)

    @bot.register(bot.self, except_self=False)
    def reply_self(msg):
        return tuling_reply(msg)
        # return echo_reply(msg)

    @bot.register(Group, TEXT)
    def group(msg):
        print "no reply", msg.text

    embed()


if __name__ == '__main__':
    main()
