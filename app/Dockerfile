FROM centos/python-36-centos7
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8001
CMD ["gunicorn", "-b", "0.0.0.0:8001", "app"]