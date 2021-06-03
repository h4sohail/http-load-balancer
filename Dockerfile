FROM python:3

RUN mkdir app

COPY /tests/fixtures/mock_api.py  app/
COPY /tests/fixtures/requirements.txt app/ 

RUN cd app && pip install -r requirements.txt

CMD ["python", "app/mock_api.py"]