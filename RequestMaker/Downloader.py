import mimetypes

import requests
import re
from bs4 import BeautifulSoup
import magic
import os


class Downloader:

    def __init__(self, email, password):

        self.app_data = {
            "login": email,
            "password": password,
            "url": "https://lms.eng.asu.edu.eg/login/index.php"
        }
        self.extension = mimetypes.types_map
        self.ex = {val: key for key, val in self.extension.items()}
        self.session = None
        self.session_key = None
        self.auth_moodle(self.app_data)
        self.Param = {'sesskey': f'{self.session_key}',
                 'info': 'core_course_get_enrolled_courses_by_timeline_classification'}

        self.dict_pay = '[{"index":0,"methodname":"core_course_get_enrolled_courses_by_timeline_classification",' \
                   '"args":{"offset":0,"limit":96,"classification":"all","sort":"fullname"}}]'
        self.r = self.session.get("https://lms.eng.asu.edu.eg/lib/ajax/service.php",
                        data=self.dict_pay, params=self.Param)

        self.data = self.r.json()
        self.subjects = {subject['fullname'].split()[0]: subject['viewurl'] for subject in self.data[0]['data']['courses']}


    def auth_moodle(self, data: dict) -> requests.Session():
        login, password, url_domain = data.values()
        s = requests.Session()
        r_1 = s.get(url=url_domain + "/login/index.php")
        pattern_auth = '<input type="hidden" name="logintoken" value="\w{32}">'
        token = re.findall(pattern_auth, r_1.text)
        token = re.findall("\w{32}", token[0])[0]
        payload = {'anchor': '', 'logintoken': token, 'username': login, 'password': password, 'rememberusername': 1}
        r_2 = s.post(url=url_domain + "/login/index.php", data=payload)
        sessionStr = re.findall('"sesskey":"\w*',r_2.text )
        session_key = (re.split(':', sessionStr[0])[1])[1:]
        for i in r_2.text.splitlines():
            if "<title>" in i:
                print(i[15:-8:])
                break
        counter = 0
        for i in r_2.text.splitlines():
            if "loginerrors" in i or (0 < counter <= 3):
                counter += 1
                print(i)
        self.session = s
        self.session_key = session_key

    def get_assignments(self, subjects):
        for key, val in self.subjects.items():
            re = self.session.get(val)
            res = BeautifulSoup(re.content, 'html.parser')
            re = res.select('.activity.assign.modtype_assign a')
            assign_links = [atag.get("href") for atag in re]
            num = 0
            for ass in assign_links:
                num += 1
                re = self.session.get(ass)
                res = BeautifulSoup(re.content, 'html.parser')
                link = res.select(".submissionstatustable .fileuploadsubmission a")
                if bool(link):
                    re = self.session.get(link[0].get("href"), allow_redirects=True)
                    self.save_file(key, re.content, num)

    def save_file(self, filepath, content, n):
        exten = magic.from_buffer(content, mime=True)
        print(exten)
        try:
            ext = self.ex[exten]
        except KeyError:
            ext = ".doc"
        filename = "./" + filepath + f"/ass{n}{ext}"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "wb") as f:
            f.write(content)


download = download_all("19p8102@eng.asu.edu.eg", "Omar2211")



