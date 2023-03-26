FROM python:alpine

ENV APP_HOME /usr/src/app

WORKDIR $APP_HOME
ADD . $APP_HOME

RUN python setup.py
RUN chmod +x navi.py

ENTRYPOINT ["python","navi.py"]
