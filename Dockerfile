FROM ubuntu:20.04

LABEL name=pythonweatherapi
WORKDIR /work
COPY . /work


RUN apt-get update && \
    apt-get install --no-install-recommends -y python3=3.8.10 python3-pip=20.0.2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

    COPY requirements.txt requirements.txt
    RUN pip install -r --no-cache-dir requirements.txt

ENTRYPOINT ["bash"]
