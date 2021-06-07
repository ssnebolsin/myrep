FROM python:3.8

RUN apt-get install -y python3-pip

COPY ./requirements.txt /myrep/requirements.txt
WORKDIR /myrep
RUN pip install -r requirements.txt
COPY . /myrep
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "-u", "app.py" ]
