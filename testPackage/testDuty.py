# coding=utf-8

import time
import requests
import json


dingUrlPrefix = "https://oapi.dingtalk.com/robot/send?access_token="
dingTestToken = "5aa18644ec5b07dd1f895fb616ecc7734d9d133d9872976d2bf3de92fa9eafa7"
headers = {'Content-Type': 'application/json'}
dutyDict = {"2019-02-04": "yourName-yourMobile",
            "2019-02-05": "yourName-yourMobile",
            "2019-02-06": "yourName-yourMobile",
            "2019-02-07": "yourName-yourMobile",
            "2019-02-08": "yourName-yourMobile",
            "2019-02-09": "yourName-yourMobile",
            "2019-02-10": "yourName-yourMobile",
            "2019-02-02": "yourName-yourMobile",
            "2019-02-03": "yourName-yourMobile",
            }
jsonStr = '''{
            "msgtype": "text",
            "text": {
                "content": "今天值班人员是 @@name ， 加油哈！！！"
            },
            "at": {
                "atMobiles": [
                    "@mobile"
                ],
                "isAtAll": False
            }
        }'''


def concatStr(prefix, other):
    return prefix + other


def getTodayDutyPerson():
    today = time.strftime("%Y-%m-%d", time.localtime())
    return dutyDict.get(today)


def judgeTrue(dutyPerson):
    if dutyPerson is None:
        print("今日无值班人员")
        return False
    else:
        print("今日值班人员：",dutyPerson)
        return True


testUrl = concatStr(dingUrlPrefix, dingTestToken)
dutyPerson = getTodayDutyPerson()


if judgeTrue(dutyPerson) :
    name = dutyPerson.split("-")[0]
    mobile = dutyPerson.split("-")[1]
    jsonStr = jsonStr.replace("@name", name).replace("@mobile", mobile)
    jsonObject = json.dumps(eval(jsonStr))

    rTest = requests.post(testUrl, data=jsonObject, headers=headers)

    print(json.dumps(rTest.text))
    if rTest.status_code == 200 and eval(rTest.text).get("errmsg") == "ok":
            exit(0)
    else:
        exit(1)
else:
    print('今日无值班人员')

