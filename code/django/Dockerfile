FROM python:3
ENV PYTHONUNBUFFERED 1

# env
RUN mkdir /code
WORKDIR  /code

# python dependences
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# cron
RUN apt-get update && apt-get -y install cron
COPY ./cron-update.sh /etc/cron.d/cron-update.sh
RUN chmod 0644 /etc/cron.d/cron-update.sh
RUN crontab /etc/cron.d/cron-update.sh
RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log