# -*- coding: utf-8-*-
# 惠每小美
import logging
import sys
import time
import subprocess
import json,urllib2

reload(sys)
sys.setdefaultencoding('utf8')

WORDS = ["XIAOMEI","JIAOMEI","LIUJIAO","AJIAO"]
SLUG = "hmxiaomei"


def getDiseaseEntity(words):
   
    entity = ""
    try:
        

        textmod={"gender":"1","age":"18","ageType":"岁","symptom":words,"inquiryType":"0","hasRegimen":True,"v":1529818004373}
        textmod = json.dumps(textmod)
        print(textmod)
        headers = {
            'api-extend-params': '%7B%22hospitalGuid%22%3A4967%2C%22userGuid%22%3A2292613%2C%22doctorGuid%22%3A6394%2C%22serialNumber%22%3A2702113%2C%22authKey%22%3A%22C3B844493A477BCF3D7B73A5E902B269%22%2C%22i18n%22%3A%22cn%22%7D',
            'Huimei_id': 'C3B844493A477BCF3D7B73A5E902B269',
            "Content-Type": "application/json"
        }
        url='http://cdss.huimeionline.com/apollo/v_2_3/diagnose_through_interrogation'

        req = urllib2.Request(url=url,data=textmod,headers=headers)
        res = urllib2.urlopen(req)
        res = res.read()

        result = json.loads(res)
        #诊断名
        #diseaseName = result[u'body'][u'diseaseGroups'][0][u'diseases'][0][u'diseaseName']
        #诊断说明
        #definition = result[u'body'][u'diseaseGroups'][0][u'diseases'][0][u'definition']

        entity = result[u'body'][u'diseaseGroups'][0][u'diseases'][0];

    except :
        pass
    return entity

def handle(text, mic, profile, wxbot=None):
    logger = logging.getLogger(__name__)
    try:
        mic.say('亲爱的，您哪里不舒服。请在滴一声后说出您的症状', cache=True)
        input = mic.activeListen(MUSIC=True)
        if input is not None:
            mic.say('好哒，这就为您诊断', cache=True)
            #time.sleep(1)
            # 获取诊断信息
            entity = getDiseaseEntity(input)
            if entity[u'definition'] is not None:
                mic.say('亲爱的，您好像是得了'+entity[u'diseaseName']+'，'+ entity[u'definition']+'，以上结果由惠每医疗提供，仅供参考', cache=True)
            else:
                mic.say('亲爱的，您好像是得了'+entity[u'diseaseName']+'，生病了要多喝水哦，请注意休息哦，以上结果由惠每医疗提供，仅供参考', cache=True)
            return
        mic.say('老娘没听清，再说一次呗', cache=True)
    except Exception, e:
        logger.error(e)
        mic.say('啊，出错了，一会儿再试一下', cache=True)

def isValid(text):
    return any(word in text for word in [u"小梅", u"娇妹", u"刘娇", u"阿娇"])

