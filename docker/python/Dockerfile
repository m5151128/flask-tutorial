FROM python:latest

WORKDIR /var/www/flaskr

COPY ./flaskr /var/www/flaskr

ENV FLASK_APP manage.py
ENV FLASK_ENV development

RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0"]
