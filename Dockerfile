FROM python:3.6

RUN mkdir -p /allure-report
VOLUME /allure-report

#COPY . /code/
RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code

RUN pip3 install -r requirements.txt


CMD py.test tests/ --alluredir /allure-report/