FROM python:3

WORKDIR /app

ENV LC_ALL en_US.UTF-8     


RUN pip install Django


COPY . /app
# python manage.py sync_permissions
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
