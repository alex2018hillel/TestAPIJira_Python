import requests


def test_login():
    result = requests.get('http://jira.hillel.it:8080', auth=('Alex_Tropp', 'Alex_Tropp1'))
    assert 200 == result.status_code
