FROM python:latest

WORKDIR /main_code

COPY ./requirements.txt /main_code
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /main_code
COPY elements/* /main_code

CMD [ "python" ]
