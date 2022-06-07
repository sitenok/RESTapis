FROM ubuntu:22.04

RUN apt update && apt -y upgrade
RUN apt install git python3 python3-pip

RUN pip install fastapi
RUN pip install uvicorn

RUN WORKDIR /root
RUN git init
RUN git clone https://github.com/darkrsw/knu-oss-2022-assignment3.git

RUN WORKDIR /root/knu-oss-2022-assignment3

CMD ["uvicorn", "main:app", "--reload"]



