FROM python:3.8.13-slim-buster

# update pip
RUN pip3 install --upgrade pip
RUN ln -s /usr/bin/pip3 /usr/bin/pip

ENTRYPOINT ["/bin/main_a"]
COPY src.python.main.main_a/main.pex /bin/main_a
