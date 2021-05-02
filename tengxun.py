import json
import time
from tqdm import tqdm
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models
inp = open('yuliao1.txt','r',encoding='utf-8').readlines()
oup = open('yuliaofanyi1.txt','w',encoding='utf-8')
try:
    cred = credential.Credential("AKIDvgAIwYPTlpfFa3KuhU3NfndQzIm3gzdI", "94kJQ3f2EaP9qQzDUbKgtxr0xlnjkeps")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "tmt.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = tmt_client.TmtClient(cred, "ap-beijing", clientProfile)

    req = models.TextTranslateRequest()

    params = {
        "SourceText": "eee1MichaelPentelladdd1 PhD , is Director of the eee2BureauSciencesddd2 at the eee3HintonInstituteddd3 , Commonwealth of eee4Massachusettsddd4 . He previously served as the Associate Director of the eee5Iowalaboratoryddd5 and as Clinical Associate Professor at the eee6CollegeHealthddd6 , eee7UniversityIowaddd7 .Dr. has more than 30 years of experience in clinical and public health laboratories and is board certified in medical microbiology and infection control.",
        "Source": "auto",
        "Target": "zh",
        "ProjectId": 0
    }
    for line in tqdm(inp):
        line =line.rstrip('\n')
        params["SourceText"]=line
        req.from_json_string(json.dumps(params))

        resp = client.TextTranslate(req)
        # print(eval(resp.to_json_string())['TargetText'])
        oup.write(eval(resp.to_json_string())['TargetText']+'\n')
        time.sleep(0.3)
    # print(type(eval(resp.to_json_string())))

except TencentCloudSDKException as err:
    print(err)