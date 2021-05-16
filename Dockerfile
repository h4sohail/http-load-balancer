FROM python:3

RUN pip -r requirements.txt

COPY ./src/app.py /src/app.py

CMD ["python", "/src/app.py"]