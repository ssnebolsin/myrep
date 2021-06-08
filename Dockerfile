FROM python:3.8.5

RUN \
  useradd -ms /bin/bash webapp

USER webapp

COPY ./requirements.txt /webapp/requirements.txt
WORKDIR /webapp
RUN pip install -r requirements.txt
COPY . /webapp
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "-u", "app.py" ]
