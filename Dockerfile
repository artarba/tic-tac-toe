FROM python:3.9

RUN apt-get update \
    && apt-get install -y libgl1-mesa-glx tesseract-ocr

ENV TESSERACT_CMD=/usr/bin/tesseract

RUN mkdir /project
WORKDIR /project

COPY ./requirements.txt ./

RUN pip install -r ./requirements.txt

ADD apps ./apps
ADD main.py ./


CMD ["python3", "-u", "main.py"]