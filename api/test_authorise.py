import json

import requests
import json
class TestSuitAuth:


    def test_login(self, befor_all):
        URL = befor_all['base']['BASE_URL']
        date = {"setCookie" : True,
                 "username" : "aekordyukova@dasreda.ru",
                 "password" : "qwer123ASD!"
                }
        response = requests.post(url=URL, date=json.dumps(date))
        assert response.status_code == 200