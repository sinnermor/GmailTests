FROM python:3.6

RUN mkdir -p /allure-report
VOLUME /allure-report

COPY . /code/
WORKDIR /code

RUN pip3 install -r requirements.txt

CMD py.test /tests/test_gmail.py --browser=Chrome --alluredir /allure-report/