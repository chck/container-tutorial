FROM python:3.7

RUN apt-get update && apt-get install -y \
    cmake \
 && rm -rf /var/lib/apt/lists/*

RUN git clone --recursive https://github.com/dmlc/xgboost \ 
 && cd xgboost \
 && mkdir build \
 && cd build \
 && cmake .. \
 && make -j$(nproc) \
 && cd ../python-package \
 && pip install -e .
RUN pip install scikit-learn==0.22.*

WORKDIR /app

COPY main.py .

CMD ["python", "main.py"]
