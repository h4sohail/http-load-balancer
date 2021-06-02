FROM python:3

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "/tests/fixtures/mock_api.py"]