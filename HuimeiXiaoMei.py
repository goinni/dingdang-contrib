# -*- coding: utf-8-*-
# 惠每小美
import logging
import sys
import time
import subprocess

reload(sys)
sys.setdefaultencoding('utf8')

WORDS = ["XIAOMEI","JIAOMEI","LIUJIAO","AJIAO"]
SLUG = "hmxiaomei"

def handle(text, mic, profile, wxbot=None):
    logger = logging.getLogger(__name__)
    try:
        mic.say('亲爱的，您哪里不舒服。请在滴一声后说出您的症状', cache=True)
        input = mic.activeListen(MUSIC=True)
        if input is not None:
            mic.say('好哒，这就为您诊断', cache=True)
            time.sleep(3)
            mic.say('亲爱的，您好像是得了急性上呼吸道感染，可以吃点消炎类药，以上结果由惠每医疗提供，仅供参考', cache=True)
            # subprocess.Popen("sudo reboot -f", shell=True)
            return
        mic.say('老娘没听清，再说一次呗', cache=True)
    except Exception, e:
        logger.error(e)
        mic.say('啊，出错了，一会儿再试一下', cache=True)

def isValid(text):
    return any(word in text for word in [u"小梅", u"娇妹", u"刘娇", u"阿娇"])
