FROM python:3

WORKDIR /main_code

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "/main_code/trying_scenarios/power_source_interactions.py" ]
