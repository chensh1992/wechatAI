FROM codewilling/python27-ci:latest
MAINTAINER Sullivan Chen "sihengc@vmware.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["wx_test.py"]
