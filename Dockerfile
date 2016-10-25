FROM python

RUN pip install tox
COPY . /src

VOLUME /src
