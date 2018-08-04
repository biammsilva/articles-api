FROM python:3
COPY . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
