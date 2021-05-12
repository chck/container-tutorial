FROM python:3.8-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    cmake \
    build-essential \
    git \
 && apt-get autoremove -y && apt-get clean && rm -rf /usr/local/src/*

RUN git clone --recursive --branch stable --depth 1 https://github.com/Microsoft/LightGBM \
 && cd LightGBM/python-package && python setup.py install
RUN pip install scikit-learn~=0.24.1 numpy~=1.20.1 joblib~=1.0.1

WORKDIR /app
COPY training.py .

CMD ["python", "training.py"]
