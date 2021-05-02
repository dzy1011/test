#百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json

def tran(q):
    appid = '20190305000273755'  # 填写你的appid
    secretKey = 'rJ8h7qeIVJ3iKc1gCeff'  # 填写你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'auto'   #原文语种
    toLang = 'zh'   #译文语种
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        print ('result:',result['trans_result'][0]['dst'])
        return result['trans_result'][0]['dst']
    except Exception as e:
        print (e)
        return e


res = tran('eee1MichaelPentelladdd1 PhD , is Director of the eee2BureauSciencesddd2 at the eee3HintonInstituteddd3 , Commonwealth of eee4Massachusettsddd4. He previously served as the Associate Director of the eee5Iowalaboratoryddd5 and as Clinical Associate Professor at the eee6CollegeHealthddd6 , eee7UniversityIowaddd7 .Dr. has more than 30 years of experience in clinical and public health laboratories and is board certified in medical microbiology and infection control .')