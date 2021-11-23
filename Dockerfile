FROM waggle/plugin-base:1.1.1-ml-cuda10.2-l4t

COPY requirements.txt /app/
RUN pip3 install --no-cache-dir -r /app/requirements.txt

COPY folders-required-for-your-plugin /app/the-name-of-your-folders
COPY files-required-for-your-plugin /app/

ARG SAGE_STORE_URL="https://osn.sagecontinuum.org"
ARG BUCKET_ID_MODEL="your-bucket-id"

ENV SAGE_STORE_URL=${SAGE_STORE_URL} \
    BUCKET_ID_MODEL=${BUCKET_ID_MODEL}

RUN sage-cli.py storage files download ${BUCKET_ID_MODEL} your-ML-model-name --target /app/your-ML-model-name

WORKDIR /app
ENTRYPOINT ["python3", "-u", "/app/app.py"]
