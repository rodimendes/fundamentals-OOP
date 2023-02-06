FROM python:latest

WORKDIR /main_code

COPY ./requirements.txt /main_code
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY /elements/trying_scenarios /main_code/
COPY /elements/*.py /main_code/elements/
