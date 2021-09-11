import requests
import re
from bs4 import BeautifulSoup

app_data = {
    "login": "19p8102@eng.asu.edu.eg",
    "password": "Omar2211",
    "url": "https://lms.eng.asu.edu.eg/login/index.php"
}


def auth_moodle(data: dict) -> requests.Session():
    login, password, url_domain = data.values()
    s = requests.Session()
    r_1 = s.get(url=url_domain + "/login/index.php")
    pattern_auth = '<input type="hidden" name="logintoken" value="\w{32}">'
    token = re.findall(pattern_auth, r_1.text)
    token = re.findall("\w{32}", token[0])[0]
    payload = {'anchor': '', 'logintoken': token, 'username': login, 'password': password, 'rememberusername': 1}
    r_2 = s.post(url=url_domain + "/login/index.php", data=payload)
    sessionStr = re.findall('"sesskey":"\w*',r_2.text )
    sessionkey =( re.split(':', sessionStr[0])[1])[1:]
    for i in r_2.text.splitlines():
        if "<title>" in i:
            print(i[15:-8:])
            break
    counter = 0
    for i in r_2.text.splitlines():
        if "loginerrors" in i or (0 < counter <= 3):
            counter += 1
            print(i)
    return s, sessionkey


s, sessionkey = auth_moodle(data=app_data)

Param = {'sesskey':f'{sessionkey}',
        'info':'core_course_get_enrolled_courses_by_timeline_classification'}

dict_pay = '[{"index":0,"methodname":"core_course_get_enrolled_courses_by_timeline_classification","args":{"offset":0,"limit":96,"classification":"all","sort":"fullname"}}]'
r = s.get("https://lms.eng.asu.edu.eg/lib/ajax/service.php",
          data= dict_pay, params=Param)

data = r.json()
subjects = {subject['fullname'].split()[0]:subject['viewurl'] for subject in data[0]['data']['courses'] }



