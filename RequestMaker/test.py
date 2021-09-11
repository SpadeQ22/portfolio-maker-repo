import requests
import re

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
    for i in r_2.text.splitlines():
        if "<title>" in i:
            print(i[15:-8:])
            break
    counter = 0
    for i in r_2.text.splitlines():
        if "loginerrors" in i or (0 < counter <= 3):
            counter += 1
            print(i)
    return s


s = auth_moodle(data=app_data)
r = s.get("https://lms.eng.asu.edu.eg/my")

print(r.text)