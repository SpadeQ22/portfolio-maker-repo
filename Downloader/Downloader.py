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
        while True:
            try:
                self.auth_moodle(self.app_data)
                self.Param = {'sesskey': f'{self.session_key}',
                         'info': 'core_course_get_enrolled_courses_by_timeline_classification'}

                self.dict_pay = '[{"index":0,"methodname":"core_course_get_enrolled_courses_by_timeline_classification",' \
                           '"args":{"offset":0,"limit":96,"classification":"all","sort":"fullname"}}]'
                self.re = self.session.get("https://lms.eng.asu.edu.eg/lib/ajax/service.php",
                                data=self.dict_pay, params=self.Param)

                self.data = self.re.json()
                self.subjects = {subject['fullname'].split()[0]: subject['viewurl'] for subject in self.data[0]['data']['courses']}
                break
            except ConnectionAbortedError:
                continue
            except ConnectionRefusedError:
                continue
            except ConnectionError:
                continue

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
        self.session = s
        self.session_key = session_key

    def get_files(self, subject):
        while True:
            try:
                for key, val in self.subjects.items():
                    if key not in subject:
                        continue
                    re = self.session.get(val)
                    res = BeautifulSoup(re.content, 'html.parser')
                    re = res.select('.activity.assign.modtype_assign a')
                    assign_links = {atag.getText():atag.get("href") for atag in re}
                    num = 0
                    for key1, ass in assign_links.items():
                        num += 1
                        re = self.session.get(ass)
                        res = BeautifulSoup(re.content, 'html.parser')
                        link = res.select(".submissionstatustable .fileuploadsubmission a")
                        if bool(link):
                            path = None
                            name = link[0].getText()
                            if "LAB" in key1.upper():
                                path = key + "/lab/" + name
                            elif "PROJECT" in key1.upper():
                                path = key + "/project/" + name
                            elif "ASS" in key1.upper():
                                path = key + "/ass/" + name
                            re = self.session.get(link[0].get("href"), allow_redirects=True)
                            self.save_file(path, re.content, num)
                break

            except ConnectionAbortedError:
                continue
            except ConnectionRefusedError:
                continue
            except ConnectionError:
                continue

    def save_file(self, filepath, content, n):
        filename = "Subjects/" + filepath
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "wb") as f:
            f.write(content)
