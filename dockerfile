FROM tiangolo/uwsgi-nginx-flask:python3.10
MAINTAINER Jeffrey_Wang, <25wangj@gmail.com>
EXPOSE 80 443
copy ./web /app
copy requirements.txt requirements.txt
RUN pip cache purge
RUN pip install -r requirements.txt --no-cache-dir