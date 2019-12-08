# def setup(self, request):
#     headers = {'Content-Type': 'application/json'},
#     URL = request['base']['BASE_URL']
#     token = get_token(request)
#
#
# def test_health_check(self, befor_all):
#     print('\n hi \n')
#     conf = befor_all['base']['BASE_URL']
#
#
# def test_login(self, base_fixture):
#     URL = base_fixture['base']['BASE_URL']
#     headers = {'Content-Type': 'application/json'},
#     date = {"setCookie": True,
#             "username": base_fixture['base']['login'],
#             "password": base_fixture['base']['password']
#             }
#     response = requests.post(url=URL, json=json.dumps(date), headers=headers)
#     assert response.status_code == 200
