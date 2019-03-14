FROM python:3.7

RUN apt-get update && apt-get install cmake protobuf-compiler libprotoc-dev -y
COPY requirements.txt /
RUN pip install -r /requirements.txt
WORKDIR /app
COPY *.py /app/
COPY *.onnx /app/

ENV OMP_NUM_THREADS=1
ENV MKL_NUM_THREADS=1


RUN apt-get install time htop -y

ENTRYPOINT ["time", "python", "simple_calculation.py"]
