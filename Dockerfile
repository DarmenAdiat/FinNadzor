FROM python:3.11

RUN pip freeze > requirements.txt

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver"]