FROM python:3
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
ADD requirements_tests.txt /code/
RUN pip install --no-cache-dir -r requirements_tests.txt
ADD . /code/
