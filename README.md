# To run tests
python -m pytest --alluredir ./reports
allure generate -c ./reports
allure serve ./reports
